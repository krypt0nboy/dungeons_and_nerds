from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label

from kivy_boost.audio.utils import *


class HoverLabel(Label):
    """
    A label that changes color or texture when hovered on.
    """
    base_color = ObjectProperty()
    hover_color = ObjectProperty()
    base_text = StringProperty()
    hover_sound = StringProperty()
    sound = ObjectProperty()

    def __init__(self, **kwargs):
        super(HoverLabel, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *largs):
        pos = self.to_widget(*largs[1])
        if self.collide_point(*pos):
            self.color = self.hover_color
        else:
            self.color = self.base_color

    def on_touch_down(self, touch):
        if not self.sound:
            if self.hover_sound:
                self.sound = load_sound_by_name(name=self.hover_sound)
                self.sound.volume = 1
        if self.sound:
            self.sound.play()


class FadingLabel(Label):
    """
    A self fading label.
    """

    def __init__(self, **kwargs):
        super(FadingLabel, self).__init__(**kwargs)
        self.animate()

    def animate(self):
        anim = Animation(opacity=0, duration=10)
        anim.start(self)
