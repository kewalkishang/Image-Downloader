from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Design(BoxLayout):
      
    def change_text(self, userInput):
        userInput.text="hey you clicked shit!"




class DownloaderApp(App):
    def build(self):
        return Design()

DownloaderApp().run()