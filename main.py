import kivy
kivy.require('1.0.6')

from glob import glob
from random import randint
from os.path import join, dirname


#@title Default title text
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.image import Image 
from kivy.uix.label import Label
import time

Config.set("graphics","width","1400")
Config.set("graphics","height","800")
Config.set('graphics', 'resizable', True)

class MyApp(App):
    def build(self):
        self.first = [12,10]
        self.second = [13,10]
        self.sm = ScreenManager()
        screen = Screen(name = "select_character")
        self.helth_1 = 3
        self.helth_2 = 3
        self.helth_1_label = Label(text = "1 health: " + str(self.helth_1), pos = (0,0),size = (200,100))
        self.helth_2_label = Label(text = "2 health: " + str(self.helth_2), pos = (1300,0),size = (200,100))
        self.hod = 0
        self.oh = 0
        self.prep = [[13,12],[13,13],[13,14],[2,7],[11,20],[13,5],[14,16],[10,16],[12,7],[9,8],[11,5],[8,7],[12,12],[7,6],[7,7],[7,8],[8,9],[9,8],[4,7],[14,6],[12,14],[6,9]]
        self.title = ""
        f = Widget()
        self.i = 0
        button = GridLayout(cols=30)
        button.size = (1500,750)
        self.button = [0 for _ in range(450)]
        self.a = list()
        for y in range(15):
            self.a.append(list())
            for x in range (30):
                if([y,x] in self.prep):
                    self.a[y].append(str(y * 30 + x) + "g")
                else:
                    self.a[y].append(str(y * 30 + x))
        self.mas = list()
        for i in range(450):
            t = True
            for j in self.prep:
                if(int(i / 30) == j[0] and int(i % 30) == j[1]):
                    print(1)
                    self.mas.append(Button(text='',on_press=self.callback_press, id=str(i), background_color = [0.0,2.0,0,1.0]))
                    t = False
                    break
            if(t):
                self.mas.append(Button(text='',on_press=self.callback_press, id=str(i), background_color = [1.0,0.0,0,1.0]))
            button.add_widget(self.mas[i])
        self.a[12][10] = "370r"
        self.a[13][10] = "400b"
        self.img = Image(source ='1.jpg')
        self.img.size = (50,50)
        self.img.pos = (10 * 50, 2 * 50)
        self.img2 = Image(source ='2.jpg')
        self.img2.size = (50,50)
        self.img2.pos = (10 * 50, 1 * 50)
        self.img_win_1 = Image(source ='3.png')
        self.img_win_1.size = (1200,600)

        self.img_win_1.pos = (1212,1313)
        self.img_win_2 = Image(source ='4.png')
        self.img_win_2.size = (1200,600)
        self.img_win_2.pos = (1212,1313)
        f.add_widget(button)
        f.add_widget(self.img)
        f.add_widget(self.img2)
        f.add_widget(self.img_win_1)
        f.add_widget(self.img_win_2)
        f.add_widget(self.helth_1_label)
        f.add_widget(self.helth_2_label)
        f.add_widget(screen)
        return f

    def callback_press(self, instance):
        print(instance.id)
        if(self.hod == 0 and self.oh < 3):
            self.oh += 1
            b = 0
            z = 0
            k = 0
            for y in range(15):
                for x in range (30):
                    if self.a[y][x] == str(y * 30 + x) + 'r':
                        k = y*30+x
                        b = x
                        z = y
            if(int(instance.id) == k + 1 or int(instance.id) == k-1 or int(instance.id) == k+30 or int(instance.id) == k-30):
                for y in range(15):
                    for x in range (30):
                        if str(self.a[y][x]) == str(instance.id):
                            self.a[y][x] = str(instance.id) + 'r'
                            self.a[z][b] = str(k)

                            self.img.pos = (x * 50,(14 - y) * 50)
                            self.first = [y,x]
                            print("Саня ты где")
                            break

            else:
                for i in self.prep:
                    if((self.first[0] - int(int(instance.id) / 30))*i[1] + (int(int(instance.id) % 10) - self.first[1])* i[0] + (self.first[1] * int(int(instance.id) / 30) - int(int(instance.id) % 10) * self.first[0]) == 0):
                        print(1)
                        return 0    
                for y in range(15):
                    for x in range (30):
                        if(self.a[y][x] == str(instance.id) + 'b'):
                            self.helth_2 -= 1
                            self.helth_2_label.text = "2 health: " + str(self.helth_2)
                print("Ложись")

        if(self.hod == 1 and self.oh < 3):
            self.oh += 1
            b = 0
            z = 0
            k = 0
            for y in range(15):
                for x in range (30):
                    if self.a[y][x] == str(y * 30 + x) + 'b':
                        k = y*30+x
                        b = x
                        z = y
            if(int(instance.id) == k + 1 or int(instance.id) == k-1 or int(instance.id) == k+30 or int(instance.id) == k-30):
                for y in range(15):
                    for x in range (30):
                        if str(self.a[y][x]) == str(instance.id):
                            self.a[y][x] = str(instance.id) + 'b'
                            self.a[z][b] = str(k)
                            self.img2.pos = (x * 50,(14 - y) * 50)
                            self.second = [y,x]
                            print("Саня ты где")
                            break

            elif(self.a[int(int(instance.id) / 30)][int(int(instance.id) % 30)][0:-1] != "g"):
                for y in range(15):
                    for x in range (30):
                        if(self.a[y][x] == str(instance.id) + 'r'):
                            self.helth_1 -= 1
                            self.helth_1_label.text = "1 health: " + str(self.helth_1)

                print("Ложись")
        if(self.oh == 3):
            self.hod = (self.hod + 1) % 2 
            self.oh = 0
        if(self.helth_1 == 0):
            self.img_win_2.pos = (0,0)
            self.hod = 3
        if(self.helth_2 == 0):
            self.img_win_1.pos = (0,0)
            self.hod = 3


if __name__ == '__main__':
    MyApp().run()