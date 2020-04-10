from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You preston!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()