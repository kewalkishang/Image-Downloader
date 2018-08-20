from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from ImageDownloader import getSynsetId



class Design(BoxLayout):
    popup=None
    search_input = ObjectProperty()
    
    def chane():
       print("hello")
       
       
    def change_text(self, userInput):
       # userInput.text="hey you clicked shit!"
        print(userInput.text)
        getSynsetId(userInput.text)
        
        

class DownloaderApp(App):
    def build(self):
        return Design()

DownloaderApp().run()