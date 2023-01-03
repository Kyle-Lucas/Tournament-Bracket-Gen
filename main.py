from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (1280, 720)    # (Width, Height)

class Main(FloatLayout):

    # Once The 8 Players are all inserted and Tournament Begins
    Players_Locked = False

    # An Integer to keep track of what we're currently changing
    Editing = 0

    # A List of id's set in kv file that we can easily Access as Numbers with Variable Above
    EditList = [
        'Tournament Title', 
        'Player 1', 
        'Player 2', 
        'Player 3', 
        'Player 4', 
        'Player 4', 
        'Player 5', 
        'Player 6', 
        'Player 7', 
        'Player 8'
        ]

    Edited =  [
        'Tournament Title', 
        'Player 1', 
        'Player 2', 
        'Player 3', 
        'Player 4', 
        'Player 4', 
        'Player 5', 
        'Player 6', 
        'Player 7', 
        'Player 8'
        ]

    # Switch Between Fields we can Edit
    def Switch_Edit(self,widget, Direction):

        if Direction == 'right':

            if self.Editing < len(self.EditList) - 1:
                
                self.Editing += 1
        
        if Direction =='left':

            if self.Editing > 0:

                self.Editing -= 1

        Type_Text = self.ids['txtinp']
        Type_Text.text = self.Edited[self.Editing]

        
    def validate(self,widget):

        # We set which ever id is currently active via EditList[Editing]
        Set_As = self.ids[self.EditList[self.Editing]]
        Set_As.text = widget.text
        self.Edited[self.Editing] = widget.text

    def Shuffle_Players(self,widget):
        # Quite Simple, Will only work if Players_Locked = True
        pass

class Alkahmi(App):
    def build(self):
        return 

if __name__ == "__main__"    :

    Alkahmi().run()