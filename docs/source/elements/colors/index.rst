.. _color:

Color
=====

.. rst-class:: lead

    Application of the color palette brings a unified and recognizable consistency to the array of digital products and interfaces.

Overview
--------

.. figure:: https://carbondesignsystem.com/4aac660a6246f8324e2c4dd8d47f4fa5/introduction.gif
    :class: centered

    Carbon Design Colors Overview

Color Anatomy
-------------

Carbon’s default themes are derived from the IBM Design Language color palette. The neutral gray family is dominant in the default themes, making use of subtle shifts in value to organize content into distinct zones.

The core blue family serves as the primary action color. Additional colors are used sparingly and purposefully.

.. seealso::

    `Color overview - Carbon Docs <https://carbondesignsystem.com/elements/color/overview/>`_

.. raw:: html

    <div class="color-grid" style="margin-top: 2rem;">
        <div class="color-box" style="background-color: rgb(0, 0, 0);"></div>
        <div class="color-box" style="background-color: rgb(0, 17, 65);"></div>
        <div class="color-box" style="background-color: rgb(0, 29, 108);"></div>
        <div class="color-box" style="background-color: rgb(0, 45, 156);"></div>
        <div class="color-box" style="background-color: rgb(0, 67, 206);"></div>
        <div class="color-box" style="background-color: rgb(15, 98, 254);"></div>
        <div class="color-box" style="background-color: rgb(69, 137, 255);"></div>
        <div class="color-box" style="background-color: rgb(120, 169, 255);"></div>
        <div class="color-box" style="background-color: rgb(166, 200, 255);"></div>
        <div class="color-box" style="background-color: rgb(208, 226, 255);"></div>
        <div class="color-box" style="background-color: rgb(237, 245, 255);"></div>
        <div class="color-box" style="background-color: rgb(255, 255, 255);"></div>
    </div>

   <div class="color-grid">
       <div class="color-box" style="background-color: rgb(0, 0, 0);"></div>
       <div class="color-box" style="background-color: rgb(22, 22, 22);"></div>
       <div class="color-box" style="background-color: rgb(38, 38, 38);"></div>
       <div class="color-box" style="background-color: rgb(57, 57, 57);"></div>
       <div class="color-box" style="background-color: rgb(82, 82, 82);"></div>
       <div class="color-box" style="background-color: rgb(111, 111, 111);"></div>
       <div class="color-box" style="background-color: rgb(141, 141, 141);"></div>
       <div class="color-box" style="background-color: rgb(168, 168, 168);"></div>
       <div class="color-box" style="background-color: rgb(198, 198, 198);"></div>
       <div class="color-box" style="background-color: rgb(224, 224, 224);"></div>
       <div class="color-box" style="background-color: rgb(244, 244, 244);"></div>
       <div class="color-box" style="background-color: rgb(255, 255, 255);"></div>
   </div>

   <div class="color-grid" style="margin-top: 2rem;">
       <div class="color-box" style="background-color: rgb(218, 30, 40);"></div>
       <div class="color-box" style="background-color: rgb(255, 131, 43);"></div>
       <div class="color-box" style="background-color: rgb(253, 220, 105);"></div>
       <div class="color-box" style="background-color: rgb(36, 161, 72);"></div>
   </div>


Tokens
------

Tokens are a method of applying color in a consistent, reusable, and scalable way. They are used in place of hard coded values, like hex codes. Whenever you update the theme of your app, these color tokens attains the desired value based on the current color theme and all the visual elements are updated dynamically.

For a complete list of available color tokens see the below API documentation of the available color classes implementing the colors or run the example code given below. You can also visit the official Carbon docs for reference.

.. seealso::

    `Color tokens - Carbon Docs <https://carbondesignsystem.com/elements/color/tokens/>`_

Example
^^^^^^^

.. figure:: /_static/images/elements/carbondesigncolorsexample.png
    :class: centered

    CarbonKivy Colors Example

.. code-block:: python

    from kivy.clock import Clock
    from kivy.core.window import Window


    def set_softinput(*args) -> None:
        Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
        Window.softinput_mode = "below_target"


    Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

    appkv = """
    CScreen:
        ColorView:
            size_hint: 1, 1
            viewclass: "MyColor"
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

    <MyColor@CAnchorLayout>:
        anchor_x: 'center'
        anchor_y: 'center'
        size_hint: 1, 1
        token: ""
        padding: dp(16)

        CLabel:
            text: root.token
            padding: dp(4)
            bg_color: [1, 1, 1, 0.6]
            color: app.text_primary
    """

    from kivy.lang import Builder
    from kivy.uix.recycleview import RecycleView

    from carbonkivy.theme.color_tokens import thematic_tokens, static_tokens
    from carbonkivy.app import CarbonApp
    from carbonkivy.uix.screen import CScreen


    class ColorView(RecycleView):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.app = CarbonApp.get_running_app()
            self.data = []
            tokenl = {}
            tokenl.update(thematic_tokens)
            tokenl.update(static_tokens)
            for token in tokenl.keys():
                if hasattr(self.app, token):
                    self.data.extend([
                        {
                            "bg_color": getattr(self.app, token),
                            "token": token,
                        }
                    ])


    class myapp(CarbonApp):
        def __init__(self, *args, **kwargs):
            super(myapp, self).__init__(*args, **kwargs)

        def build(self) -> CScreen:
            screen = Builder.load_string(appkv)
            return screen


    if __name__ == "__main__":
        myapp().run()

Thematic tokens
~~~~~~~~~~~~~~~

These tokens are expected to attain different color values based on the current color theme of the app.

.. seealso::

    :class:`~carbonkivy.theme.colors.ThematicColors`

Static tokens
~~~~~~~~~~~~~

These tokens are expected to attain a fixed color value on start.

.. seealso::

    :class:`~carbonkivy.theme.colors.StaticColors`


Usage
-----

- All available color tokens can be accessed via the main app class.

    .. tab-set::

        .. tab-item:: kvlang

            .. code-block:: kv

                CScreen:
                    bg_color: app.interactive

        .. tab-item:: python

            .. code-block:: python

                ...

                class MyApp(CarbonApp):

                    def build(self) -> CScreen:
                        self.screen = CScreen(bg_color=self.interactive)
                        return self.screen

                ...

- These tokens can also be used directly in the application but you'll need to bind an update to all the :class:`~carbonkivy.theme.color_tokens.thematic_tokens` inside the :class:`~carbonkivy.theme.CarbonTheme.on_theme` method based on the current color theme of your app.

    .. code-block:: python

        from kivy.properties import ColorProperty

        from carbonkivy.app import CarbonApp
        from carbonkivy.uix.color_tokens import thematic_tokens, static_tokens

        class MyApp(CarbonApp):

            mycolor = ColorProperty()

            def __init__(self, **kwargs) -> None:
                super(MyApp, self).__init__(**kwargs)
                self.mycolor = thematic_tokens["interactive"][self.theme]
            
            def on_theme(self, *args) -> None:
                super(MyApp, self).on_theme(*args)
                self.my_color = thematic_tokens["interactive"][self.theme]
        
        ...

- All available color tokens are a part of the :class:`~kivy.utils.colormap` utility, so they can also be used as normal strings.

    .. note::

        Using these tokens as strings attains color values based on the color theme of the app on start. These color values will not update with a change in the color theme.

    .. code-block:: kv

        CScreen:
            bg_color: "interactive" # attains a fixed color value on start.

API
---

.. automodule:: carbonkivy.theme.colors
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
