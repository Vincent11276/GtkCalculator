import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import calculator

if __name__ == '__main__':
    calculator = calculator.CalculatorWindow()
    calculator.show()
    Gtk.main()
    