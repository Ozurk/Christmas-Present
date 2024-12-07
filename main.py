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
    
    
class ChristmasPresent(BoxLayout):
    pass


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

class Inventory(GridLayout):
    pass

class Key(Image):
    def move_to_inventory(self, touch):
        if self.collide_point(*touch.pos):
            # Access the current app instance
            app = App.get_running_app()
            # Access the inventory screen's BoxLayout (inventory_box)
            inventory_box = inventory_box = app.root.ids.inventory

            # Remove the key from its current parent
            if self.parent:
                self.parent.remove_widget(self)

            key = Key(size=(250, 250))
            inventory_box.add_widget(key)


class Matches(Image):
    def move_to_inventory(self, touch):
        if self.collide_point(*touch.pos):
            # Access the current app instance
            app = App.get_running_app()
            # Access the inventory screen's BoxLayout (inventory_box)
            inventory_box = inventory_box = app.root.ids.inventory

            # Remove the key from its current parent
            if self.parent:
                self.parent.remove_widget(self)

            matches = Matches(size=(250, 250))
            inventory_box.add_widget(matches)

class Candle(Image):
    def move_to_inventory(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            print("--" + app.root.ids.screenmanager.current + "--")
            print(app.root.ids)
            inventory_box = app.root.ids.inventory
            if str(app.root.ids.screenmanager.current) == "Closet":
                if "inventory_candle" in inventory_box.ids:
                    candle = inventory_box.ids["inventory_candle"]
                    inventory_box.remove_widget(candle)
                    closet_screen = app.root.ids.screenmanager.get_screen("Closet")
                    closet_screen.ids.closet_image.source = "pics/closet/dark_closet_with_candle.png"
                    return

            # Remove the key from its current parent
            if self.parent:
                self.parent.remove_widget(self)

            
            widget = Candle(source=self.source, size=(200, 200), size_hint=(None, None))
            inventory_box.ids["inventory_candle"] = widget
            inventory_box.add_widget(widget)


class Barn(Screen):
    pass

if __name__ == '__main__':
    app = ChristmasPresentApp()
    app.run()