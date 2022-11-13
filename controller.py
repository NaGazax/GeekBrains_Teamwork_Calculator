# Все связующий и управляющий скрипт

import view
import operations
import log

def button_click():
    value_lst = view.get_value()
    operations.init(value_lst)

