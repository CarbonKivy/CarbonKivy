from __future__ import annotations

__all__ = (
    "CDatePicker",
    "CDatePickerCalendar",
    "CDatePickerDayButton",
    "CDatePickerHeader",
)


import calendar
from datetime import date, timedelta

from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.widget import Widget

from carbonkivy.behaviors import ElevationBehavior, SelectableBehavior
from carbonkivy.uix.boxlayout import CBoxLayout
from carbonkivy.uix.button import CButton
from carbonkivy.uix.gridlayout import CGridLayout
from carbonkivy.utils import DEVICE_TYPE


class CDatePicker(CBoxLayout, ElevationBehavior):

    visibility = BooleanProperty(False, allownone=True)

    master = ObjectProperty()

    margin = NumericProperty(None, allownone=True)

    pointer = OptionProperty("Downward", options=["Upward", "Downward"])

    _pointer = OptionProperty("Downward", options=["Upward", "Downward"])

    today = ObjectProperty(date.today())

    current_month = NumericProperty()

    current_year = NumericProperty()

    month_name = StringProperty()

    selected_date = ObjectProperty(date.today(), allownone=True)

    def __init__(self, **kwargs):
        super(CDatePicker, self).__init__(**kwargs)
        self.current_month = self.today.month
        self.current_year = self.today.year
        self.month_name = calendar.month_name[int(self.current_month)]

    def on_master(self, *args) -> None:
        if self.master and DEVICE_TYPE == "desktop":
            self.update_pos(self.master)

    @mainthread
    def update_pos(self, instance: Widget, *args) -> None:
        pos_x, pos_y = [
            instance.center_x - dp(16),
            (
                instance.top + dp(12)
                if (self.pointer == "Downward")
                else instance.y - self.height - dp(12)
            ),
        ]

        instance_center = instance.to_window(
            *instance.to_local(
                *instance.to_parent(*[instance.center_x, instance.center_y])
            )
        )

        if instance_center[0] < self.width / 2:
            pos_x = instance.center_x - dp(16) if (not self.margin) else self.margin
        elif (Window.width - instance_center[0]) < self.width / 2:
            pos_x = (
                instance.center_x - self.width + dp(16)
                if (not self.margin)
                else Window.width - self.width - self.margin
            )

        if (Window.height - instance_center[1]) < (
            instance.height / 2 + self.height + dp(12)
        ):
            pos_y = instance.top - self.height
        elif (instance_center[1]) < (instance.height / 2 + self.height + dp(12)):
            pos_y = instance.top + dp(12)
        else:
            self._pointer = self.pointer

        self.pos = instance.to_window(
            *instance.to_local(*instance.to_parent(*[pos_x, pos_y]))
        )

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) and not self.master.collide_point(
            *self.master.to_parent(*self.master.to_widget(*touch.pos))
        ):
            self.visibility = False
        return super().on_touch_down(touch)

    def on_visibility(self, *args) -> None:
        Clock.unschedule(self.set_visibility)
        Clock.schedule_once(self.set_visibility)

    def set_visibility(self, *args) -> None:
        if self.visibility:
            try:
                if DEVICE_TYPE == "desktop":
                    self.update_pos(self.master)
                    self.master.bind(pos=self.update_pos)
                else:
                    self.pos_hint = {"center_y": 0.5}
                Window.add_widget(self)
            except Exception as e:
                print(e)
        else:
            try:
                self.master.unbind(pos=self.update_pos)
                Window.remove_widget(self)
            except Exception:
                return

    def month_prev(self, *args) -> None:
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.month_name = calendar.month_name[int(self.current_month)]
        Clock.unschedule(self.ids.cdatepickercalendar.update_calendar)
        Clock.schedule_once(self.ids.cdatepickercalendar.update_calendar)

    def month_next(self, *args) -> None:
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.month_name = calendar.month_name[int(self.current_month)]
        Clock.unschedule(self.ids.cdatepickercalendar.update_calendar)
        Clock.schedule_once(self.ids.cdatepickercalendar.update_calendar)


