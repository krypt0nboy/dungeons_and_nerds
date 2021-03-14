from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy_boost.audio.utils import *
from settings.base import RESOURCES_PATH


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
            # self.text = "> %s <" % self.base_text
        else:
            self.color = self.base_color
            # self.text = self.base_text

            # sound = load_sound_by_name(resources_path=RESOURCES_PATH, name='mixkit_metal_hit_woosh_1485')
            # if sound:
            #     sound.play()
            #     sound.loop = True

    def on_touch_down(self, touch):
        if not self.sound:
            if self.hover_sound:
                self.sound = load_sound_by_name(resources_path=RESOURCES_PATH, name=self.hover_sound)
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
