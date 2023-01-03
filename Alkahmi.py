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

    # An Integer to keep track of what we're currently changing
    Editing = 0

    # A List of id's set in kv file that we can easily Access as Numbers with Variable Above
    EditList = ['Tournament Title', 'P1', 'P2', 'P3', 'P4', 'P4', 'P5', 'P6', 'P7', 'P8']

    # Switch Between Fields we can Edit
    def Switch_Edit(self,widget, Direction):

        
        CurrentEdit = self.ids['edit']
        CurrentEdit.text = self.EditList[self.Editing]

        Type_Text = self.ids['txtinp']
        Type_Text.text = self.EditList[self.Editing]

        if Direction == 'right':

            if self.Editing < len(self.EditList) - 1:
                
                self.Editing += 1
        
        if Direction =='left':

            if self.Editing > 0:

                self.Editing -= 1

        
    def validate(self,widget):

        # We set which ever id is currently active via EditList[Editing]
        Set_As = self.ids[self.EditList[self.Editing]]
        Set_As.text = widget.text



class Alkahmi(App):
    def build(self):
        return 

if __name__ == "__main__"    :

    Alkahmi().run()