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
from kivy.graphics import Rectangle
from kivy.uix.image import Image

Builder.load_file("ChristmasPresent.kv")

class ChristmasPresentApp(App):
    def build(self):
        app = ChristmasPresent()
        app.transition = RiseInTransition()
        return app
    
    
class ChristmasPresent(ScreenManager):
    inventory = {}
    inventory_button = Button()

    def go_to_inventory(self):
        self.current = "Inventory"
    
    inventory_button.on_press = go_to_inventory


class HomeScreen(Screen):
    pass

class LivingRoom(Screen):
    pass

class DownstairsLivingRoom(Screen):
    pass

class HuntersRoom(Screen):
    pass

class Barn(Screen):
    pass

class LaundryRoom(Screen):
    pass

class HalfBath(Screen):
    pass

class Closet(Screen):
    pass

class Kitchen(Screen):
    pass

class Hallway(Screen):
    pass

class Outside(Screen):
    pass

class Inventory(Screen):
    pass

class Key(Image):
    def move_to_inventory(self, touch):
        if self.collide_point(*touch.pos):
            # Access the current app instance
            app = App.get_running_app()
            # Access the inventory screen's BoxLayout (inventory_box)
            inventory_box = app.root.get_screen("Inventory").ids.inventory_box

            # Remove the key from its current parent
            if self.parent:
                self.parent.remove_widget(self)

            key = Key()
            inventory_box.add_widget(key)


class Matches(Image):
    def move_to_inventory(self, touch):
        if self.collide_point(*touch.pos):
            # Access the current app instance
            app = App.get_running_app()
            # Access the inventory screen's BoxLayout (inventory_box)
            inventory_box = app.root.get_screen("Inventory").ids.inventory_box

            # Remove the key from its current parent
            if self.parent:
                self.parent.remove_widget(self)

            matches = Matches()
            inventory_box.add_widget(matches)

class Barn(Screen):
    pass

if __name__ == '__main__':
    app = ChristmasPresentApp()
    app.run()