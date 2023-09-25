import random
from kivy.config import Config
from kivy.metrics import dp

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy import platform
from kivy.core.window import Window
from  kivy.app import App
from kivy.graphics import Color, Line, Quad, Triangle
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty
from kivy.uix.widget import Widget
import mysql.connector as mycon
conobj= mycon.connect(host="localhost",user="root",password="kartik1909", database = 'data')
curobj=conobj.cursor()
Builder.load_file("menu.kv")
lst_of_user = []
class ScreenManagement (ScreenManager):
    def __init__(self,**kwargs):
        super(ScreenManagement,self).__init__(**kwargs)

class MainWindow(Screen):
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        self.name='main'
        layout = FloatLayout()
        self.add_widget(layout)
        self.add_widget(Label(text = 'I  N  T  E  R  S  P  A  C  E', font_size =dp(50), pos_hint = {"x": 0.01,  "top": 1.2}, bold=True, font_name = 'fonts/Sackers-Gothic-Std-Light.ttf'))
        self.btn = Button(text='Login', bold=True,size_hint=(0.5, 0.07), pos_hint={'x': 0.25, 'y': 0.35},background_color =( 1, .3, .4, 1), background_normal= '', font_name= 'fonts/Eurostile.ttf')
        self.btn2 = Button(text='Register', bold=True, size_hint=(0.5, 0.07), pos_hint={'x': 0.25, 'y': 0.25}, background_color =( 1, .3, .4, 1), background_normal= '', font_name= 'fonts/Eurostile.ttf')
        self.add_widget(self.btn)
        self.add_widget(self.btn2)
        self.btn.bind(on_press=self.screen_transition1)
        self.btn2.bind(on_press=self.screen_transition2)

    def screen_transition1(self, *args):
        self.manager.current = 'login'

    def screen_transition2(self, *args):
        self.manager.current = 'register'

class RegisterWindow(Screen):
    def __init__(self,**kwargs):
        super(RegisterWindow,self).__init__(**kwargs)
        self.name='register'
        layout = RelativeLayout()
        self.add_widget(layout)
        self.add_widget(Label(text = 'I  N  T  E  R  S  P  A  C  E', font_size =dp(50), pos_hint = {"x": 0.01,  "top": 1.2}, bold=True, font_name = 'fonts/Sackers-Gothic-Std-Light.ttf'))
        self.add_widget(Label(text='Username', size_hint=(.45, .07), pos_hint={'x': .05, 'y': .5}, font_name= 'fonts/Eurostile.ttf'))
        self.username = TextInput(multiline=False, size_hint=(.4, .07), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.username)
        self.add_widget(Label(text='Password', size_hint=(.45, .07), pos_hint={'x': .05, 'y': .4}, font_name= 'fonts/Eurostile.ttf'))
        self.password = TextInput(multiline=False, password=True, size_hint=(.4, .07), pos_hint={'x': .5, 'y': .4})
        self.add_widget(self.password)
        self.add_widget(Label(text='Confirm Password',size_hint=(.45,.07),pos_hint={'x':.05,'y':.3}, font_name= 'fonts/Eurostile.ttf'))
        self.conpass= TextInput(multiline=False,password=True,size_hint=(.4,.07),pos_hint={'x':.5,'y':.3})
        self.add_widget(self.conpass)
        self.btn = Button(text='Register', size_hint=(.4, .07), pos_hint={'center_x': .5, 'y': .2},
                          background_color=( 1, .3, .4, 1), background_normal= '', bold=True, font_name= 'fonts/Eurostile.ttf')
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.submit)
        self.back = Button(text='Back', size_hint=(.1, .07), pos_hint={'center_x': 0.1, 'y': 0.9},
                          background_color=( 1, .3, .4, 1), background_normal= '',  bold=True, font_name= 'fonts/Eurostile.ttf')
        self.add_widget(self.back)
        self.back.bind(on_press=self.prev_pg)

    def prev_pg(self, *args):
        self.manager.current = "main"

    def submit(self, instance):
        username1= self.username.text
        password2 = self.password.text
        conpass = self.conpass.text
        if password2==conpass:
            cmd="INSERT INTO game_data VALUES('{}','{}', {})".format(username1,password2, 0)
            curobj.execute(cmd)
            conobj.commit()
            self.manager.current = 'login'
