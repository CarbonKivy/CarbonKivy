import os

from kivy.lang import Builder

from carbonkivy.config import UIX

from .datepicker import (
    CDatePicker,
    CDatePickerCalendar,
    CDatePickerDayButton,
    CDatePickerHeader,
)

filename = os.path.join(UIX, "datepicker", "datepicker.kv")
if not filename in Builder.files:
    Builder.load_file(filename)
