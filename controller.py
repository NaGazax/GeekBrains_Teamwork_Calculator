# Все связующий и управляющий скрипт

import view
import operations
import log

def button_click():
    value_lst = view.get_value()
    operations.calc(value_lst)
    result = operations.calc()
    view.output(result)
