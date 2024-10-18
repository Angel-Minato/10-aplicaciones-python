from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob, random
from hoverable import HoverBehavior
from datetime import datetime
from pathlib import Path

Builder.load_file('desing.kv')

class LoginScreen(Screen):
    def sing_up(self):
        self.manager.current = "Sign_up_screen"

    def login(self,unam, poda):
        with open ("user.json") as file:
            users = json.load(file)
        if unam in users and users[unam]['password'] == poda:
            self.manager.current = "Login_Screen_success"
        else:
            self.manager.login_wong.text= 'esta mal'

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,unesco, poda):
        print(unesco,poda)
        with open("user.json") as file:
            users = json.load(file)
            print(users)
        users[unesco] = {'username': unesco, 'password':poda,
            'created': datetime.now().strftime("%Y-%m-%d, %H:%M:%S")} 
        self.manager.current ="sign_up_screen_success"

class SingUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction ="right"
        self.manager.current ="login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction ="right"
        self.manager.current ="login_screen"

    def get_camote(self, feel):
        feel = feel.lower()
        avidable = glob.glob("textos/*txt")
        avidable= [Path(filema)for filema in avidable]
        if feel in avidable:
            with open(f"textos/{feel}.txt") as file:
                camotes = file.readlines()
            self.ids.camotes.text = random.choice(camotes)
        else:
            self.ids.camotes.text = "esa opcion no esxite gracias"

class ImagenB(HoverBehavior,Image,ButtonBehavior):
    pass
    

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__" :
    MainApp().run()   
