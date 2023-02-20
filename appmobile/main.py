import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kivy.require('2.1.0')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init()

class DavidApp(App):
    def buils(self):
        return GameView()
    
davidApp = DavidApp()
davidApp.run()