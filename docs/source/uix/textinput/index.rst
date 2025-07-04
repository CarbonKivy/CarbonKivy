.. _text-inputs::

Text inputs
===========

.. rst-class:: lead

    Text inputs enable users to enter free-form text data. You can use them for long and short-form entries.

Overview
--------

.. figure:: /_static/images/textinput/carbondesigntextinputs.png
    :class: centered

Text inputs enable users to enter free-form text data. The type of text field used should reflect the length of the content you expect the user to enter. The default text input is for short, one-line content, whereas text area is for longer, multi-line entries.

*Only default variant of CTextInput is available.*

Live demo
---------

Click below text inputs to test user interactivity.

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Default

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-textinput--default&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CTextInputLayout:

                CTextInput:
                    hint_text: "Placeholder text"

                CTextInputLabel:
                    text: "Label text"

                CTextInputHelperText:
                    text: "Helper text"

Example
-------

Run below code for a full-fledged running example.

.. code-block:: python

    from kivy.clock import Clock
    from kivy.core.window import Window


    def set_softinput(*args) -> None:
        Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
        Window.softinput_mode = "below_target"


    Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

    appkv = """
    CScreen:

        CTextInputLayout:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint_x: None
            width: dp(300)

            CTextInput:
                hint_text: "Placeholder text"

            CTextInputLabel:
                text: "Label text"

            CTextInputHelperText:
                text: "Helper text"

            CTextInputTrailingIconButton:
                icon: "error"
                spacing: 0

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

.. automodule:: carbonkivy.uix.textinput.textinput
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
