"""This file provides with a boosted App class.

"""
from kivy.app import App
from kivy.properties import *


class BoostedApp(App):
    """
    """

    def __init__(self, version=None, main_theme_song=None, main_theme_song__loaded=None, **kwargs):
        super(BoostedApp, self).__init__(**kwargs)
        self.version = version
        self.main_theme_song = main_theme_song
        self.main_theme_song__loaded = main_theme_song__loaded
