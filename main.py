from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

from random import *

Window.size = (1280, 720)    # (Width, Height)

class Main(FloatLayout):

    # Once The 8 Players are all inserted and Tournament Begins
    Players_Locked = False
    Winners_Locked = False
    Finalists_Locked = False

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

    # 
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

    def Check_Lockable(self,String,widget):

        Players = [ None, 'Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8',]
        Winners = [ None, 'Winner 1', 'Winner 2', 'Winner 3', 'Winner 4']
        Finalists = [ None, None, None, None, None, 'Finalist 1', 'Finalist 2' ]


        P = []
        W = []

        for i in range(1,9):

            P.append(self.ids[Players[i]])

        for i in range(1,5):

            W.append(self.ids[Winners[i]])



        RollCall = 0
        for i in range(8):

            if P[i].text != Players[i + 1]:
                RollCall += 1
                print(f' Players: {RollCall}/8')

            if RollCall == 8:
                self.Players_Locked = True
                print(f' All Player Names Have Been Entered! ')

        RollCall = 0 
        for i in range(4):

            if W[i].text != Winners[i + 1]:
                RollCall +=1
                print(f' Winners: {RollCall}/4')

            if RollCall == 4:
                self.Winners_Locked = True
                print(f' First 4 Winners Are Now Locked! ')

        

    def Lock_Winners(self,widget):

        b1 = Button(text='Claire')

    def Shuffle_Players(self,widget):
        # Quite Simple, Will only work if Players_Locked = True

        Players = [ None, 'Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8',]
       
        P = []

        for i in range(1,9):

            P.append(self.ids[Players[i]])


        if self.Players_Locked == True and self.Winners_Locked == False:

            Cache = []
            while len(Cache) != 8:
                for i in range(8):
                    RNG = randint(0,7)
                    if P[RNG] not in Cache:
                        Cache.append(P[RNG].text)

            while len(Cache) > 0:
                for i in range(8):
                    RNG = randint(0,len(Cache) -1)
                    if Cache[RNG] != P[i].text:
                        P[i].text == Cache[RNG]
                        del Cache[RNG]

    def Advance_Player(self,widget,string):
        
        Winner = [ None, 'Winner 1', 'Winner 2', 'Winner 3', 'Winner 4']
        Finalists = [ None, None, None, None, None, 'Finalist 1', 'Finalist 2' ]

        if int(string) < 5 and self.Players_Locked == True:
            W = self.ids[Winner[int(string)]]
            W.text = widget.text
            W.color = widget.color
            print(f' Winner {string }: {widget.text}')

        elif int(string) > 4 and self.Winners_Locked == True:
            if int(string) < 7:
                F = self.ids[Finalists[int(string)]]
                F.text = widget.text
                F.color = widget.color
                print(f' Finalist {string }: {widget.text}')

        if int(string) > 6:
            C = self.ids['Champion']
            C.text = widget.text
            C.color = widget.color

        String = string
        self.Check_Lockable(String,widget)

    # This Function needs to run through the bracket in an order
    # Locking each segment finished
    # Unoccupied Buttons are also Locked

    def DEV_FILL_PLAYERS(self,widget):
        
        
        DEV0 = self.ids['Champion']
        Players = [ None, 'Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8',]
       
        P = []

        for i in range(1,9):

            P.append(self.ids[Players[i]])  
            P[i-1]
        

class Alkahmi(App):
    def build(self):
        return 

if __name__ == "__main__"    :

    Alkahmi().run()