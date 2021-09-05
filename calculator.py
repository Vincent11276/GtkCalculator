from re import S, match, sub
from typing import Match, Text, get_type_hints
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from enum import Enum, auto


class Operations(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    NIL = auto()


@Gtk.Template(filename='calculator.ui')
class CalculatorWindow(Gtk.Window):
    __gtype_name__ = 'main_window'

    _output_ent: Gtk.Entry = Gtk.Template.Child('output_ent')

    def __init__(self) -> None:
        super().__init__()
        self.operation    = Operations.NIL
        self.first_value  = 0
        self.second_value = 0
        self.has_to_reset = False
        self.is_opera_set = False

    def set_operation(self, operation: Operations):
        self.operation    = operation
        self.has_to_reset = True
        self.is_opera_set = True
        self.first_value  = float(self._output_ent.get_text())

    def calculate(self):
        if self.is_opera_set: 
            self.second_value = float(self._output_ent.get_text())
            self.is_opera_set = False

        if self.operation == Operations.ADD:
            result = self.first_value + self.second_value   
        elif self.operation == Operations.SUB:
            result = self.first_value - self.second_value
        elif self.operation == Operations.MUL:
            result = self.first_value * self.second_value
        elif self.operation == Operations.DIV:
            result = self.first_value / self.second_value

        self._output_ent.set_text(str(result))
        self.first_value = result

    def appendDigit(self, digit: str):
        if self.has_to_reset:
            self.has_to_reset = False
            self.clear_output()

        current_text = self._output_ent.get_text()
        self._output_ent.set_text(current_text + digit)

    def do_hundreths(self):
        res = float(self._output_ent.get_text()) / 100
        self._output_ent.set_text(str(res))

    def do_identity_prop(self):
        res = float(self._output_ent.get_text()) * -1
        self._output_ent.set_text(str(res))

    def reset_output(self):
        self._output_ent.set_text('0')

    def clear_output(self):
        self._output_ent.set_text('')

    def reset_all(self):
        self.operation    = Operations.NIL
        self.first_value  = 0
        self.second_value = 0
        self.has_to_reset = False
        self.is_opera_set = False
        self._output_ent.set_text('0')

    # ===================== Widget Handlers =====================

    @Gtk.Template.Callback()
    def on_main_window_destroy(self, widget, user_data=None):
        Gtk.main_quit()

    @Gtk.Template.Callback()
    def on_cancel_btn_clicked(self, widget, user_data=None):
        self.reset_all()

    @Gtk.Template.Callback()
    def on_dot_btn_clicked(self, widget, user_data=None):
        self.appendDigit('.')

    @Gtk.Template.Callback()
    def on_equal_btn_clicked(self, widget, user_data=None):
        self.calculate()

    @Gtk.Template.Callback()
    def on_plus_btn_clicked(self, widget, user_data=None):
        self.set_operation(Operations.ADD)

    @Gtk.Template.Callback()
    def on_minus_btn_clicked(self, widget, user_data=None):
        self.set_operation(Operations.SUB)

    @Gtk.Template.Callback()
    def on_multiply_btn_clicked(self, widget, user_data=None):
        self.set_operation(Operations.MUL)

    @Gtk.Template.Callback()
    def on_division_btn_clicked(self, widget, user_data=None):
        self.set_operation(Operations.DIV)

    @Gtk.Template.Callback()
    def on_opp_sign_btn_clicked(self, widget, user_data=None):
        self.do_identity_prop()

    @Gtk.Template.Callback()
    def on_percent_btn_clicked(self, widget, user_data=None):
        self.do_hundreths()

    @Gtk.Template.Callback()
    def on_zero_btn_clicked(self, widget, user_data=None):
        self.appendDigit('0')

    @Gtk.Template.Callback()
    def on_one_btn_clicked(self, widget, user_data=None):
        self.appendDigit('1')

    @Gtk.Template.Callback()
    def on_two_btn_clicked(self, widget, user_data=None):
        self.appendDigit('2')

    @Gtk.Template.Callback()
    def on_three_btn_clicked(self, widget, user_data=None):
        self.appendDigit('3')

    @Gtk.Template.Callback()
    def on_four_btn_clicked(self, widget, user_data=None):
        self.appendDigit('4')

    @Gtk.Template.Callback()
    def on_five_btn_clicked(self, widget, user_data=None):
        self.appendDigit('5')

    @Gtk.Template.Callback()
    def on_six_btn_clicked(self, widget, user_data=None):
        self.appendDigit('6')

    @Gtk.Template.Callback()
    def on_seven_btn_clicked(self, widget, user_data=None):
        self.appendDigit('7')
        
    @Gtk.Template.Callback()
    def on_eight_btn_clicked(self, widget, user_data=None):
        self.appendDigit('8')

    @Gtk.Template.Callback()
    def on_nine_btn_clicked(self, widget, user_data=None):
        self.appendDigit('9')