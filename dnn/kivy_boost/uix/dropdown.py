"""
Provides with custom DrowDown classes.
"""
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import (
    ObjectProperty,
    StringProperty
)


class DropDownOption(Button):
    """
    """
    value = StringProperty()

    def dropdown(self):
        return self.root


class DropDownList(DropDown):
    """

    """
    main_button = ObjectProperty()

    def add_option(self, label=None, value=None):
        pass
