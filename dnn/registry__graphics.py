"""This file provides with graphic resources.

"""
from kivy_boost.common import *
from settings.base import RESOURCES_PATH


@register_graphic_resource
class LogoTheTribeWhitePNG(GraphicResourceBase):

    @classmethod
    def base_path(cls):
        return RESOURCES_PATH

    @classmethod
    def path(cls):
        return 'imgs/logo-the-tribe-white.png'

    @classmethod
    def name(cls):
        return 'logo-the-tribe-white'
