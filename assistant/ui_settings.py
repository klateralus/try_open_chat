from __future__ import annotations
# base modules
from PySide2.QtCore import Signal, QObject, Qt, QSize
from PySide2.QtWidgets import QPushButton, QInputDialog, QLineEdit, QLabel, QMainWindow
from PySide2.QtGui import QPixmap
from string import capwords
# base project  modules
from .ui_compiled.settings import Ui_AISettingsWindow as _Ui_AISettingsWindow
from .ai_api_key import set_api_key, get_api_key
from .ai_settings import get_model, get_temperature, get_tokens, set_model, set_temperature, set_tokens, set_behavior
from .ai_settings import get_behavior
from . import ai_models


class AISettingsSignals(QObject):
    key_api_changed = Signal()


class AIAssistantSettingsWindow(QMainWindow):
    native_tool_name = "AIAssistantSettingsTool"
    native_tool_size = QSize(649, 516)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = _Ui_AISettingsWindow()
        self.ui.setupUi(self)
        self._signals = AISettingsSignals()
        self._image: QPixmap | None = None

        self.update_api_key_status()
        self.initialize_model()
        self.initialize_creativity()
        self.initialize_talkativeness()
        self.initialize_behavior()

        self.connect_signals()

    def resizeEvent(self, event):
        self.update_model_label()
        return super().resizeEvent(event)

    @property
    def api_key_status(self) -> QLabel:
        return self.ui.labelAPIKeyStatus

    @property
    def set_key_button(self) -> QPushButton:
        return self.ui.pushButtonSetAPIKey

    def connect_signals(self):
        self.set_key_button.clicked.connect(self.set_key)
        self.creativity_slider.valueChanged.connect(self.set_creativity)
        self.talkative_slider.valueChanged.connect(self.set_talkativeness)
        self.behavior_lineedit.editingFinished.connect(self.set_behavior)

    def set_key(self):
        text, ok = QInputDialog.getText(self, "API KEY",
                                        "Input your API KEY here:",
                                        QLineEdit.Normal)
        if ok and text:
            set_api_key(text)
            self.update_api_key_status()
            self.settings_changed.emit()

    def update_api_key_status(self):
        api_key = get_api_key()
        status = "API key is set" if api_key else "No API key"
        self.api_key_status.setText(f"Status: {status}")

    @property
    def settings_changed(self) -> Signal:
        return self._signals.key_api_changed

    @property
    def model_label(self):
        return self.ui.labelModelImage

    @property
    def model_description(self):
        return self.ui.labelModelDescription

    @property
    def model_name(self):
        return self.ui.labelModelName

    def set_nice_model_name(self, name: str):
        new_name = capwords(name.replace("-", " "))
        self.model_name.setText(new_name)

    def initialize_model(self):
        self.update_model_info()

    @property
    def creativity_slider(self):
        return self.ui.horizontalSliderCreativity

    def initialize_creativity(self):
        value = int(get_temperature() * 100)
        self.creativity_slider.setValue(value)

    def set_creativity(self):
        if self.creativity_slider.hasTracking():
            value = self.creativity_slider.value() / self.creativity_slider.maximum()
            set_temperature(value)
            self.settings_changed.emit()

    @property
    def talkative_slider(self):
        return self.ui.horizontalSliderTalkativeness

    def initialize_talkativeness(self):
        self.talkative_slider.setValue(get_tokens())

    def set_talkativeness(self):
        if self.talkative_slider.hasTracking():
            tokens = self.talkative_slider.value()
            set_tokens(tokens)
            self.settings_changed.emit()

    def update_model_info(self):
        # now we use hardcoded "gpt-3.5-turbo"
        set_model(get_model())
        index = ai_models.get_model_index(get_model())
        self.set_model_image(ai_models.get_model_image(index))
        self.model_description.setText(ai_models.get_model_description(index))
        self.set_nice_model_name(ai_models.get_model_name(index))

    def set_model_image(self, path: str):
        self._image = QPixmap(path)
        self.update_model_label()

    def update_model_label(self):
        w = self.model_label.width()
        h = self.model_label.height()
        if self._image:
            self.model_label.setPixmap(self._image.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    @property
    def behavior_lineedit(self) -> QLineEdit:
        return self.ui.lineEditBehavior

    def set_behavior(self):
        set_behavior(self.behavior_lineedit.text())
        self.settings_changed.emit()

    def initialize_behavior(self):
        self.behavior_lineedit.setText(get_behavior())

