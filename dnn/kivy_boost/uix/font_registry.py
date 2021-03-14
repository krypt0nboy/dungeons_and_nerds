"""This file updates the font registry.

"""
from kivy_boost.common import *


@register_font_resource
class AlagardFont(FontResourceBase):

    @classmethod
    def path(cls):
        return 'fonts/alagard.ttf'

    @classmethod
    def name(cls):
        return 'alagard'
