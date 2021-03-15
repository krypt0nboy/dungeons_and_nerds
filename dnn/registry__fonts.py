"""This file updates the font registry.

"""
from kivy_boost.common import *
from settings.base import RESOURCES_PATH


@register_font_resource
class AlagardFont(FontResourceBase):

    @classmethod
    def base_path(cls):
        return RESOURCES_PATH

    @classmethod
    def path(cls):
        return 'fonts/alagard.ttf'

    @classmethod
    def name(cls):
        return 'alagard'


@register_font_resource
class AlkhemikalFont(FontResourceBase):

    @classmethod
    def base_path(cls):
        return RESOURCES_PATH

    @classmethod
    def path(cls):
        return 'fonts/Alkhemikal.ttf'

    @classmethod
    def name(cls):
        return 'Alkhemikal'


@register_font_resource
class GothicPixelsFont(FontResourceBase):

    @classmethod
    def base_path(cls):
        return RESOURCES_PATH

    @classmethod
    def path(cls):
        return 'fonts/GothicPixels.ttf'

    @classmethod
    def name(cls):
        return 'GothicPixels'


@register_font_resource
class OwreKyngeFont(FontResourceBase):

    @classmethod
    def base_path(cls):
        return RESOURCES_PATH

    @classmethod
    def path(cls):
        return 'fonts/OwreKynge.ttf'

    @classmethod
    def name(cls):
        return 'OwreKynge'
