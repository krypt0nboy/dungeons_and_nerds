from kivy.properties import *
from kivy.animation import Animation
from kivy.uix.anchorlayout import AnchorLayout


class IntroAnchorLayout(AnchorLayout):
    """
    """

    fade_duration = NumericProperty(defaultvalue=0.5)

    def __init__(self, **kwargs):
        super(IntroAnchorLayout, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        anim = Animation(opacity=0, duration=self.fade_duration)
        anim.start(self)


class FadingAnchorLayout(AnchorLayout):
    """
    """

    def __init__(self, **kwargs):
        super(FadingAnchorLayout, self).__init__(**kwargs)
        self.animate()

    def animate(self):
        anim = Animation(opacity=0, duration=10)
        anim.start(self)
