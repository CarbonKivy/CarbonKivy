.. _relative-layout:

Relative Layout
===============

.. rst-class:: lead

    The :class:`~carbonkivy.uix.relativelayout.relativelayout.CRelativeLayout` class inherits from :class:`~kivy.uix.relativelayout.RelativeLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.relativelayout.relativelayout.CRelativeLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CRelativeLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                RelativeLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

API
---

.. automodule:: carbonkivy.uix.relativelayout.relativelayout
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
