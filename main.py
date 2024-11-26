from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.uix.popup import Popup
from time import sleep
from kivy.base import Builder

Builder.load_file("ChristmasPresent.kv")

class ChristmasPresentApp(App):
    def build(self):
        app = ChristmasPresent()
        app.transition = RiseInTransition()
        return app
    
    
class ChristmasPresent(ScreenManager):
    pass

class HomeScreen(Screen):
    pass



if __name__ == '__main__':
    app = ChristmasPresentApp()
    app.run()