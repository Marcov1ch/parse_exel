from views.gui import RemarksApp

class MainController:
    def __init__(self):
        self.app = RemarksApp()

    def start(self):
        self.app.run()
