.. Button:

Button
======

.. rst-class:: lead

  Buttons are used to initialize an action. Button labels express what action will occur when the user interacts with it.

.. image:: /_static/images/button/carbondesignbutton.png
   :alt: Carbon Design Button
   :class: centered

Overview
--------

Buttons are clickable elements that are used to trigger actions. They communicate calls to action to the user and allow users to interact with pages in a variety of ways. Button labels express what action will occur when the user interacts with it. 

By the latest CarbonKivy provides 3 types of button styles by default, however it holds the ability for developers to create thier own style customized buttons.

Live demo
---------

Click the below buttons to test user interactivity.

.. tab-set::

   .. tab-item:: Primary

      .. raw:: html

         <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--default&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

      .. code-block:: kv

         CButtonPrimary:
            text: "Button"
            role: "Large Productive"

   .. tab-item:: Secondary

      .. raw:: html

         <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--secondary&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

      .. code-block:: kv

         CButtonSecondary:
            text: "Button"
            role: "Large Productive"
   
   .. tab-item:: Ghost

      .. raw:: html

         <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-button--ghost&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

      .. code-block:: kv

         CButtonGhost:
            text: "Button"
            role: "Large Productive"

Size
----

There are six button sizes: small, medium, large productive, large expressive, extra large, and 2XL. The large expressive button is used in editorial and digital marketing experiences.

Use the :confval:`role:` property to defined the token for the button size.

.. code-block:: kv

   CButtonPrimary:
      text: "Button"
      role: "Extra Large" # Define the specific size token here (capitalized first letter of every word.)

.. image:: /_static/images/button/button_sizes.png
   :alt: Carbon Design Button Sizes
   :class: centered

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
   Screen:

      CButtonPrimary:
         text: "Primary Button"
         role: "Large Productive"
         icon: "add"
         pos_hint: {'center_y': 0.8, 'center_x': 0.35}

      CButtonPrimary:
         icon: "add"
         role: "2XL"
         spacing: 0
         pos_hint: {'center_y': 0.8, 'center_x': 0.8}

      CButtonSecondary:
         text: "Secondary Button"
         role: "Large Productive"
         icon: "add"
         pos_hint: {'center_y': 0.6, 'center_x': 0.35}

      CButtonSecondary:
         icon: "add"
         role: "2XL"
         spacing: 0
         pos_hint: {'center_y': 0.6, 'center_x': 0.8}

      CButtonGhost:
         text: "Ghost Button"
         role: "Large Productive"
         pos_hint: {'center_y': 0.4,  'center_x': 0.35}
         on_press:
               self.icon = "add"

      CButtonGhost:
         icon: "add"
         role: "2XL"
         spacing: 0
         pos_hint: {'center_y': 0.4, 'center_x': 0.8}

      CButton:
         text: "Custom Ghost Button"
         text_color: app.link_primary
         _bg_color: app.transparent
         bg_color: app.transparent
         active_color: app.transparent
         line_color: app.focus
         hover_color: app.background_hover
         role: "Large Productive"
         inset_width: 0
         pos_hint: {'center_y': 0.2, 'center_x': 0.5}
         on_press:
               self.icon = "add"

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

.. autoapimodule:: carbonkivy.uix.button
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

