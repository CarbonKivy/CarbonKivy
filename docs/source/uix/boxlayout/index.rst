.. _box-layout:

Box Layout
==========

.. rst-class:: lead

    The :class:`~carbonkivy.uix.boxlayout.boxlayout.CBoxLayout` class inherits from :class:`~kivy.uix.boxlayout.BoxLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.boxlayout.boxlayout.CBoxLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CBoxLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                BoxLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

API
---

.. automodule:: carbonkivy.uix.boxlayout.boxlayout
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
