.. _loading:

Loading
=======

.. rst-class:: lead

    Loading indicators are used when retrieving data or performing slow computations and help notify users that a process is underway.

Overview
--------

.. figure:: /_static/images/loading/loadingusage.png
    :class: centered

    Example of the loading component in a UI

The loading component provides visual feedback indicating a process or action is in progress. It helps set users’ expectations during wait times by signaling that the system is working behind the scenes. Depending on the context, it can be used as a full-page overlay or placed within a specific section or UI element. Use a loading indicator if the expected wait time exceeds three seconds.

Live demo
---------

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Large

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-loading--default&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLoadingIndicator:
                role: "Large"

    .. tab-item:: Small

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?globals=theme:white&args=small:!true&id=components-loading--default" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLoadingIndicator:
                role: "Small"

    .. tab-item:: With overlay

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?globals=theme:white&args=withOverlay:!true&id=components-loading--default" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLoadingLayout:
                CLoadingIndicator:
                    role: "Large"

Size
----

There are two available size tokens for a loading indicator:

- Large
- Small

Use the :class:`~carbonkivy.uix.loading.loading.CLoadingIndicator.role` property to define the token for the loding indicator size.

.. code-block:: kv

    CLoadingIndicator:
        role: "small"

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

        GridLayout:
            size_hint: 1, 1
            cols: 1
            padding: dp(16)

            AnchorLayout:

                CLoadingIndicator:
                    role: "Large"

            AnchorLayout:

                CLoadingIndicator:
                    role: "Small"

            CFloatLayout:
                size_hint_x: 1

                CLabel:
                    text: "Overlay"
                    halign: "center"
                    pos_hint: {"center_y": 0.5, "center_x": 0.5}
                    style: "heading_05"

                CLoadingLayout:
                    pos_hint: {"center_y": 0.5, "center_x": 0.5}
                    CLoadingIndicator:
                        role: "Large"
    """

    from kivy.lang import Builder

    from carbonkivy.app import CarbonApp
    from carbonkivy.uix.screen import CScreen


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

.. automodule:: carbonkivy.uix.loading.loading
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
