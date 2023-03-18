from pathlib import Path


class Model(object):
    __slots__ = ("name", "description")

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


MODELS = [
    Model("text-ada-001", "Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost."),
    Model("text-babbage-001", "Capable of straightforward tasks, very fast, and lower cost."),
    Model("text-curie-001", "Very capable, but faster and lower cost than Davinci."),
    Model("text-davinci-003", "Most capable GPT-3 model. Can do any task the other models can do, often with higher quality, longer output and better instruction-following. Also supports inserting completions within text."),
    Model("code-davinci-002", "Most capable Codex model. Particularly good at translating natural language to code. In addition to completing code, also supports inserting completions within code."),
    Model("code-cushman-001", "Almost as capable as Davinci Codex, but slightly faster. This speed advantage may make it preferable for real-time applications."),
    Model("gpt-3.5-turbo", "Turbo is the same model family that powers ChatGPT. It is optimized for conversational chat input and output but does equally well on completions when compared with the Davinci model family. Any use case that can be done well in ChatGPT should perform well with the Turbo model family in the API. The Turbo model family is also the first to receive regular model updates like ChatGPT. Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003. Will be updated with our latest model iteration."),
]


def get_count() -> int:
    return len(MODELS)


def get_last_index() -> int:
    return get_count() - 1


def get_model_index(name: str) -> int:
    for i, model in enumerate(MODELS):
        if model.name == name:
            return i

    return -1


def _get_image_path(name: str) -> str:
    path = Path(__file__).parent.joinpath(f"ui_source/images/{name}.png")
    return str(path.as_posix())


def get_model_name(index: int) -> str:
    model = MODELS[index]
    return model.name


def get_model_description(index: int) -> str:
    model = MODELS[index]
    return model.description


def get_model_image(index: int) -> str:
    return _get_image_path(get_model_name(index))

