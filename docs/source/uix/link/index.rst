.. _link:

Link
=====

.. rst-class:: lead

    Links are used as navigational elements. They navigate users to another location, such as a different site, resource, or section within the same page.

Overview
--------

.. figure:: /_static/images/link/carbondesignlinks.png
    :alt: Carbon Design Link
    :class: centered

    Carbon Design Links Overview

Links are used as navigational elements and can be used on their own or inline with text. They provide a lightweight option for navigation, but like other interactive elements, too many links will clutter a page and make it difficult for users to identify their next steps.

Live demo
---------

Click below links to test user interactivity.

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Default

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-link--default&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLink:
                url: "https://github.com/CarbonKivy"
                external: True # if true will open a webbrowser tab redirecting to the url provided.

                CLinkText:
                    text: "Link"

    .. tab-item:: Paired with Icon

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-link--paired-with-icon&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLink:
                url: "https://carbondesignsystem.com"
                external: True # if true will open a webbrowser tab redirecting to the url provided.

                CLinkText:
                    text: "Carbon Docs"

                CLinkIcon:
                    icon: "arrow--up-right"
                    font_size: plex_16

Size
----

There are three available size tokens for a link:

- Small
- Medium
- Large

Use the :class:`~carbonkivy.uix.link.link.CLink.role` property to define the token for the link size.

.. code-block:: kv

    CLink:
        url: "https://github.com/CarbonKivy"
        external: True # if true will open a webbrowser tab redirecting to the url provided.
        role: "Large" # Define the specific size token here (capitalized first letter of every word.)

        CLinkText:
            text: "CarbonKivy - Github"

Paired with Icon
~~~~~~~~~~~~~~~~

.. code-block:: kv

    CLink:
        url: "https://github.com/CarbonKivy"
        external: True # if true will open a webbrowser tab redirecting to the url provided.
        role: "Medium" # Define the specific size token here (capitalized first letter of every word.)

        CLinkText:
            text: "CarbonKivy - Github"

        CLinkIcon:
            icon: "logo--github"

Icon Only Link
--------------

    Additionally, CarbonKivy provides you with the ability to create an Icon Only Link.

.. code-block:: kv

    CLink:
        url: "https://github.com/CarbonKivy"
        external: True # if true will open a webbrowser tab redirecting to the url provided.
        role: "Medium" # Define the specific size token here (capitalized first letter of every word.)

        CLinkIcon:
            icon: "logo--github"

Styles
------

There are four default styles available for a link:

- active
- disabled
- normal
- visited

Use the :class:`~carbonkivy.uix.link.link.CLink.cstate` property to define the token for the link style.

.. code-block:: kv

    CLink:
        url: "https://github.com/CarbonKivy"
        external: True # if true will open a webbrowser tab redirecting to the url provided.
        role: "Medium" # Define the specific size token here (capitalized first letter of every word.)
        cstate: "visited"

        CLinkText:
            text: "CarbonKivy - Github"

        CLinkIcon:
            icon: "logo--github"

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

        CBoxLayout:
            orientation: "vertical"
            padding: dp(16)
            spacing: dp(128)
            adaptive: [True, True]
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            CLink:
                url: "https://github.com/CarbonKivy/CarbonKivy"
                external: True
                pos_hint: {"center_y": 0.6}

                CLinkText:
                    text: "Standalone Link"

                CLinkIcon:
                    icon: "arrow--up-right"

            CLink:
                url: "https://github.com/CarbonKivy/CarbonKivy"
                external: True
                cstate: "visited"
                pos_hint: {"center_y": 0.6}

                CLinkText:
                    text: "Standalone Link Visited"

                CLinkIcon:
                    icon: "arrow--up-right"

            CLink:
                url: "https://github.com/CarbonKivy/CarbonKivy"
                external: True
                cstate: "active"
                pos_hint: {"center_y": 0.6}

                CLinkText:
                    text: "Standalone Link Active"

                CLinkIcon:
                    icon: "arrow--up-right"

            CLink:
                url: "https://github.com/CarbonKivy/CarbonKivy"
                external: True
                cstate: "disabled"
                pos_hint: {"center_y": 0.6}

                CLinkText:
                    text: "Standalone Link Disabled"

                CLinkIcon:
                    icon: "arrow--up-right"

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

.. automodule:: carbonkivy.uix.link.link
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
