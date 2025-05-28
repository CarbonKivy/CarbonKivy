.. _Carbon-Design-App:

Carbon Design App
=================

.. rst-class:: lead

    The :class:`~carbonkivy.app.CarbonApp` class inherits from :class:`~kivy.app.App` and :class:`~carbonkivy.theme.theme.CarbonTheme` to define and update the theme and appropriate colors based on the given theme.

Overview
--------

.. figure:: /_static/images/carbondesignexamples.svg
    :class: centered

    Carbon Kivy Examples Overview

.. seealso::

    `CarbonKivy Examples on Github <https://github.com/CarbonKivy/CarbonKivy/tree/master/examples>`_

Minimal Example
---------------

Below is an example code of a basic CarbonKivy application.

.. code-block:: python

    from kivy.lang import Builder

    from carbonkivy.app import CarbonApp
    from carbonkivy.uix.screen import CScreen

    class MyApp(CarbonApp):

        def __init__(self, **kwargs):
            super(MyApp, self).__init__(**kwargs)

        def build(self, *args) -> CScreen:
            self.kvlang = '''

    CScreen:

        CLabel:
            text: "Carbon Design System"
            font_size: plex_18
            halign: "center"
            pos_hint: {"center_x" : 0.5, "center_y" : 0.6}

        CButtonPrimary:
            text: "Primary Button"
            role: "Large Productive"
            pos_hint: {"center_x" : 0.5, "center_y" : 0.4}
            on_press: 
                self.icon = "add"

            '''
            return Builder.load_string(self.kvlang)

    if __name__ == "__main__":
        app = MyApp()
        app.run()

API
---

.. automodule:: carbonkivy.app
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
