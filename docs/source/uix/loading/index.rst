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

API
---

.. automodule:: carbonkivy.uix.loading.loading
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
