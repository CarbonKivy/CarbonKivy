.. _tooltip:

Tooltip
===========

.. rst-class:: lead

    Tooltips display additional information upon hover or focus that is contextual, helpful, and nonessential while providing the ability to communicate and give clarity to a user.

Overview
--------

A tooltip is embedded within other components rather than being used as a standalone component. Since tooltips are embedded within other components, there’s no need to include them again. They provide additional information when a user hovers over or focuses on a UI element and should only be used when necessary to offer quick context without cluttering the interface.

*Only vertical variant of CTooltip is available.*

Live demo
---------

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Default

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-tooltip--default&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: python

            ...

            from carbonkivy.behaviors import TooltipBehavior
            from carbonkivy.uix.link import CLink
            from carbonkivy.uix.tooltip import CTooltip


            class TooltipLink(CLink, TooltipBehavior):
                def __init__(self, **kwargs) -> None:
                    super().__init__(**kwargs)
                    self.tooltip = CTooltip(text="This is a tooltip.")

            kvlang = """
            CScreen:
                TooltipLink:
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    CLinkIcon:
                        icon: "Occasionally, services are updated in a specified time window to ensure no down time for customers."
            """

            ...

API
---

.. automodule:: carbonkivy.uix.tooltip.tooltip
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:

