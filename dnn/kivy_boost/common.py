"""
Provides with common properties and attributes for kivy boost.
"""
from kivy.app import App
from kivy.properties import ObjectProperty

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


class AudioResourceBase(ResourceBase):
    """
    The base class for audio resources.
    """

    @classmethod
    def registry(cls):
        return 'audio'

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
