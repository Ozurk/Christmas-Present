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
class Woods(Screen):
    pass

class Inventory(GridLayout):
    pass

class LockBox(Screen):
    def open(self, touch):
        if self.collide_point(*touch.pos):
            # Access the current app instance
            app = App.get_running_app()
            # Access the inventory screen's BoxLayout (inventory_box)
            inventory_box = app.root.ids.inventory
            if "key" in inventory_box.ids:
                app.root.ids.screenmanager.current = "Open_Box"


class Open_Box(Screen):
    def get_rope(self, touch):
        app = App.get_running_app()
        inventory_box = app.root.ids.inventory
        rope = Rope(size=(250, 250))
        inventory_box.add_widget(rope)
        self.ids.Open_Box_ID.source = "pics/Woods/open_box.png"
        

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
            inventory_box.ids["key"] = key
            inventory_box.add_widget(key)
        


class Matches(Image):
    def move_to_inventory(self, touch):
        if not self.collide_point(*touch.pos):
            return
        
        app = App.get_running_app()
        screen_manager = app.root.ids.screenmanager
        inventory_box = inventory_box = app.root.ids.inventory

        current_screen = screen_manager.current

        if current_screen == "Closet":
            # Handle moving the Candle from inventory to Closet
            self._move_to_closet(inventory_box, screen_manager)
        else:
            # Move Candle to inventory
            self._move_to_inventory(inventory_box)            
            

    def _move_to_closet(self, inventory_box, screen_manager):
        if "inventory_matches" in inventory_box.ids:
            # Remove the Candle from inventory
            Matches = inventory_box.ids.pop("inventory_matches")
            inventory_box.remove_widget(Matches)

            # Update the Closet screen's image
            closet_screen = screen_manager.get_screen("Closet")
            if closet_screen.ids.closet_image.source == "pics/closet/dark_closet_with_candle.png":
                closet_screen.ids.closet_image.source = "pics/closet/light_closet.png"
            else:
                closet_screen.ids.closet_image.source = "pics/closet/dark_closet_with_matches.png"
                closet_screen.ids.closet_text.text = "I wonder if there is a lamp or something that could be lit.."

    def _move_to_inventory(self, inventory_box):
            if self.parent:
                self.parent.remove_widget(self)

            # Create a new Candle widget and add it to the inventory
            new_matches = Matches(size=(250, 250), size_hint=(None, None)
            )
            inventory_box.ids["inventory_matches"] = new_matches
            inventory_box.add_widget(new_matches)


class Candle(Image):
    def move_to_inventory(self, touch):
        if not self.collide_point(*touch.pos):
            return  # Exit early if the touch is not on the Candle

        app = App.get_running_app()
        screen_manager = app.root.ids.screenmanager
        inventory_box = app.root.ids.inventory

        # Debugging current state
        current_screen = screen_manager.current
        print(f"Current screen: {current_screen}")
        print(f"App ids: {app.root.ids}")

        if current_screen == "Closet":
            # Handle moving the Candle from inventory to Closet
            self._move_to_closet(inventory_box, screen_manager)
        else:
            # Move Candle to inventory
            self._move_to_inventory(inventory_box)

    def _move_to_closet(self, inventory_box, screen_manager):
        """Move the Candle widget from the inventory to the Closet screen."""
        if "inventory_candle" in inventory_box.ids:
            # Remove the Candle from inventory
            candle = inventory_box.ids.pop("inventory_candle")
            inventory_box.remove_widget(candle)

            # Update the Closet screen's image
            closet_screen = screen_manager.get_screen("Closet")
            if closet_screen.ids.closet_image.source == "pics/closet/dark_closet_with_matches.png":
                closet_screen.ids.closet_image.source = "pics/closet/light_closet.png"
            else:
                closet_screen.ids.closet_image.source = "pics/closet/dark_closet_with_candle.png"
                closet_screen.ids.closet_text.text = "A candle is only good when lit"

    def _move_to_inventory(self, inventory_box):
        """Move the Candle widget to the inventory."""
        # Remove the Candle from its current parent
        if self.parent:
            self.parent.remove_widget(self)

        # Create a new Candle widget and add it to the inventory
        new_candle = Candle(
            source=self.source, size=(200, 200), size_hint=(None, None)
        )
        inventory_box.ids["inventory_candle"] = new_candle
        inventory_box.add_widget(new_candle)


class Rope(Image):
    pass

class Barn(Screen):
    pass

if __name__ == '__main__':
    app = ChristmasPresentApp()
    app.run()