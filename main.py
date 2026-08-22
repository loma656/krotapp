from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "15dp"

        MDTopAppBar:
            title: "Krot App"

        MDLabel:
            text: "تطبيق جاهز للبناء عبر Buildozer"
            halign: "center"
"""

class KrotApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    KrotApp().run()
