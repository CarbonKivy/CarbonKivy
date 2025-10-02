from __future__ import annotations

__all__ = (
    "CDatePicker",
)


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from datetime import date, timedelta
import calendar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, ObjectProperty, NumericProperty, OptionProperty, StringProperty, DictProperty

from carbonkivy.uix.button import CButton
from carbonkivy.behaviors import ElevationBehavior, SelectableBehavior
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.gridlayout import CGridLayout


class CDatePicker(CBoxLayout, ElevationBehavior):

    visibility = BooleanProperty(False, allownone=True)

    master = ObjectProperty()

    margin = NumericProperty(None, allownone=True)

    pointer = OptionProperty("Upward", options=["Upward", "Downward"])

    _pointer = OptionProperty("Upward", options=["Upward", "Downward"])

    today = ObjectProperty(date.today())

    current_month = NumericProperty()

    current_year = NumericProperty()

    month_name = StringProperty()

    def __init__(self, **kwargs):
        super(CDatePicker, self).__init__(**kwargs)
        self.current_month = self.today.month
        self.current_year = self.today.year
        self.month_name = calendar.month_name[int(self.current_month)]

    def update_pos(self, instance: Widget, *args) -> None:
        pos_x, pos_y = [
            instance.center_x - dp(16),
            instance.top + dp(12) if (self.pointer == "Downward") else instance.y - self.height - dp(12),
        ]

        instance_center = instance.to_window(instance.center_x, instance.center_y)

        if instance_center[0] < self.width / 2:
            pos_x = instance.center_x - dp(16) if (not self.margin) else self.margin
        elif (Window.width - instance_center[0]) < self.width / 2:
            pos_x = instance.center_x - self.width + dp(16) if (not self.margin) else Window.width - self.width - self.margin

        if (Window.height - instance_center[1]) < (
            instance.height / 2 + self.height + dp(12)
        ):
            pos_y = instance.y - self.height - dp(12)
            self._pointer = "Upward"
        elif (instance_center[1]) < (instance.height/2 + self.height + dp(12)):
            pos_y = instance.top + dp(12)
            self._pointer = "Downward"
        else:
            self._pointer = self.pointer

        self.pos = instance.to_window(*[pos_x, pos_y])

    # def on_touch_down(self, touch):
    #     if not self.collide_point(*touch.pos) and not self.master.collide_point(*self.master.to_parent(*self.master.to_widget(*touch.pos))):
    #         self.visibility = False
    #     return super().on_touch_down(touch)

    def on_visibility(self, *args) -> None:

        def set_visibility(*args) -> None:
            if self.visibility:
                try:
                    self.update_pos(self.master)
                    self.master.bind(pos=self.update_pos)
                    Window.add_widget(self)
                except Exception as e:
                    print(e)
            else:
                try:
                    self.master.unbind(pos=self.update_pos)
                    Window.remove_widget(self)
                except Exception:
                    return


        Clock.schedule_once(set_visibility)

    def month_prev(self, *args) -> None:
        Clock.unschedule(self.ids.cdatepickercalendar.update_calendar)
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.month_name = calendar.month_name[int(self.current_month)]
        self.ids.cdatepickercalendar.clear_widgets()
        Clock.schedule_once(self.ids.cdatepickercalendar.update_calendar, 0.01)

    def month_next(self, *args) -> None:
        Clock.unschedule(self.ids.cdatepickercalendar.update_calendar)
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.month_name = calendar.month_name[int(self.current_month)]
        self.ids.cdatepickercalendar.clear_widgets()
        Clock.schedule_once(self.ids.cdatepickercalendar.update_calendar, 0.01)


class CDatePickerDayButton(CButton, SelectableBehavior):

    day = NumericProperty()

    month = NumericProperty()

    year = NumericProperty()

    is_today = BooleanProperty(False)

    is_current_month = BooleanProperty(False)

    data = DictProperty()

    def __init__(self, **kwargs) -> None:
        super(CDatePickerDayButton, self).__init__(**kwargs)

    def on_data(self, instance, value) -> None:
        self.day = str(value.get('day', ''))
        self.month = str(value.get('month', ''))
        self.year = str(value.get('year', ''))
        self.is_today = value.get('is_today', False)
        self.is_current_month = value.get('is_current_month', False)


class CDatePickerHeader(CBoxLayout):

    def __init__(self, **kwargs) -> None:
        super(CDatePickerHeader, self).__init__(**kwargs)


class CDatePickerCalendar(CGridLayout):

    selected_date = ObjectProperty()

    selected_button = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super(CDatePickerCalendar, self).__init__(**kwargs)
        Clock.schedule_once(self.update_calendar)

    def get_calendar_dates(self, year: str, month: str) -> None:
        '''Get all dates for a 7x7 calendar grid including prev/next month dates'''
        # Get the first day of the month and its weekday
        first_day = date(year, month, 1)
        first_weekday = first_day.weekday()
        # Convert Monday=0 to Sunday=0 format
        first_weekday = (first_weekday + 1) % 7

        # Get the last day of the month
        if month == 12:
            last_day = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = date(year, month + 1, 1) - timedelta(days=1)

        # Calculate start date (may be from previous month)
        start_date = first_day - timedelta(days=first_weekday)

        # Generate 49 days (7x7 grid)
        dates = []
        current_date = start_date
        for i in range(42):  # 7 rows x 7 days = 49 cells
            dates.append(current_date)
            current_date += timedelta(days=1)

        return dates

    def update_calendar(self, *args) -> None:
        # Clear previous calendar
        self.clear_widgets()

        # Get all dates for the 7x7 grid
        dates = self.get_calendar_dates(int(self.parent.current_year), int(self.parent.current_month))

        for calendar_date in dates:
            is_current_month = calendar_date.month == int(self.parent.current_month)
            is_today = calendar_date == self.parent.today

            btn = CDatePickerDayButton(
                text=str(calendar_date.day),
                day=calendar_date.day,
                month=calendar_date.month,
                year=calendar_date.year,
                is_today=is_today,
                is_current_month=is_current_month,
                role="Large Productive",
            )
            try:
                if (btn.day == self.selected_date.day) and (btn.month == self.selected_date.month) and btn.year == self.selected_date.year:
                    btn.selected = True
            except:
                pass
            btn.bind(on_press=lambda x, btn_date=calendar_date: self.select_date(btn_date, x))
            Clock.schedule_once(lambda e, y=btn: self.add_widget(y))

    def select_date(self, selected_date, button):
        # # Reset previous selection
        # if self.selected_button:
        #     self.selected_button.set_selected(False)

        # Set new selection
        self.selected_date = selected_date
        self.selected_button = button
        button.selected = True

        # If selected date is from different month, navigate to that month
        if selected_date.month != self.parent.current_month:
            self.parent.current_month = selected_date.month
            self.parent.current_year = selected_date.year
            self.parent.month_name = calendar.month_name[int(self.parent.current_month)]
            self.update_calendar()
            # Re-select the date in the new calendar view
            for child in self.parent.children:
                if (hasattr(child, 'day') and child.day == selected_date.day and 
                    child.month == selected_date.month and child.year == selected_date.year):
                    child.selected = True
                    self.selected_button = child
                    break

        print(f"Selected date: {self.selected_date}")
