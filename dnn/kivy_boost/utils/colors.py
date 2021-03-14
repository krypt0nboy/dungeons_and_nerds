"""
Provides with color related functions and classes.
"""
from kivy_boost.uix.colors import RGB


def translate_rgb(rgb):
    """
    Translates a RGB color into a kivy RGB equivalent.
    :param rgb: A list of red, green, blue.
    :return: A list of rgb.
    :rtype: list
    """
    return map(lambda v: round(float(v) / float(255), 3), rgb)


def translate_color(name):
    """
    Translate a human readable color to a RGB one.
    :param name: The color's name.
    :return: The color as RGB list.
    :rtype: list
    """
    return RGB[name]
