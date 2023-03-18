# base modules
from PySide2.QtCore import Slot, QThreadPool, QObject, Qt, QUrl, QSize
from PySide2.QtWidgets import QPushButton, QTextEdit, QVBoxLayout, QLabel, QMessageBox, QMainWindow
from PySide2.QtGui import QKeyEvent, QDesktopServices
from functools import partial
from getpass import getuser
# ai assistant
from .ai_communication import OpenChatQuery
from .ai_communication import Message as _Message
from .ai_communication import Roles as _Roles
from .ui_compiled.main import Ui_AIAssistantWindow as _UI_AssistantWindow
from .ui_settings import AIAssistantSettingsWindow as _SettingsWindow
from .ai_settings import get_temperature, get_model, get_tokens, get_behavior
from .ai_api_key import get_api_key


class AssistantWindow(QMainWindow):
    PAGE_HOW_TO_CREATE_KEY = "https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0"
    PAGE_API_KEY = "https://platform.openai.com/account/api-keys"

    def __init__(self):
        super().__init__()
        self.ui = _UI_AssistantWindow()
        self.ui.setupUi(self)
        # preparing the threading pool
        self._thread_pool = QThreadPool()

        self._end_user = getuser()

        self._messages = []

        self.settings_changed()
        self.connect_signals()

        self._count = 0

        self._is_listening_settings = False

    def _add_behavior(self, behavior: str):
        self._messages.append(
            {_Message.ROLE.value: _Roles.SYSTEM.value, _Message.CONTENT.value: behavior},
        )

    @property
    def send_button(self) -> QPushButton:
        return self.ui.pushButtonSend

    @property
    def request_edit(self) -> QTextEdit:
        return self.ui.requestEdit

    @property
    def prompt(self) -> str:
        return self.request_edit.toPlainText()

    @property
    def message_area(self) -> QVBoxLayout:
        return self.ui.verticalLayoutMessages

    def connect_signals(self):
        self.send_button.clicked.connect(self.send_request)
        self.request_edit.installEventFilter(self)
        self.ui.actionPreferences.triggered.connect(self.open_settings_window)

        open_how_to_create = partial(self.open_web_page, self.PAGE_HOW_TO_CREATE_KEY)
        self.ui.actionHow_to_make_API_key.triggered.connect(open_how_to_create)

        open_api_key = partial(self.open_web_page, self.PAGE_API_KEY)
        self.ui.actionMake_new_API_key.triggered.connect(open_api_key)

    def eventFilter(self, sender: QObject, event: QKeyEvent):
        if event.type() == QKeyEvent.KeyPress and sender is self.request_edit:
            if event.key() == Qt.Key_Return and bool(event.modifiers() & Qt.ControlModifier) and self.request_edit.hasFocus():
                self.send_request()

        return super().eventFilter(sender, event)

    def send_request(self):
        self.add_request(self.prompt)
        open_chat_query = OpenChatQuery(messages=list(self._messages),
                                        api_key=get_api_key(),
                                        end_user=self._end_user)

        open_chat_query.set(self.append_response, self.raise_exception, self.finish_request, *self.add_response(""))
        self._thread_pool.start(open_chat_query)
        self.request_edit.clear()

    @Slot(QLabel, tuple)
    def raise_exception(self, label: QLabel, index: int, error: tuple):
        exception_type, info = error
        self.append_error(label, index, f"Open AI ERROR: {info}")
        QMessageBox.critical(None,
                             str(exception_type),
                             info)
        raise exception_type(info)

    def add_message(self, message: str, margin=4,
                    alignment=Qt.AlignRight | Qt.AlignVCenter,
                    background="rgb(255, 255, 255)",
                    role: str = _Roles.USER.value) -> (QLabel, int):
        label = QLabel(message)
        label.setMargin(margin)
        label.setWordWrap(True)
        label.setAlignment(alignment)
        label.setStyleSheet(self.background(background))
        self.message_area.addWidget(label)
        index = len(self._messages)
        self._messages.append({_Message.ROLE.value: role, _Message.CONTENT.value: message})
        return label, index

    @Slot(str)
    def add_request(self, message: str) -> (QLabel, int):
        return self.add_message(message,
                                alignment=Qt.AlignRight | Qt.AlignVCenter,
                                background="rgb(255, 255, 255)",
                                role=_Roles.USER.value)

    @Slot(str)
    def add_response(self, message: str) -> (QLabel, int):
        return self.add_message(message,
                                alignment=Qt.AlignLeft | Qt.AlignVCenter,
                                background="rgb(255, 255, 253)",
                                role=_Roles.ASSISTANT.value)

    def append_part(self, label: QLabel, index: int, part: str, background: str):
        # update messages array
        message_info = self._messages[index]
        message = message_info.get(_Message.CONTENT.value, "")
        message_info[_Message.CONTENT.value] = f"{message}{part}"

        # update ui
        text = label.text()
        label.setText(f"{text}{part}")
        label.setStyleSheet(self.background(background))

    @Slot(QLabel, str)
    def append_response(self, label: QLabel, index: int, part: str):
        self.append_part(label, index, part, "rgb(255, 255, 253)")

    @Slot(QLabel, str)
    def append_error(self, label: QLabel, index:int, part: str):
        self.append_part(label, index, part, "rgb(253, 249, 249)")

    @Slot()
    def finish_request(self):
        self._count += 1

    @staticmethod
    def background(color: str) -> str:
        return f"QLabel {{background-color: {color}}} "

    def open_settings_window(self):
        settings_window = _SettingsWindow(self)
        settings_window.show()
        if not self._is_listening_settings:
            settings_window.settings_changed.connect(self.settings_changed)
            self._is_listening_settings = True

    @Slot()
    def settings_changed(self):
        self.key_api_changed()
        self.model_changed()
        self.creativity_changed()
        self.talkativeness_changed()
        self.behavior_changed()

    def key_api_changed(self):
        api_key = get_api_key()
        if api_key:
            self.send_button.setDisabled(False)
            self.request_edit.setDisabled(False)
            self.request_edit.setStyleSheet("")
            self.request_edit.clear()
        else:
            self.send_button.setDisabled(True)
            self.request_edit.setDisabled(True)
            self.request_edit.setText("Please provide an API Key in 'Settings -> Preferences'")
            style = "QTextEdit {background-color: rgb(255, 235, 235); font: 18pt \"Segoe UI\"}"
            self.request_edit.setStyleSheet(style)

    def model_changed(self):
        model_nice_name = get_model().replace("-", " ").capitalize()
        self.ui.labelModelName.setText(f"Model: '{model_nice_name}'")

    def creativity_changed(self):
        creativity = get_temperature()
        self.ui.labelCreativity.setText(f"Creativity: {creativity}")

    def talkativeness_changed(self):
        talkativeness = get_tokens()
        self.ui.labelTalkativeness.setText(f"Talkativeness: {talkativeness}")

    def behavior_changed(self):
        self._add_behavior(get_behavior())

    def open_web_page(self, page_address: str):
        url = QUrl(page_address)
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, "Can't open Page", f"Could not open confluence page {page_address}")
