"""
Provides with FormComponent class.
"""
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    NumericProperty
)

from kivy_boost.common import KivyBoostCommon


class FormComponent(KivyBoostCommon):
    """
    A form component.
    """
    # The component's form
    form = ObjectProperty()


class FormField(FormComponent):
    """
    A form field.
    """
    field = ObjectProperty()