class CDatePickerDayButton(CButton, SelectableBehavior):

    day = NumericProperty()

    month = NumericProperty()

    year = NumericProperty()

    is_today = BooleanProperty(False)

    is_current_month = BooleanProperty(False)

    date = ObjectProperty(None, allownone=True)

    callback_selection = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        super(CDatePickerDayButton, self).__init__(**kwargs)

    def on_press(self) -> None:
        if self.callback_selection:
            self.callback_selection(self.date, self)


class CDatePickerHeader(CBoxLayout):

    def __init__(self, **kwargs) -> None:
        super(CDatePickerHeader, self).__init__(**kwargs)


class CDatePickerCalendar(CGridLayout):

    selected_date = ObjectProperty(None, allownone=True)

    selected_button = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs) -> None:
        self.selected_date = date.today()
        super(CDatePickerCalendar, self).__init__(**kwargs)
        Clock.schedule_once(self.update_calendar)

    def on_selected_date(self, *args) -> None:
        try:
            self.parent.selected_date = self.selected_date
        except Exception as e:
            print(e)

    def get_calendar_dates(self, year: str, month: str) -> None:
        """Get all dates for a 7x7 calendar grid including prev/next month dates"""
        # Get the first day of the month and its weekday
        first_day = date(year, month, 1)
        first_weekday = first_day.weekday()
        # Convert Monday=0 to Sunday=0 format
        first_weekday = (first_weekday + 1) % 7

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
        self.clear_selection()

        # Get all dates for the 7x7 grid
        dates = self.get_calendar_dates(
            int(self.parent.current_year), int(self.parent.current_month)
        )

        for i, calendar_date in enumerate(dates):
            is_current_month = calendar_date.month == int(self.parent.current_month)
            is_today = calendar_date == self.parent.today

            if len(self.children) > 1:
                i += 1
                self.children[-i].text = str(calendar_date.day)
                self.children[-i].date = calendar_date
                self.children[-i].day = calendar_date.day
                self.children[-i].month = calendar_date.month
                self.children[-i].year = calendar_date.year
                self.children[-i].is_today = is_today
                self.children[-i].is_current_month = is_current_month

                for widget in self.children:
                    if (
                        widget.day == self.selected_date.day
                        and widget.month
                        == self.selected_date.month
                        == self.parent.current_month
                        and widget.year == self.selected_date.year
                    ):
                        widget.selected = True
                        self.selected_button = widget
                        self.selected_date = widget.date
                    else:
                        widget.selected = False
            else:
                btn = CDatePickerDayButton(
                    text=str(calendar_date.day),
                    day=calendar_date.day,
                    month=calendar_date.month,
                    year=calendar_date.year,
                    date=calendar_date,
                    is_today=is_today,
                    is_current_month=is_current_month,
                    role="Large Productive",
                )
                if (
                    btn.day == self.selected_date.day
                    and btn.month
                    == self.selected_date.month
                    == self.parent.current_month
                    and btn.year == self.selected_date.year
                ):
                    btn.selected = True
                    self.selected_button = btn
                    self.selected_date = btn.date
                btn.callback_selection = self.select_date
                Clock.schedule_once(lambda dt, y=btn: self.add_widget(y))

    def clear_selection(self, *args) -> None:
        for widget in self.children:
            widget.selected = False
            self.selected_button = None

    def select_date(self, selected_date, button):
        Clock.unschedule(self.update_calendar)

        # Set new selection
        self.selected_date = selected_date
        self.selected_button = button
        button.selected = True

        # If selected date is from different month, navigate to that month
        if selected_date.month != self.parent.current_month:
            self.clear_selection()
            self.parent.current_month = selected_date.month
            self.parent.current_year = selected_date.year
            self.parent.month_name = calendar.month_name[int(self.parent.current_month)]
            # Re-select the date in the new calendar view
            for child in self.parent.children:
                if (
                    hasattr(child, "day")
                    and child.day == selected_date.day
                    and child.month == selected_date.month
                    and child.year == selected_date.year
                ):
                    child.selected = True
                    self.selected_button = child
                    break

        Clock.schedule_once(self.update_calendar)
        print(f"Selected date: {self.selected_date}")
