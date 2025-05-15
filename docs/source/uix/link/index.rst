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
                text: "Link"
                url: "https://github.com/CarbonKivy"
                external: True # if true will open a webbrowser tab redirecting to the url provided.

    .. tab-item:: Paired with Icon

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-link--paired-with-icon&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: kv

            CLink:
                text: "Carbon Docs"
                url: "https://carbondesignsystem.com"
                external: True # if true will open a webbrowser tab redirecting to the url provided.

                CLinkIcon:
                    icon: "arrow--up-right"
                    font_size: plex_16

API
---

.. automodule:: carbonkivy.uix.button.button
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
