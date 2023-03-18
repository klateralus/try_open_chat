# base modules
from functools import partial
from enum import Enum
from PySide2.QtCore import QObject, Signal, QRunnable, Slot
from PySide2.QtWidgets import QLabel
import openai
# tool modules
from .ai_models import MODELS as _MODELS


class Roles(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Message(Enum):
    ROLE = "role"
    CONTENT = "content"


class Choice(Enum):
    MESSAGE = "message"
    FINISH_REASON = "finish_reason"
    INDEX = "index"
    DELTA = "delta"


class Response(Enum):
    ID = "id"
    OBJECT = "object"
    CREATED = "created"
    MODEL = "model"
    USAGE = "usage"
    CHOICES = "choices"


class Request(Enum):
    MODEL = "model"
    MESSAGES = "messages"
    TEMPERATURE = "temperature"
    N = "n"
    STREAM = "stream"
    USER = "user"


class AIQuerySignals(QObject):
    finished = Signal()
    exception_raised = Signal(tuple)
    response_received = Signal(str)


class OpenChatQuery(QRunnable):
    def __init__(self, messages: list, api_key: str, end_user: str):
        super().__init__()
        # we're hardcoding the usage of "gpt-3.5-turbo"
        self._model = _MODELS[6].name
        self._messages = list(messages)
        self._api_key = api_key
        self._end_user = end_user
        # signals handler
        self._signals = AIQuerySignals()

    def set(self, received, raised, finished, label: QLabel, index: int):
        raised_exception = partial(raised, label, index)
        self._signals.exception_raised.connect(raised_exception)

        self._signals.finished.connect(finished)

        response_received = partial(received, label, index)
        self._signals.response_received.connect(response_received)

    @Slot()
    def run(self):
        openai.api_key = self._api_key

        try:
            # for tests without using expensive tokens
            production = True
            if production:
                self.communicate_with_ai()
            else:
                self.simulate_communication()

        except Exception as e:
            self._signals.exception_raised.emit((type(e), str(e)))
        finally:
            self._signals.finished.emit()

    def communicate_with_ai(self):
        request = {
            Request.MODEL.value: self._model,
            Request.USER.value: self._end_user,
            Request.MESSAGES.value: self._messages,
            Request.STREAM.value: True,
        }

        response = openai.ChatCompletion.create(
            **request
        )

        for part in response:
            message_part = OpenChatQuery._extract_message_part(part)
            self._signals.response_received.emit(message_part)

    @staticmethod
    def _extract_message_part(part: dict) -> str:
        choices = part.get(Response.CHOICES.value, [])
        if not choices:
            return ""

        message_struct = OpenChatQuery._extract_message_struct(choices[0])
        return message_struct.get(Message.CONTENT.value, "")

    @staticmethod
    def _extract_message_struct(choice: dict) -> dict:
        if Choice.MESSAGE.value in choice:
            message = choice.get(Choice.MESSAGE.value, dict())
        elif Choice.DELTA.value in choice:
            message = choice.get(Choice.DELTA.value, dict())
        else:
            message = dict()

        return message

    def simulate_communication(self):
        raise RuntimeError("Simulate Communication is not implemented")


class AIQuery(QRunnable):
    def __init__(self, prompt: str, api_key: str, model=_MODELS[0].name, max_tokens=100, temperature=0.5, n=1, stop=None):
        """ Class for making a threaded request to AI

        Args:
            prompt: The questions itself
            model: The model to use, default is text-davinci-002
            max_tokens: How long the response should be [25-4096]
            temperature: How creative is the model should be [0.0 - 1.0]
            n: How many responses should AI generate? [1-4]
            stop: Stop tokens, like "Thanks," "Thank you,"
        """
        super().__init__()
        self._prompt = prompt
        self._api_key = api_key
        self._model = model
        self._max_tokes = max_tokens
        self._temperature = temperature
        self._n = n
        self._stop = stop
        self._signals = AIQuerySignals()

    def set(self, received, raised, finished, label: QLabel, index: int):
        raised_exception = partial(raised, label, index)
        self._signals.exception_raised.connect(raised_exception)

        self._signals.finished.connect(finished)

        response_received = partial(received, label, index)
        self._signals.response_received.connect(response_received)

    @Slot()
    def run(self):
        openai.api_key = self._api_key

        try:
            # for tests without using expensive tokens
            production = True
            if production:
                self.communicate_with_ai()
            else:
                self.simulate_communication()

        except Exception as e:
            self._signals.exception_raised.emit((type(e), str(e)))
        finally:
            self._signals.finished.emit()

    def simulate_communication(self):
        if self._prompt == "error":
            raise RuntimeError("Test Error!")
        if self._prompt == "slow":
            from time import sleep
            for i in range(32):
                partial_message = f"Part 0{i} "
                self._signals.response_received.emit(partial_message)
                sleep(0.1)
        else:
            self._signals.response_received.emit(f"Test response!\n"
                                                 f"Model parameters:\n"
                                                 f" model: {self._model}\n"
                                                 f" prompt: \"{self._prompt}\"\n"
                                                 f" tokens: {self._max_tokes}\n"
                                                 f" temperature: {self._temperature}\n"
                                                 f" api key: {self._api_key}")

    def communicate_with_ai(self):
        response = openai.Completion.create(
            model=self._model,
            prompt=self._prompt,
            temperature=self._temperature,
            max_tokens=self._max_tokes,
            n=self._n,
            stop=self._stop,
            # to make receiving of response similar to open chat gpt
            stream=True,
        )
        for block in response:
            self._signals.response_received.emit(block.choices[0].text)
