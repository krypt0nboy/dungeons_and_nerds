# coding: utf-8
"""

"""
import os
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy_boost.uix.views import *
from kivy_boost.uix.boxlayout import FileBrowserDialog


class PathField(TextInput):
    """
    Stores a path.
    """
    # The field's value
    path = StringProperty()
    # The field's info window
    info_window = ObjectProperty()
    # The browse button associated with the field
    browse_button = ObjectProperty()
    # The browser
    browser = ObjectProperty()
    # Whether the path is a directory or not.
    isdir = BooleanProperty
    # RGX Input
    rgx_input = ObjectProperty()

    def __init__(self, **kwargs):
        super(PathField, self).__init__(**kwargs)
        self.bind(text=self.on_text)

    def dismiss_browser(self):
        """
        :return:
        """
        self.browser.dismiss()

    def open_browser(self):
        """

        :return:
        """
        self.init_popup()
        self.browser.open()

    def init_popup(self):
        """
        :return:
        """
        content = FileBrowserDialog(cancel=self.dismiss_browser, path_field=self)
        self.browser = Popup(title="Choose file", content=content, size_hint=(0.9, 0.9))

    def on_text(self, instance, value):
        """
        :param instance:
        :param value:
        :return:
        """
        self.isdir = os.path.isdir(value)
        if self.rgx_input is not None:
            if self.isdir:
                self.rgx_input.disabled = False
            else:
                self.rgx_input.disabled = True


class TablePathField(PathField):
    """

    """
    table = ObjectProperty()

    def on_text(self, instance, value):
        self.isdir = os.path.isdir(value)
        if not self.isdir and os.path.exists(value):
            self.table.update(value)


# Factory.register('PathField', cls=PathField)
# Factory.register('TablePathField', cls=TablePathField)
