.. _grid-layout:

Grid Layout
============

.. rst-class:: lead

    The :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout` class inherits from :class:`~kivy.uix.gridlayout.GridLayout` and extends its functionality by introducing additional properties.

For instance, let's see an example of how :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout` enhances control of `background color` compared to standard one.


.. tab-set::

    .. tab-item:: CarbonKivy

            .. code-block:: kv

                CGridLayout:
                    bg_color: app.background_hover

    .. tab-item:: Kivy

            .. code-block:: kv

                GridLayout:
                    canvas.before:
                        Color:
                            rgba: app.background_hover
                        SmoothRectangle:
                            pos: self.pos
                            size: self.size

Responsive Behavior
-------------------

.. figure:: /_static/gif/cgrid.gif
    :class: centered

Use the :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.responsive` property to enable or disable the responsive behavior of the layout.

There are three tokens for responsive attribute:

- cols
- rows
- both

Use the :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.responsive_attr` property to define the responsive attribute for the responsive behavior of the layout.

Usage
~~~~~

With any responsive attribute you have access to its minimum and maximum values.

- :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.min_cols`
- :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.max_cols`
- :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.min_rows`
- :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.max_rows`


Scaling - Breakpoints
~~~~~~~~~~~~~~~~~~~~~

Use the :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.scale_width` and :class:`~carbonkivy.uix.gridlayout.gridlayout.CGridLayout.scale_height` properties to define the breakpoints for the responsive behavior of the layout.

Example
-------

Let's take an example of a grid layout with minimum columns `2`, maximum columns `4` and responsive attribute as :confval:`cols` `(default)` with a breakpoint of :confval:`dp(200)`.

.. code-block:: kv

    CGridLayout:
        responsive: True
        min_cols: 2
        cols: 2 # default number of cols on start
        max_cols: 4
        scale_width: dp(200)
        adaptive: [False, True]

        CBoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: dp(300)
            bg_color: app.interactive

        CBoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: dp(300)
            bg_color: app.interactive

        CBoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: dp(300)
            bg_color: app.interactive

        CBoxLayout:
            orientation: 'vertical'
            size_hint: 1, None
            height: dp(300)
            bg_color: app.interactive

API
---

.. automodule:: carbonkivy.uix.gridlayout.gridlayout
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