class LoginWindow(Screen):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.name='login'
        layout=FloatLayout(size=(500,500))
        self.add_widget(layout)
        self.add_widget(Label(text = 'I  N  T  E  R  S  P  A  C  E', font_size =dp(50), pos_hint = {"x": 0.01,  "top": 1.2}, bold=True, font_name = 'fonts/Sackers-Gothic-Std-Light.ttf'))

        self.add_widget(Label(text='Please fill the following to Login', bold=True,pos_hint={'x':.26,'y':.5},size_hint=(.45,.09), font_name= 'fonts/Eurostile.ttf'))
        self.user= TextInput(text='Username', multiline=False, size_hint=(.6,.07),pos_hint={'x':.2,'y':.4})
        self.add_widget(self.user)
        self.passw= TextInput(text='Password', multiline=False, size_hint=(.6,.07),pos_hint={'x':.2,'y':.3}, password=True)
        self.add_widget(self.passw)
        self.btn=Button(text='Login',bold=True,size_hint=(.6,.07),pos_hint={'x':.2,'y':.15}, background_color=(1, .3, .4, 1), background_normal='')
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.screen_transition)
        self.back = Button(text='Back', size_hint=(.1, .07), pos_hint={'center_x': 0.1, 'y': 0.9},
                           background_color=(1, .3, .4, 1), background_normal='', bold=True, font_name= 'fonts/Eurostile.ttf')
        self.add_widget(self.back)
        self.back.bind(on_press=self.prev_pg)

    def prev_pg(self, *args):
        self.manager.current = "main"
    def screen_transition (self,*args):

        user= self.user.text
        global lst_of_user
        lst_of_user.append(user)
        print(lst_of_user)
        passw= self.passw.text
        cmd="SELECT username,password FROM game_data WHERE username = '{}'".format(user)
        curobj.execute(cmd)
        fetch= curobj.fetchone()
        print(fetch)
        if fetch==None:
            self.add_widget(Label(text='*Incorrect Username or Password*', pos_hint={'x': 0, 'y': -.24},bold=True))
        elif passw==fetch[1]:
            self.manager.current = "game"
        else:
            self.add_widget(Label(text='*Incorrect Username or Password*',pos_hint={'x':0,'y':-.24},bold=True))
class Tutorial(Screen):
    tut_text = StringProperty('''1. Tap the screen to move the ship. Tap left to move the ship left and similarly right, to move the ship to the right.
    
2. Keep the ship steadily moving on the white illuminated path.

3. If the ship crosses the boundaries of the path, the game ends after which you must restart.


Happy Playing!''')
    def __init__(self, **kwargs):
        super(Tutorial, self).__init__(**kwargs)
        self.name='tutorial'
        self.back = Button(text='Back', size_hint=(.1, .07), pos_hint={'center_x': 0.1, 'y': 0.9},
                           background_color=(1, .3, .4, 1), background_normal='', bold=True,
                           font_name='fonts/Eurostile.ttf')
        self.add_widget(self.back)
        self.back.bind(on_press=self.prev_pg)

    def prev_pg(self, *args):
        self.manager.current = "game"

