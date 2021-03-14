"""
Provides with Table classes.
"""
import csv
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty,
    BooleanProperty,
    NumericProperty
)
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView

from kivy_boost.common import KivyBoostCommon


Builder.load_string("""
<RowLabel>:
  canvas.before:
    Color:
      rgb: self.bgcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

Builder.load_string("""
<MasterSelector>:
  canvas.before:
    Color:
      rgb: self.bgcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

Builder.load_string("""
<RowSelector>:
  canvas.before:
    Color:
      rgb: self.bgcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


def build_batches(rows, num_rows_per_batch):
    batches = []
    num_rows = len(rows)
    num_batches = num_rows / num_rows_per_batch
    remains = num_rows % num_rows_per_batch
    base_index = 0
    for i in range(0, num_batches):
        batch = []
        for ii in range(0, num_rows_per_batch):
            batch.append(ii + (num_rows_per_batch * base_index))
        base_index += 1
        batches.append(batch)
    if remains:
        batch = []
        for ii in range(0, remains):
            batch.append(ii + (num_rows_per_batch * base_index))
        batches.append(batch)
    return batches


def on_checkbox_active(checkbox, value):
    """
    Activate, deactivate linked selectors in bulk.
    :param checkbox: The master checkbox
    :param value: Whether the checkbox is active.
    :return: None
    """
    if value:
        for c in checkbox.selectors:
            c.active = True
    else:
        for c in checkbox.selectors:
            c.active = False


class RowLabel(Label):
    """

    """
    bgcolor = ListProperty([1, 1, 1])


class MasterSelector(CheckBox, KivyBoostCommon):
    """
    The master selector.
    """
    # The associated selectors.
    selectors = ListProperty()
    bgcolor = ListProperty([1, 1, 1])


class RowSelector(CheckBox, KivyBoostCommon):
    """
    A row selector.
    """
    # The master selector.
    master = ObjectProperty()
    # The matching row index
    row_index = NumericProperty()
    bgcolor = ListProperty([1, 1, 1])


class Table(GridLayout, KivyBoostCommon):
    """
    Table class.
    """
    # The table header
    header = ObjectProperty()
    # The table body
    body = ObjectProperty()
    # The table's source
    source = ObjectProperty()
    # The table's header content
    header_ = ListProperty()
    # The table's rows content.
    rows_ = ListProperty()
    #
    current_rows = ListProperty()
    # Whether rows can be selected
    rows_selectable = BooleanProperty()
    # Cells len.
    cells_len = ListProperty()
    # Whether the table has been init yet.
    is_init = BooleanProperty()
    current_min_index = NumericProperty()
    #
    batches = ListProperty()
    #
    current_batch = NumericProperty()
    #
    prev_button = ObjectProperty()
    #
    next_button = ObjectProperty()
    #
    info_label = ObjectProperty()
    #
    limit = NumericProperty()

    def common_init(self):
        """
        :return:
        """
        self.feed()
        # noinspection PyUnexpectedType
        if self.header:
            self.header.cols = len(self.header_) + (1 if self.rows_selectable else 0)
            # noinspection PyUnresolvedReferences
            self.header.feed()
        if self.body:
            self.body.cols = len(self.header_) + (1 if self.rows_selectable else 0)
            len_rows = len(self.rows_)
            self.body.rows = len_rows if len_rows < self.limit else self.limit
            # noinspection PyUnresolvedReferences
            self.body.feed()

    def feed(self):
        """
        :return:
        """
        self.feed_rows()
        self.compute_cells_len()
        self.build_batches()
        self.current_batch = 0

    def feed_rows(self):
        """
        :return:
        """
        pass

    def build_batches(self):
        """
        :return:
        """
        self.batches = build_batches(self.rows_, self.limit)

    def compute_cells_len(self):
        """
        :return:
        """
        cells = map(lambda v: [], self.header_)
        index = 0
        for c in self.header_:
            cells[index].append(len(c))
            index += 1
        for row in self.rows_:
            index = 0
            for cell in row:
                cells[index].append(len(cell))
                index += 1
        for c in cells:
            self.cells_len.append(max(c))

    def update(self, source):
        """
        :param source:
        :return:
        """
        if not self.is_init:
            self.update_source(source)
            self.header.clear_widgets()
            self.body.clear_widgets()
            self.flush()
            self.common_init()

    def flush(self):
        """
        :return:
        """
        self.cells_len = []
        self.rows_ = []

    def update_source(self, source):
        """
        :param source:
        :return:
        """
        pass

    def prev_batch(self):
        """
        :return:
        """
        if self.current_batch >= 1:
            self.current_batch -= 1
            self.body.clear_widgets()
            self.body.feed()
        else:
            pass
        self.header.selector_widget.active = False
        self.update_info_label()

    def next_batch(self):
        """
        :return:
        """
        if self.current_batch < len(self.batches) - 1:
            self.current_batch += 1
            self.body.clear_widgets()
            self.body.feed()
        else:
            pass
        self.header.selector_widget.active = False
        self.update_info_label()

    def update_info_label(self):
        new_info = " - ".join(
            [str(self.batches[self.current_batch][0] + 1), str(self.batches[self.current_batch][-1] + 1)])
        self.info_label.text = new_info


class TableHeader(GridLayout, KivyBoostCommon):
    """
    Stores a table's header.
    """
    # The header table.
    table = ObjectProperty()
    # The selector widget.
    selector_widget = ObjectProperty()
    # The color of the cell's text.
    cells_color = ListProperty()
    # Whether the cell's are bold or not.
    cells_bold = BooleanProperty()
    # The cells halign.
    cells_halign = StringProperty()
    # The cells valign.
    cells_valign = StringProperty()

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        super(TableHeader, self).__init__(**kwargs)
        self.rows = 1

    def feed(self):
        """
        :return:
        """
        index = 0
        for cell in self.table.header_:
            self.add_widget(self.build_cell(text=cell, index=index))
            index += 1
        if self.table.rows_selectable:
            self.selector_widget = self.build_selector()
            self.add_widget(self.selector_widget)

    def clear(self):
        """
        :return:
        """
        for child in self.children:
            if isinstance(child, RowLabel) or isinstance(child, MasterSelector):
                self.remove_widget(child)

    def build_cell(self, text=None, index=None):
        """
        :param text:
        :param index:
        :return:
        """
        label = RowLabel()
        label.bgcolor = [0.5, 0.5, 0.5]
        label.text = text
        label.text_size = (self.table.cells_len[index] * 9, label.size[1])
        label.size_hint_x = self.table.cells_len[index] * 9
        label.size_hint_y = label.size[1]
        label.color = self.cells_color
        label.bold = self.cells_bold
        label.halign = self.cells_halign
        label.valign = self.cells_valign
        return label

    def build_selector(self):
        """
        :return:
        """
        checkbox = MasterSelector()
        checkbox.bind(active=on_checkbox_active)
        checkbox.id = "_".join([self.table.widget_id, 'selector'])
        checkbox.size_hint_x = 20
        checkbox.size_hint_y = 100
        checkbox.bgcolor = [0.5, 0.5, 0.5]
        return checkbox


class TableBody(GridLayout, KivyBoostCommon):
    """
    Stores a table's body.
    """
    table = ObjectProperty()
    # The color of the cell's text.
    cells_color = ListProperty()
    # Whether the cell's are bold or not.
    cells_bold = BooleanProperty()
    # The cells halign.
    cells_halign = StringProperty()
    # The cells valign.
    cells_valign = StringProperty()
    #
    cells_ = ListProperty()

    def feed(self):
        """
        :return:
        """
        if len(self.table.batches):
            for i in self.table.batches[self.table.current_batch]:
                row = self.table.rows_[i]
                cells_index = 0
                for value in row:
                    cell = self.build_cell(text=value, index=cells_index)
                    self.add_widget(cell)
                    self.cells_.append(cell)
                    cells_index += 1
                if self.table.rows_selectable:
                    selector = self.build_selector(i)
                    self.add_widget(selector)
                    self.cells_.append(selector)

    def clear(self):
        """
        :return:
        """
        self.clear_widgets(self.cells_)

    def build_cell(self, text=None, index=None):
        """
        :param text:
        :param index:
        :return:
        """
        label = RowLabel()
        label.bgcolor = [1, 1, 1]
        label.text = text
        label.text_size = (self.table.cells_len[index] * 9, label.size[1])
        label.size_hint_x = self.table.cells_len[index] * 9
        label.size_hint_y = label.size[1]
        label.color = self.cells_color
        label.bold = self.cells_bold
        label.halign = self.cells_halign
        label.valign = self.cells_valign
        return label

    def build_selector(self, index):
        """
        :param index:
        :return:
        """
        checkbox = RowSelector()
        checkbox.row_index = index
        checkbox.master = self.table.header.selector_widget
        self.table.header.selector_widget.selectors.append(checkbox)
        checkbox.id = "_".join([self.table.widget_id, 'row', str(index)])
        checkbox.size_hint_x = 20
        checkbox.size_hint_y = 100
        return checkbox


class FileTable(Table, KivyBoostCommon):
    """
    Table with a file as source.
    """
    # The source filename.
    source_filename = StringProperty()
    # The source format.
    source_format = StringProperty()
    # The handler.
    handler = ObjectProperty()
    # First row is header.
    first_row_is_header = BooleanProperty()

    def feed_rows(self):
        if self.source_filename is not '':
            self.source = open(self.source_filename, mode="rb")
            self.handler = csv.reader(self.source, delimiter=";")
            if self.first_row_is_header:
                skip = next(self.handler)
            for row in self.handler:
                self.rows_.append(row)

    def update_source(self, source):
        self.source_filename = source


class ScrollableFileTable(FileTable, ScrollView):
    """

    """
    pass


Factory.register('KivyB', module='RowLabel')
