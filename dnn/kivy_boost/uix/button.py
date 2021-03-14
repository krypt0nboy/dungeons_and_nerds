from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

from kivy_boost.audio.utils import *

from settings.base import RESOURCES_PATH


class InteractiveButton(Button):
    """
    """
    base_text_color = ObjectProperty()
    hover_text_color = ObjectProperty()
    base_text = StringProperty()
    press_sound = StringProperty()
    sound = ObjectProperty()

    def __init__(self, **kwargs):
        super(InteractiveButton, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *largs):
        pos = self.to_widget(*largs[1])
        if self.collide_point(*pos):
            self.color = self.hover_text_color
        else:
            self.color = self.base_text_color

    def on_press(self):
        if not self.sound:
            if self.press_sound:
                self.sound = load_sound_by_name(resources_path=RESOURCES_PATH, name=self.press_sound)
                self.sound.volume = 1
        if self.sound:
            self.sound.play()


class MenuButton(Button):
    """
    """

    screen = ObjectProperty()
