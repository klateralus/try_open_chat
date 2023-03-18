def start():
    import sys
    from PySide2.QtWidgets import QApplication
    from .ui import AssistantWindow

    application = QApplication(sys.argv)

    assistant_window = AssistantWindow()
    assistant_window.show()

    application.exec_()
