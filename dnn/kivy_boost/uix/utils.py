"""This file provides with uix related utility functions.

"""
import os

from kivy_boost.common import resources_registry


def load_font_by_name(name=None, resources_path=None):
    """
    Allows to load a font resource by name.
    :param name: The resource to load.
    :param resources_path: The resources path to use.
    :return: The path of the font
    """
    if name in resources_registry['fonts'].keys():
        return os.path.join(resources_path, resources_registry['fonts'][name].path())


def load_graphic_by_name(name=None, resources_path=None):
    """
    Allows to load a graphic resource by name.
    :param name: The resource to load.
    :param resources_path: The resources path to use.
    :return: The path of the font
    """
    if name in resources_registry['fonts'].keys():
        return os.path.join(resources_path, resources_registry['graphics'][name].path())
