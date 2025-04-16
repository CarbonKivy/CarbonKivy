.. _anchor-layout:

Anchor Layout
=============

.. rst-class:: lead

    The :class:`~carbonkivy.uix.anchorlayout.anchorlayout.CAnchorLayout` class inherits from :class:`~kivy.uix.anchorlayout.AnchorLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.anchorlayout.anchorlayout.CAnchorLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CAnchorLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                AnchorLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

API
---

.. automodule:: carbonkivy.uix.anchorlayout.anchorlayout
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
