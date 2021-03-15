from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import *

from kivy_boost.common import KivyBoostCommon


class BoostedScreenManager(KivyBoostCommon, ScreenManager):
    """
    """

    # def __init__(self, **kwargs):
    #     super(BoostedScreenManager, self).__init__(**kwargs)

    def switch_screen(self, name=None):
        if name in [screen.name for screen in self.screens]:
            self.current = name


class BoostedScreen(KivyBoostCommon, Screen):
    """
    """

    screen_audio_track = StringProperty()

    # def __init__(self, **kwargs):
    #     super(BoostedScreen, self).__init__(**kwargs)


class MenuScreen(BoostedScreen):
    """
    """

    # A list of the MenuButtons attached to the menu
    buttons = ListProperty()

    # def __init__(self, **kwargs):
    #     super(MenuScreen, self).__init__(**kwargs)


class LockableScreen(BoostedScreen):
    """
    """

    # A callback that allows to determine if the target screen should be available
    is_available_callbacks = ObjectProperty()

    def is_available(self, **kwargs):
        """
        Evaluates if the screen is available.
        :param kwargs:
        :return: A dictionary containing .
        :rtype: dict
        """
        is_available_controls = [cb(**kwargs) for cb in self.is_available_callbacks]
        is_available_controls.append(self._is_available(**kwargs))
        return is_available_controls

    # noinspection PyMethodMayBeStatic
    def _is_available(self, **kwargs):
        """
        Rather than providing a series of control callbacks, this method may be overwritten to evaluate if the screen
        is available.
        :param kwargs:
        :return: A boolean indicating if the screen is available.
        :rtype: bool
        """
        return True
