"""
Provides with views widgets and views buttons widgets.
"""
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    NumericProperty
)
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy_boost.common import KivyBoostCommon


class ViewsController(Widget, KivyBoostCommon):
    """
    Controls a set of views.
    A ViewsController instance hides the inactive views and displays the active one.
    """

    # The buttons associated with the views
    views_buttons = ListProperty()
    # The views to control
    views = ListProperty()
    # The active view
    active_view = ObjectProperty()
    # The default horizontal position for the active view.
    default_pos_h = NumericProperty()
    # The default vertical position for the active view.
    default_pos_w = NumericProperty()
    # The default horizontal position for the hidden views (Should be negative value).
    default_pos_h_hidden = NumericProperty()
    # The default vertical position for the hidden views (Should be negative value).
    default_pos_w_hidden = NumericProperty()
    # The active button color
    active_color = ListProperty()
    # The active button background color
    active_background_color = ListProperty()

    def add_widget(self, widget, index=0, canvas=None):
        super(ViewsController, self).add_widget(widget, index=index, canvas=canvas)
        if isinstance(widget, ViewButton):
            self.views_buttons.append(widget)
            widget.controller = self
        if isinstance(widget, View):
            self.views.append(widget)

    def hide_view(self, view):
        """
        :param view:
        :return:
        """
        view.pos = self.default_pos_w_hidden, self.default_pos_h_hidden
        view.button.bold = False

    def set_view_active(self, view):
        """
        :param view:
        :return:
        """
        view.pos = self.default_pos_w, self.default_pos_h
        view.button.color = self.active_color
        view.button.background_color = self.active_background_color
        view.button.bold = True
        for v in self.views:
            if v != view:
                self.hide_view(v)


class ViewButton(Button, KivyBoostCommon):
    """
    Button for a view.
    """
    # The view associated with the button.
    view = ObjectProperty()
    # The controller associated.
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super(ViewButton, self).__init__(**kwargs)
        self.font_name = '/System/Library/Fonts/Courier.dfont'
        self.font_name = '/Users/haroldcohen/Library/Fonts/Fipps-Regular.otf'

    def on_release(self):
        """
        :return:
        """
        self.controller.set_view_active(self.view)


class ViewBase(Widget, KivyBoostCommon):
    """
    View class.
    """
    pass


class View(ViewBase):
    """
    View class.
    """
    # The title of the view.
    title = StringProperty()
    # The button associated with the view.
    button = ObjectProperty()
    # Whether the view is active.
    is_active = BooleanProperty(defaultvalue=False)


class ViewBaseGrid(ViewBase, GridLayout):
    """
    View as GridLayout.
    """
    pass


class ViewGrid(View, GridLayout):
    """
    View as GridLayout.
    """
    pass


class ScrollableViewGrid(ViewGrid, ScrollView):
    """

    """
    pass
