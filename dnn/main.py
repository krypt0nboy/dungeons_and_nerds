# coding: utf-8
"""
App's main file.
"""
import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock

from kivy_boost.uix.table import *
from kivy_boost.uix.button import *
from kivy_boost.uix.views import *
from kivy_boost.uix.layouts import *
from kivy_boost.uix.label import *
from kivy_boost.common import *
from kivy_boost.app import BoostedApp
from kivy_boost.audio.utils import *
from kivy_boost.uix.popup import WarningPopup
from kivy_boost.uix.screens import *

from registry__audio import *
from registry__fonts import *
from registry__graphics import *

kivy.require("2.0.0")
# Config.set('graphics', 'width', '1400')
# Config.set('graphics', 'height', '900')
# Config.set('graphics', 'resizable', 1)
# Config.write()

INTRO = """
You and your two friends Charles and Aurel were playing Dungeons and Dragons,
like a bunch of nerds that you are, 
when suddenly, you, the dungeon master, unwittingly summoned a demon,
by pronouncing magic words from an old grimoire you thought were a fake.
The demon has trapped and sent you and your two friends into 
a magic realm, the dark lands of DeepWoods.

For you and your friends to go home, you must compete in a deadly tournament.
You will eventually have to defeat Lazarus Thornheart, 
an evil and wicked Sorcerer that seeks a passage to your world.

Next time you see an old and evil looking book,
leave it alone you idiot !

Click anywhere to log in and start.
"""


class HCStudiosScreen(Screen):
    pass


class TheTribeIOScreen(Screen):
    pass


class DNNLogoScreen(Screen):
    pass


class DNNIntroScreen(Screen):
    intro = StringProperty()

    def __init__(self, **kwargs):
        super(DNNIntroScreen, self).__init__(**kwargs)
        self.intro = INTRO


class DNNMenuScreen(Screen):
    pass


class DnnScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(DnnScreenManager, self).__init__(transition=FadeTransition(), **kwargs)
        Clock.schedule_once(self.screen_switch_dnn_menu_screen_, 3)

    def screen_switch_hc_studio_screen_(self, dt):
        self.current = '_hc_studio_screen_'
        Clock.schedule_once(self.screen_switch_the_tribe_io_screen_, 4)

    def screen_switch_the_tribe_io_screen_(self, dt):
        self.current = '_the_tribe_io_screen_'
        Clock.schedule_once(self.screen_switch_dnn_logo_screen_, 4)

    def screen_switch_dnn_logo_screen_(self, dt):
        self.current = '_dnn_logo_screen_'
        Clock.schedule_once(self.screen_switch_dnn_menu_screen_, 4)

    def screen_switch_dnn_intro_screen_(self, dt):
        self.current = '_dnn_intro_screen_'
        sound = load_sound_by_name(name='intro')
        if sound:
            sound.play()
            sound.volume = 1
        Clock.schedule_once(self.screen_switch_dnn_menu_screen_, 46)

    def screen_switch_dnn_menu_screen_(self, dt):
        self.current = '_dnn_menu_screen_'


class DNNApp(App):

    def build(self):
        return DnnScreenManager()

    def run(self, **kwargs):
        sound = load_sound_by_name(name='jim_hall_hope_not_lost')
        if sound:
            sound.play()
            sound.volume = 0.05
            sound.loop = True

        super(DNNApp, self).run()


if __name__ == "__main__":
    DNNApp().run()
