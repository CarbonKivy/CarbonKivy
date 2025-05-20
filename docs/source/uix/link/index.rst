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

        CLinkIcon:
            icon: "logo--github"

API
---

.. automodule:: carbonkivy.uix.link.link
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
