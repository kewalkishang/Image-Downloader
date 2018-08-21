from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from ImageDownloader import getSynsetId , getImageLinks



class Design(BoxLayout):
    popup=None
    search_input = ObjectProperty()
         
       
    def change_text(self, userInput):
       # userInput.text="hey you clicked shit!"
        print(userInput.text)
        if userInput.text:
            sid=getSynsetId(userInput.text)
            sidn,n=sid.split("-")
            if sidn=="0000":
                content = GridLayout(cols=1)
                content_cancel = Button(text='Try again!', size_hint_y=None, height=40)
                content.add_widget(Label(text='Noun doesnt exist!'))
                content.add_widget(content_cancel)
                popup = Popup(title='Error!', content=content,
                size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                content_cancel.bind(on_release=popup.dismiss)
                popup.open()    
            else:
                getImageLinks(sidn)
            
        #http://image-net.org/api/text/imagenet.synset.geturls?
        

class DownloaderApp(App):
    def build(self):
        return Design()

DownloaderApp().run()