"""This file updates the audio registry.

"""
import os

from kivy_boost.common import *


@register_audio_resource
class HopeNotLostAudio(AudioResourceBase):

    @classmethod
    def path(cls):
        return 'sounds/jim_hall_hope_not_lost.mp3'

    @classmethod
    def name(cls):
        return 'jim_hall_hope_not_lost'


@register_audio_resource
class LastBreathAudio(AudioResourceBase):

    @classmethod
    def path(cls):
        return 'sounds/jim_hall_last_breath.mp3'

    @classmethod
    def name(cls):
        return 'jim_hall_last_breath'


@register_audio_resource
class MetalSwooshAudio(AudioResourceBase):

    @classmethod
    def path(cls):
        return 'sounds/mixkit_metal_hit_woosh_1485.wav'

    @classmethod
    def name(cls):
        return 'mixkit_metal_hit_woosh_1485'


@register_audio_resource
class MonsterEvilVoice1(AudioResourceBase):

    @classmethod
    def path(cls):
        return 'sounds/mixkit-monster-evil-voice-290.wav'

    @classmethod
    def name(cls):
        return 'monster_evil_voice_1'


@register_audio_resource
class MonsterScreech1(AudioResourceBase):

    @classmethod
    def path(cls):
        return 'sounds/mixkit-creature-long-screech-307.wav'

    @classmethod
    def name(cls):
        return 'monster_screech_1'
