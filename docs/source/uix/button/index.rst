.. _button:

Button
======

.. rst-class:: lead

    Buttons are used to initialize an action. Button labels express what action will occur when the user interacts with it.

Overview
--------

.. figure:: /_static/images/button/carbondesignbuttons.png
    :alt: Carbon Design Button
    :class: centered

    Carbon Design Buttons Overview

Buttons are clickable elements that are used to trigger actions. They communicate calls to action to the user and allow users to interact with pages in a variety of ways. Button labels express what action will occur when the user interacts with it. 

By the latest CarbonKivy provides 3 types of button styles by default, however it holds the ability for developers to create thier own style customized buttons.

Live demo
---------

Click the below buttons to test user interactivity.

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Primary

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--default&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CButtonPrimary:
                text: "Button"
                role: "Large Productive"
                # icon: "add"

    .. tab-item:: Secondary

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--secondary&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CButtonSecondary:
                text: "Button"
                role: "Large Productive"
                # icon: "add"

    .. tab-item:: Ghost

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--ghost&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CButtonGhost:
                text: "Button"
                role: "Large Productive"
                # icon: "add"

    .. tab-item:: Tertiary

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--tertiary&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CButtonTertiary:
                text: "Button"
                role: "Large Productive"
                # icon: "add"

    .. tab-item:: Danger

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--danger&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CButtonDanger:
                text: "Button"
                variant: "Primary" # Primary (default), Tertiary, Ghost
                role: "Large Productive"
                # icon: "add"

Size
----

There are six available size tokens for a button:

- **Small**
- **Medium**
- **Large Productive**
- **Large Expressive**
- **Extra Large**
- **2XL**

The **Large Expressive** button is used in editorial and digital marketing experiences.

Use the :class:`~carbonkivy.uix.button.button.CButton.role` property to define the token for the button size.

.. code-block:: kv

    CButtonPrimary:
        text: "Button"
        role: "Extra Large" # Define the specific size token here (capitalized first letter of every word.)

.. figure:: /_static/images/button/button_sizes.png
    :alt: Carbon Design Button Sizes
    :class: centered

    Sizes of buttons in relation to its usage.

Custom Button
-------------

To create a custom button using the :class:`~carbonkivy.uix.button.button.CButton` you have certain properties and methods which needs to be customized.

The :class:`~carbonkivy.uix.button.button.CButton` class inherits certain behaviors to enable smooth user interactivity during different interactive states. It also holds some pre-defined properties like `padding`, `spacing`, `font_size`, `text_color`, `bg_color`, `inset_color`, `cstate`, etc.

Let's start with an example code:

.. code-block:: kv

    CButton:
        text: "Button"
        text_color: "blue_60"
        icon: "add"
        cstate: "normal" # active, disabled, normal
        pos_hint: {"center_x" : 0.5, "center_y" : 0.5}

Appearance of Button in different interactive states is shown below:

.. list-table::
    :widths: 50 50
    :align: center

    *   - .. figure:: /_static/images/button/cbuttonnormal.png

            normal

        - .. figure:: /_static/images/button/cbuttonhover.png

            hover

    *   - .. figure:: /_static/images/button/cbuttonfocus.png

            focus

        - .. figure:: /_static/images/button/cbuttondisabled.png

            disabled


To create an active state button you have to define the :class:`~carbonkivy.uix.button.button.CButton.active_color`, the color that appears when the button :class:`~kivy.uix.behaviors.ButtonBehavior.state` is :confval:`down`.

.. figure:: /_static/images/button/cbuttonactive.png
    :class: centered

    active

.. code-block:: kv

    CButton:
        text: "Button"
        icon: "add"
        active_color: app.button_primary_active
        cstate: "active" # active, disabled, normal
        pos_hint: {"center_x" : 0.5, "center_y" : 0.5}

----

Let's create a button similar to :class:`~carbonkivy.uix.button.button.CButtonPrimary` by defining the color properties by ourselves.

.. figure:: /_static/images/button/cbuttoncustom.png
    :class: centered

.. code-block:: kv

    <MyPrimaryButton@CButton>:
        bg_color: app.button_primary
        hover_color: app.button_primary_hover
        active_color: app.button_primary_active

    MyPrimaryButton:
        text: "My Primary Button"
        # cstate: "active" # active, disabled, normal (`default`)
        role: "2XL"
        icon: "add"
        pos_hint: {"center_x" : 0.5, "center_y" : 0.5}

Icon Button
-----------

To add icons to the button you have to define the :class:`~carbonkivy.uix.button.button.CButton.icon`, the icon that would appear at the specific slot aside the label or centralized in `Icon Only Buttons`.

.. figure:: /_static/images/button/primary/normal.png
    :class: centered

.. code-block:: kv

    CButtonPrimary:
        text: "Button"
        icon: "add"
        role: "Large Productive"
        icon: "add"

----

.. figure:: /_static/images/button/primary/iconnormal.png
    :class: centered

.. code-block:: kv

    CButtonPrimary:
        icon: "add"
        role: "Large Productive"
        spacing: 0

.. note::

    For an `Icon Only Button` you have to only define the :class:`~carbonkivy.uix.button.button.CButton.icon` property and set the button :class:`spacing` to **0** for centralized icon slot.

Example
-------

Run the below python script for a full-fledged running Example.

.. code-block:: python

    from kivy.core.window import Window
    from kivy.clock import Clock


    def set_softinput(*args) -> None:
        Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
        Window.softinput_mode = "below_target"


    Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

    appkv = """
    CScreen:

        CButtonPrimary:
            text: "Primary Button"
            role: "Large Productive"
            icon: "add"
            pos_hint: {'center_y': 0.9, 'center_x': 0.35}

        CButtonPrimary:
            icon: "add"
            role: "2XL"
            spacing: 0
            pos_hint: {'center_y': 0.9, 'center_x': 0.8}

        CButtonSecondary:
            text: "Secondary Button"
            role: "Large Productive"
            icon: "add"
            pos_hint: {'center_y': 0.7, 'center_x': 0.35}

        CButtonSecondary:
            icon: "add"
            role: "2XL"
            spacing: 0
            pos_hint: {'center_y': 0.7, 'center_x': 0.8}

        CButtonTertiary:
            text: "Tertiary Button"
            role: "Large Productive"
            icon: "add"
            pos_hint: {'center_y': 0.5, 'center_x': 0.35}

        CButtonTertiary:
            icon: "add"
            role: "2XL"
            spacing: 0
            pos_hint: {'center_y': 0.5, 'center_x': 0.8}

        CButtonGhost:
            text: "Ghost Button"
            role: "Large Productive"
            icon: "add"
            pos_hint: {'center_y': 0.3,  'center_x': 0.35}

        CButtonGhost:
            icon: "add"
            role: "2XL"
            spacing: 0
            pos_hint: {'center_y': 0.3, 'center_x': 0.8}

        CButtonDanger:
            text: "Danger Button"
            role: "Large Productive"
            icon: "add"
            pos_hint: {'center_y': 0.1,  'center_x': 0.35}

        CButtonDanger:
            icon: "add"
            role: "2XL"
            spacing: 0
            pos_hint: {'center_y': 0.1, 'center_x': 0.8}
    """

    from kivy.lang import Builder
    from carbonkivy.app import CarbonApp


    class myapp(CarbonApp):
        def __init__(self, *args, **kwargs):
            super(myapp, self).__init__(*args, **kwargs)

        def build(self, *args) -> None:
            screen = Builder.load_string(appkv)
            return screen


    if __name__ == "__main__":
        myapp().run()

API
---

.. automodule:: carbonkivy.uix.button.button
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
