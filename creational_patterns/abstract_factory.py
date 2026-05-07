class WindowsButton:
    def render(self):
        return "Windows Button"

class MacButton:
    def render(self):
        return "Mac Button"

class GUIFactory:
    def create_button(self, type):
        if type == "windows":
            return WindowsButton()
        elif type == "mac":
            return MacButton()
