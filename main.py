from kivy.app import App
from kivy.uix.label import Label

class KrotApp(App):
    def build(self):
        return Label(text='تطبيق ناجح عبر GitHub Actions')

if __name__ == '__main__':
    KrotApp().run()
