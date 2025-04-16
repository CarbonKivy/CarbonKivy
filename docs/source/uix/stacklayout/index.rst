.. _stack-layout:

Stack Layout
============

.. rst-class:: lead

    The :class:`~carbonkivy.uix.stacklayout.stacklayout.CStackLayout` class inherits from :class:`~kivy.uix.stacklayout.StackLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.stacklayout.stacklayout.CStackLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CStackLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                StackLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

API
---

.. automodule:: carbonkivy.uix.stacklayout.stacklayout
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
