from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import *

from kivy_boost.common import KivyBoostCommon


class ScreenManager_(KivyBoostCommon, ScreenManager):
    """
    """
    pass


class Screen_(KivyBoostCommon, Screen):
    """
    """

    screen_audio = StringProperty()
