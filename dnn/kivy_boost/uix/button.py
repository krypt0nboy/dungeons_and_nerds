from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty

from kivy_boost.audio.utils import *
from kivy_boost.uix.screens import *


class BoostedButton(Button):
    """
    BoostedButton offers handy features such as hovering.
    """

    # The normal state text color
    base_text_color = ObjectProperty()
    # The text color when hovering the button
    hover_text_color = ObjectProperty()
    # The normal state text
    base_text = StringProperty()
    # The altered text when hovering the button
    hover_text = StringProperty()
    # The sound resource to play when hovering the button
    press_sound = StringProperty()
    # The loaded sound resource to play when hovering the button
    sound = ObjectProperty()

    def __init__(self, **kwargs):
        super(BoostedButton, self).__init__(**kwargs)
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
                self.sound = load_sound_by_name(name=self.press_sound)
                self.sound.volume = 1
        if self.sound:
            self.sound.play()


class MenuButton(Button):
    """
    """

    # The menu to which the button is attached
    menu = ObjectProperty()
    # The target screen to switch to when clicking the button
    target_screen = ObjectProperty()
    # The warning popup allows to display a warning in case a screen is unavailable
    warning_popup = ObjectProperty()

    def __init__(self, **kwargs):
        super(MenuButton, self).__init__(**kwargs)

    def on_press(self):
        self.switch_to_target_screen()

    def switch_to_target_screen(self):
        if self.target_screen:
            if isinstance(self.target_screen, LockableScreen):
                is_available, controls = self.target_screen.is_available()
                if not is_available:
                    warning_popup.warn(controls)
                else:
                    m = 'screen_switch' + self.target_screen
                    getattr(self.parent.parent.manager, m)(0)


class BoostedMenuButton(BoostedButton, MenuButton):
    """
    """

    def on_press(self):
        super(BoostedButton, self).on_press()
        super(MenuButton, self).on_press()
