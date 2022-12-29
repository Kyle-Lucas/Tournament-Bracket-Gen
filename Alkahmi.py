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

    # Editing is an Integer that will keep track of which info we want to change
    Editing = 0
    EditList = ['Tournament Title', 'Player 1', 'Player 2']

    def NextEdit(self,widget):

        if self.Editing < len(self.EditList) - 1:
            
            self.Editing += 1
            print(f' {self.Editing}')

            CurrentEdit = self.ids['edit']
            CurrentEdit.text = self.EditList[self.Editing]

    def PreviousEdit(self,widget):

        # We dont want to go below 0
        if self.Editing > 0:

            self.Editing -= 1
            print(f' {self.Editing}')

            CurrentEdit = self.ids['edit']
            CurrentEdit.text = self.EditList[self.Editing]

    def validate(self,widget):

        # Editing = 0 >> Change Tournament Title
        # Editing = 1 >> Player 1
        # etc
        
        if self.Editing == 1:

            Player1 = self.ids['P1']
            Player1.text = widget.text


"""
    def on_text_validate(self, widget):

        button = self.ids['bttn']
        button.text = widget.text
"""

class Alkahmi(App):
    def build(self):
        return 

if __name__ == "__main__"    :

    Alkahmi().run()