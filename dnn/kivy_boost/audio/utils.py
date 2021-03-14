"""This file provides with audio related utility functions.

"""
import os

from kivy.core.audio import SoundLoader
from kivy_boost.common import resources_registry


def load_sound_by_name(name=None, resources_path=None):
    """
    Allows to load a sound resource by name.
    :param name: The resource to load.
    :param resources_path: The resources path to use.
    :return: The sound
    """
    if name in resources_registry['audio'].keys():
        sound = SoundLoader.load(os.path.join(resources_path, resources_registry['audio'][name].path()))

        return sound


def play_sound_by_name(name=None, resources_path=None, loop=False, volume=None):
    """
    :param name:
    :param resources_path:
    :param loop:
    :param volume:
    :return:
    """
    sound = load_sound_by_name(resources_path=resources_path, name=name)
    if sound:
        sound.play()
        sound.loop = loop
        sound.volume = volume
    return sound
