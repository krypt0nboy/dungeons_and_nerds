"""
Provides with images related classes and functions.
"""
import os
from kivy.uix.image import Image
from kivy_boost.common import KivyBoostCommon
from kivy.properties import StringProperty


class Image_(Image, KivyBoostCommon):
    """

    """
    resource = StringProperty()

    def __init__(self, **kwargs):
        super(Image_, self).__init__(**kwargs)
        self.source = os.path.join("../../resources/imgs/", self.resource)
