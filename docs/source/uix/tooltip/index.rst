.. _tooltip:

Tooltip
===========

.. rst-class:: lead

    Tooltips display additional information upon hover or focus that is contextual, helpful, and nonessential while providing the ability to communicate and give clarity to a user.

Overview
--------

.. figure:: /_static/images/tooltip/carbondesigntooltip.png
    :class: centered

    Carbon Design Tooltip Overview

A tooltip is embedded within other components rather than being used as a standalone component. They provide additional information when a user hovers over or focuses on a UI element and should only be used when necessary to offer quick context without cluttering the interface.

*Only vertical variant of CTooltip is available.*

Live demo
---------

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Default

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-tooltip--default&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: python

            ...

            from carbonkivy.behaviors import TooltipBehavior
            from carbonkivy.uix.link import CLink
            from carbonkivy.uix.tooltip import CTooltip


            class TooltipLink(CLink, TooltipBehavior):
                def __init__(self, **kwargs) -> None:
                    super().__init__(**kwargs)
                    self.tooltip = CTooltip(text="Occasionally, services are updated in a specified time window to ensure no down time for customers.")

            kvlang = """
            CScreen:
                TooltipLink:
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    CLinkIcon:
                        icon: "help"
            """

            ...

Usage
-----

For embedding a tooltip to any widget, the widget needs to inherit from the :class:`~carbonkivy.behaviors.tooltip_behavior.TooltipBehavior` class and then define a tooltip widget inheriting from :class:`~carbonkivy.uix.tooltip.tooltip.CTooltip` class.

Use the :class:`~carbonkivy.behaviors.tooltip_behavior.TooltipBehavior.tooltip` property to define the widget to be displayed as a tooltip.

.. note::

    On DESKTOP platforms, the tooltip will appear if hovered over the widget, by default.
    For this the widget should be an instance of the class :class:`~carbonkivy.behaviors.hover_behavior.HoverBehavior`.

.. code-block:: python

    ...

    from carbonkivy.behaviors import TooltipBehavior
    from carbonkivy.uix.tooltip import CTooltip

    from carbonkivy.uix.button import CButtonPrimary

    class TooltipButton(CButtonPrimary, TooltipBehavior):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)
            self.tooltip = CTooltip(text="This is a Tooltip.")

    ...

Example
-------

.. code-block:: python

    from kivy.clock import Clock
    from kivy.core.window import Window


    def set_softinput(*args) -> None:
        Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
        Window.softinput_mode = "below_target"


    Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

    appkv = """
    CScreen:

        TooltipButton:
            text: "Drag Me!"
            icon: "add--large"
            pos: [30, 30]
    """

    from kivy.input.providers.mouse import MouseMotionEvent
    from kivy.lang import Builder
    from kivy.metrics import dp

    from carbonkivy.app import CarbonApp
    from carbonkivy.behaviors import TooltipBehavior
    from carbonkivy.uix.button import CButtonPrimary
    from carbonkivy.uix.screen import CScreen
    from carbonkivy.uix.tooltip import CTooltip


    class TooltipButton(CButtonPrimary, TooltipBehavior):

        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)
            self.tooltip = CTooltip(text="This is a large Tooltip text.", width=dp(200))

        def on_touch_move(self, touch: MouseMotionEvent, *args) -> bool | None:
            self.center_x, self.center_y = touch.pos
            return super().on_touch_move(touch)


    class myapp(CarbonApp):
        def __init__(self, *args, **kwargs):
            super(myapp, self).__init__(*args, **kwargs)

        def build(self) -> CScreen:
            screen = Builder.load_string(appkv)
            return screen


    if __name__ == "__main__":
        myapp().run()

API
---

.. automodule:: carbonkivy.uix.tooltip.tooltip
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:

