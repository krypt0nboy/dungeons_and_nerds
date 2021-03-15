"""
"""
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout


class BoostedPopup(Popup):
    """
    """
    pass


class WarningPopup(BoostedPopup):
    """
    """

    is_open = BooleanProperty(defaultvalue=False)

    def __init__(self):
        super(WarningPopup, self).__init__()
        #self.add_widget()

    def on_open(self):
        self.is_open = True
        print('foo')

    def on_dismiss(self):
        self.is_open = False

    def warn(self, warnings=None, *largs, **kwargs):
        if not self.is_open:
            self.populate_content(warnings=warnings)
            self.open(*largs, **kwargs)

    def populate_content(self, warnings=None):
        #title: 'Log in required'
        pass

    def clear_content(self):
        self.title = ''
