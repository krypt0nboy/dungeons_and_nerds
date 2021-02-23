"""This file provides with GameAttribute base classes.

Game attributes can be used for both game logic and display.
"""


class GameAttributeBase(object):
    """
    Base class for GameAttribute.
    """

    def __init__(self, name: str = None, label: str = None, help_text: str = None):
        """
        :param str name: The attribute's machine name.
        :param str label: The attribute's label, a human readable name.
        :param str help_text: A short description to help understanding what the attribute is for.
        """
        self.name = name
        self.label = label
        self.help_text = help_text
