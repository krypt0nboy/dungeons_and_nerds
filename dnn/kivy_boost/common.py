"""
Provides with common properties and attributes for kivy boost.
"""
import os

from kivy.app import App
from kivy.properties import ObjectProperty

from kivy_boost.exceptions import *

resources_registry = {}


def register_resource(registry=None, resource=None):
    """
    Allows to register a resource.
    :param registry: The registry
    :param resource: The resource to register.
    :return: The updated registry
    :rtype: dict
    """
    resources_registry.setdefault(registry, {})
    resources_registry[registry].setdefault(resource.name(), resource)


def register_audio_resource(resource=None):
    """
    Allows to register an audio resource.
    :param resource: The audio resource to register.
    :return: The updated registry.
    :rtype: dict
    """
    return register_resource(registry='audio', resource=resource)


def register_font_resource(resource=None):
    """
    Allows to register a font resource.
    :param resource: The resource to register.
    :return: The updated registry.
    :rtype: dict
    """
    return register_resource(registry='fonts', resource=resource)


def register_graphic_resource(resource=None):
    """
    Allows to register a graphic resource.
    :param resource: The resource to register.
    :return: The updated registry.
    :rtype: dict
    """
    return register_resource(registry='graphics', resource=resource)


def get_resource_full_path(registry=None, name=None):
    """
    Allows to get the full path of a registered resource.
    :param registry: The registry to query.
    :param name: The name of the resource.
    :return: The resource's full path as a string.
    :rtype: str
    """
    if registry in resources_registry.keys():
        if name in resources_registry[registry].keys():
            return resources_registry[registry][name].fullpath()
    else:
        raise ResourcesRegistryException("No such registry : %s" % registry)


def get_font_resource_full_path(name=None):
    """
    Allows to get the full path of a font registered resource.
    :param name: The name of the font resource.
    :return: The resource's full path as a string.
    :rtype: str
    """
    return get_resource_full_path(registry='fonts', name=name)


def get_audio_resource_full_path(name=None):
    """
    Allows to get the full path of an audio registered resource.
    :param name: The name of the audio resource.
    :return: The resource's full path as a string.
    :rtype: str
    """
    return get_resource_full_path(registry='audio', name=name)


def get_graphic_resource_full_path(name=None):
    """
    Allows to get the full path of a graphic registered resource.
    :param name: The name of the graphic resource.
    :return: The resource's full path as a string.
    :rtype: str
    """
    return get_resource_full_path(registry='graphics', name=name)


class KivyBoostCommon(object):
    """
    Common class for KivyBoost.
    """
    # The running app.
    app = ObjectProperty()

    def __init__(self):
        self.app = App.get_running_app()


class ResourceBase(object):
    """
    The base class for any resource, might it be audio, video, etc...
    """

    @classmethod
    def registry(cls):
        raise NotImplementedError

    @classmethod
    def base_path(cls):
        raise NotImplementedError

    @classmethod
    def path(cls):
        raise NotImplementedError

    @classmethod
    def fullpath(cls):
        return os.path.join(cls.base_path(), cls.path())

    @classmethod
    def name(cls):
        raise NotImplementedError

    @classmethod
    def requires_notice(cls):
        raise NotImplementedError

    @classmethod
    def artist(cls):
        raise NotImplementedError

    @classmethod
    def copyright_notice(cls):
        raise NotImplementedError

    @classmethod
    def copyright_link(cls):
        raise NotImplementedError


class AudioResourceBase(ResourceBase):
    """
    The base class for audio resources.
    """

    @classmethod
    def registry(cls):
        return 'audio'

    @classmethod
    def base_path(cls):
        raise NotImplementedError

    @classmethod
    def path(cls):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError

    @classmethod
    def requires_notice(cls):
        raise NotImplementedError

    @classmethod
    def artist(cls):
        raise NotImplementedError

    @classmethod
    def copyright_notice(cls):
        raise NotImplementedError

    @classmethod
    def copyright_link(cls):
        raise NotImplementedError


class FontResourceBase(ResourceBase):
    """
    The base class for font resources.
    """

    @classmethod
    def registry(cls):
        return 'fonts'

    @classmethod
    def base_path(cls):
        raise NotImplementedError

    @classmethod
    def path(cls):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError

    @classmethod
    def requires_notice(cls):
        raise NotImplementedError

    @classmethod
    def artist(cls):
        raise NotImplementedError

    @classmethod
    def copyright_notice(cls):
        raise NotImplementedError

    @classmethod
    def copyright_link(cls):
        raise NotImplementedError


class GraphicResourceBase(ResourceBase):
    """
    The base class for graphic resources.
    """

    @classmethod
    def registry(cls):
        return 'graphics'

    @classmethod
    def base_path(cls):
        raise NotImplementedError

    @classmethod
    def path(cls):
        raise NotImplementedError

    @classmethod
    def name(cls):
        raise NotImplementedError

    @classmethod
    def requires_notice(cls):
        raise NotImplementedError

    @classmethod
    def artist(cls):
        raise NotImplementedError

    @classmethod
    def copyright_notice(cls):
        raise NotImplementedError

    @classmethod
    def copyright_link(cls):
        raise NotImplementedError
