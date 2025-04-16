.. _float-layout:

Float Layout
============

.. rst-class:: lead

    The :class:`~carbonkivy.uix.floatlayout.floatlayout.CFloatLayout` class inherits from :class:`~kivy.uix.floatlayout.FloatLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.floatlayout.floatlayout.CFloatLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CFloatLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                FloatLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

API
---

.. automodule:: carbonkivy.uix.floatlayout.floatlayout
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
