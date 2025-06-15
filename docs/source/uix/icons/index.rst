.. _icons:

Icons
=====

.. rst-class:: lead

	Icons are visual symbols used to represent ideas, objects, or actions. They communicate messages at a glance, afford interactivity, and draw attention to important information.

Overview
--------

.. figure:: /_static/images/icons/carbondesignicons.svg
    :class: centered

.. seealso::

    `Icons - Carbon Design System <https://carbondesignsystem.com/elements/icons/library/>`_

The :class:`~carbonkivy.uix.icon.icon.CIcon` class provides you with the ability to display available Carbon Design Icons. 

`Access the icon font here <https://github.com/CarbonKivy/CarbonKivy/tree/master/carbonkivy/data/Icons/carbondesignicons.ttf>`_.
This Icon font is managed by `Kartavya Shukla <https://github.com/Novfensec>`_.

For a complete dictionary of available glyph codes visit `CarbonKivy Glyph Codes Dictionary <https://github.com/CarbonKivy/CarbonKivy/tree/master/carbonkivy/theme/icons.py>`_.

.. code-block:: kv

    CIcon:
        icon: "shopping--cart"
        color: app.interactive
        font_size: plex_16

Example
-------


.. figure:: /_static/images/icons/carbondesignicons.png
    :class: centered

Run the below code for a full-fledged running example with all available glyphs.

.. code-block:: python

    from kivy.clock import Clock
    from kivy.core.window import Window


    def set_softinput(*args) -> None:
        Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
        Window.softinput_mode = "below_target"


    Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

    appkv = """
    CScreen:

        CLabel:
            text: f"{app.icon_count} glyphs"
            color: app.text_primary
            style: "heading_04"
            padding: dp(8)
            pos_hint: {"top": 1}

        IconView:
            size_hint: 1, 0.9
            viewclass: "MyIcon"
            bar_width: "20dp"
            do_scroll_x: False
            scroll_type: ['bars', 'content']

            RecycleGridLayout:
                cols: 2
                default_size: None, None
                default_size_hint: 1, None
                size_hint: 1, None
                height: self.minimum_height
                padding: [dp(16), dp(16), dp(16), dp(16)]
                spacing: dp(20)

    <MyIcon@CAnchorLayout>:
        anchor_x: 'center'
        anchor_y: 'center'
        size_hint: 1, 1
        text: ""
        icon: ""

        CBoxLayout:
            spacing: "20dp"
            orientation: "vertical"
            adaptive: [False, True]
            CIcon:
                multiline: True
                icon: root.icon
                font_size: plex_32
                pos_hint: {'center_x': 0.5}
            CLabel:
                text: root.text
                halign: "center"
    """

    from kivy.lang import Builder
    from kivy.uix.recycleview import RecycleView

    from carbonkivy.app import CarbonApp
    from carbonkivy.theme.icons import ibm_icons
    from carbonkivy.uix.screen import CScreen


    class IconView(RecycleView):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.data = []
            for icons in ibm_icons.keys():
                self.data.extend([{"icon": icons, "text": icons}])


    class myapp(CarbonApp):
        def __init__(self, *args, **kwargs):
            super(myapp, self).__init__(*args, **kwargs)
            self.icon_count = len(ibm_icons.keys())

        def build(self) -> CScreen:
            screen = Builder.load_string(appkv)
            return screen


    if __name__ == "__main__":
        myapp().run()

API
---

.. automodule:: carbonkivy.uix.icon.icon
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
