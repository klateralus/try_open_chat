from pathlib import Path
import sys


def main():
    # prepare the environment
    path = str(Path().joinpath("packages").absolute())
    sys.path.append(path)

    import assistant
    assistant.start()


if __name__ == "__main__":
    main()
