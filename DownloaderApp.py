from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty,StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from ImageDownloader import getSynsetId , getImageLinks,downloadFromImageNet
from kivy.lang import Builder
from kivy.utils import platform 
import urllib.request

class SearchGUI(BoxLayout):
    popup=None
    search_input = ObjectProperty()
         
    def PopupMsg(self,buttonT,LabelT):
                print("popup")
                content = GridLayout(cols=1)
                content_cancel = Button(text=buttonT, size_hint_y=None, height=40)
                content.add_widget(Label(text=LabelT))
                content.add_widget(content_cancel)
                self.popup = Popup(title='Error!', content=content,
                size_hint=(None, None), size=(400, 400),auto_dismiss=False)
                content_cancel.bind(on_release=self.popup.dismiss)
                self.popup.open()
        
    
    def search(self, userInput):
       
        print(userInput.text)
        if userInput.text:
            si = userInput.text
            siu= si.replace(" ","_")
            global test
            test= siu
            #print("si -"+si+" siu -"+siu+" siu")
            sid=getSynsetId(siu)
            sidn,n=sid.split("-")
            if sidn=="0000":
                self.PopupMsg("Retry!","Unknown Noun!")
            else:
                self.imagelinks=getImageLinks(sidn)
                global ima
                ima= self.imagelinks
                #self.dp = DownlGUI()
                self.ResetGUI(si,self.imagelinks)
                print("here ma")
                
        else:
             self.PopupMsg("Ooh okay!","No search text found!")    
            
        #http://image-net.org/api/text/imagenet.synset.geturls?
    
    def ResetGUI(self,imageName, imagelinks):
        print("in resset")
        self.clear_widgets()
        self.dg= DownloaderGUI()
        self.dg.Updatetexts()
        self.add_widget(self.dg)
           

class DownloaderGUI(BoxLayout):
    
    
    imageslist = []
    imageN = "no name"
    spath="path"
    def Updatetexts(self):
        self.ids.pb.value = 50
        self.ids.ImageCount.text="Found "+str(len(ima))+" images of "+ test 
       
    #folder_text="Asdas"
    def download(self):
        self.ids.downloadb.text="Downloading.."
        self.ids.downloadb.disabled=True
        #self.imageDownload()
            
            
    def imageDownload(self):
          for n in range(0,len(ima)):
             #self.ids.pb.value= n         
             fpath=self.spath+"\\"+test+""+str(n)+".jpg"
             #print(fpath)
             try:
                  urllib.request.urlretrieve(ima[n],fpath)
             except:
                 pass
         
             
             
                                    
                                    
    def GotoSelector(self):
        self.clear_widgets()
        self.add_widget(FolderSelector())
    
    def GoBackToSearch(self):
        self.clear_widgets()
        self.add_widget(SearchGUI())
        
    def setPath(self,path):
        self.ids.selectText.text=path
        self.ids.downloadb.disabled=False
        self.spath=path
       
        
   
         
class FolderSelector(BoxLayout):
    def __init__(self, **kwargs):
        super(FolderSelector, self).__init__(**kwargs)
        self.drives_list.adapter.bind(on_selection_change=self.drive_selection_changed)

    def get_win_drives(self):
        if platform == 'win':
            import win32api

            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split('\000')[:-1]

            return drives
        else:    
            return []

    def drive_selection_changed(self, *args):
        selected_item = args[0].selection[0].text
        self.file_chooser.path = selected_item
    
    
    def selectfolder(self, path, filename):
        self.clear_widgets()
        
        self.fs= DownloaderGUI()
        self.fs.setPath(path)
        self.fs.Updatetexts()
        self.add_widget(self.fs)
        print(path)    
                
                
                
class DownloaderApp(App):
    def build(self):
        
        return SearchGUI()

DownloaderApp().run()