class MainWidget(Screen,RelativeLayout):
    from transforms import transform, transform_2d, transform_perspective
    from user_actions import  on_touch_down, on_touch_up, keyboard_closed
    menu_widget = ObjectProperty()
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    V_NB_LINES = 8
    V_LINES_SPACING = .4  # percentage in screen width
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = .1  # percentage in screen height
    horizontal_lines = []
    SPEED = .8
    current_offset_y = 0
    current_y_loop = 0

    SPEED_X = 3.0
    current_speed_x = 0
    current_offset_x = 0

    NB_TILES = 16
    tiles = []
    tiles_coordinates = []

    SHIP_WIDTH = .1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship = None
    ship_coordinates = [(0, 0), (0, 0), (0, 0)]

    state_game_over = False
    state_game_has_started =False

    menu_title = StringProperty("I  N  T  E  R  S  P  A  C  E")
    normal_txt = StringProperty('RESULTS')
    menu_title_button = StringProperty("START")
    score_txt = StringProperty()
    tutorial_button = StringProperty("How To Play")
    highscore = StringProperty()



    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()
        self.init_ship()
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()
        self.name = 'game'

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def reset_game(self):
        self.current_offset_y = 0
        self.current_y_loop = 0
        self.current_speed_x = 0
        self.current_offset_x = 0
        self.tiles_coordinates = []
        self.score_txt = "SCORE: " + str(self.current_y_loop)

        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()
        self.state_game_over = False

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()

    def update_ship(self):
        center_x = self.width / 2
        base_y = self.SHIP_BASE_Y * self.height
        ship_half_width = self.SHIP_WIDTH * self.width / 2
        ship_height = self.SHIP_HEIGHT * self.height
        # ....
        #    2
        #  1   3
        # self.transform
        self.ship_coordinates[0] = (center_x - ship_half_width, base_y)
        self.ship_coordinates[1] = (center_x, base_y + ship_height)
        self.ship_coordinates[2] = (center_x + ship_half_width, base_y)

        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2 = self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])

        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collision(self):
        for i in range(0, len(self.tiles_coordinates)):
            ti_x, ti_y = self.tiles_coordinates[i]
            if ti_y > self.current_y_loop + 1:
                return False
            if self.check_ship_collision_with_tile(ti_x, ti_y):
                return True
        return False

    def check_ship_collision_with_tile(self, ti_x, ti_y):
        xmin, ymin = self.get_tile_coordinates(ti_x, ti_y)
        xmax, ymax = self.get_tile_coordinates(ti_x + 1, ti_y + 1)
        for i in range(0, 3):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
                return True
        return False

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_TILES):
                self.tiles.append(Quad())

    def pre_fill_tiles_coordinates(self):
        for i in range(0, 10):
            self.tiles_coordinates.append((0, i))

    def generate_tiles_coordinates(self):
        last_x = 0
        last_y = 0

        # clean the coordinates that are out of the screen
        # ti_y < self.current_y_loop
        for i in range(len(self.tiles_coordinates) - 1, -1, -1):
            if self.tiles_coordinates[i][1] < self.current_y_loop:
                del self.tiles_coordinates[i]

        if len(self.tiles_coordinates) > 0:
            last_coordinates = self.tiles_coordinates[-1]
            last_x = last_coordinates[0]
            last_y = last_coordinates[1] + 1

        for i in range(len(self.tiles_coordinates), self.NB_TILES):
            r = random.randint(0, 2)
            # 0 -> straight
            # 1 -> right
            # 2 -> left
            start_index = -int(self.V_NB_LINES / 2) + 1
            end_index = start_index + self.V_NB_LINES - 1
            if last_x <= start_index:
                r = 1
            if last_x >= end_index:
                r = 2

            self.tiles_coordinates.append((last_x, last_y))
            if r == 1:
                last_x += 1
                self.tiles_coordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_coordinates.append((last_x, last_y))
            if r == 2:
                last_x -= 1
                self.tiles_coordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_coordinates.append((last_x, last_y))

            last_y += 1

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index - 0.5
        line_x = central_line_x + offset * spacing + self.current_offset_x
        return line_x

    def get_line_y_from_index(self, index):
        spacing_y = self.H_LINES_SPACING * self.height
        line_y = index * spacing_y - self.current_offset_y
        return line_y

    def get_tile_coordinates(self, ti_x, ti_y):
        ti_y = ti_y - self.current_y_loop
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile = self.tiles[i]
            tile_coordinates = self.tiles_coordinates[i]
            xmin, ymin = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_tile_coordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)

            #  2    3
            #
            #  1    4
            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)

            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def update_vertical_lines(self):
        # -1 0 1 2
        start_index = -int(self.V_NB_LINES / 2) + 1
        for i in range(start_index, start_index + self.V_NB_LINES):
            line_x = self.get_line_x_from_index(i)

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1
        end_index = start_index + self.V_NB_LINES - 1

        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        for i in range(0, self.H_NB_LINES):
            line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt):
        # print("dt: " + str(dt*60))
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.update_ship()

        if not self.state_game_over and self.state_game_has_started:
            speed_y = self.SPEED * self.height / 100
            self.current_offset_y += speed_y * time_factor


            spacing_y = self.H_LINES_SPACING * self.height
            while self.current_offset_y >= spacing_y:
                self.current_offset_y -= spacing_y
                self.current_y_loop += 1
                self.score_txt = "SCORE: " + str(self.current_y_loop)
                if int(self.current_y_loop)//10 == 0:
                    self.SPEED = self.SPEED + int(self.current_y_loop)//10
                self.generate_tiles_coordinates()
            speed_x = self.current_speed_x * self.width / 100
            self.current_offset_x += speed_x * time_factor
        if not self.check_ship_collision() and not self.state_game_over:
            cmd = "SELECT score FROM game_data WHERE username = '{}'".format(lst_of_user[0])
            curobj.execute(cmd)
            fetch = curobj.fetchone()
            if fetch[0] < int(self.current_y_loop):
                cmd1 = "UPDATE game_data SET score= {} WHERE username = '{}'".format(int(self.current_y_loop),lst_of_user[0])
                curobj.execute(cmd1)
                conobj.commit()
            cmd = "SELECT score FROM game_data WHERE username = '{}'".format(lst_of_user[0])
            curobj.execute(cmd)
            fetch1 = curobj.fetchone()
            self.highscore =str(lst_of_user[0])+ " High Score: " + str(fetch1[0])
            self.state_game_over = True
            self.menu_widget.opacity = 1
            self.menu_title = "G  A  M  E    O  V  E  R"
            self.menu_title_button = "RESTART"



    def on_menu_button_pressed(self):
        self.reset_game()
        self.state_game_has_started = True
        self.menu_widget.opacity =0
    def how_to_play(self):
        self.manager.current = "tutorial"
    def prev_pg(self, *args):
        global lst_of_user
        lst_of_user = []

        self.manager.current = "main"

class GalaxyApp(App):
    pass

GalaxyApp().run()
