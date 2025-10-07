.. _ui-shell:

UI Shell
========

.. rst-class:: lead

    A shell is a collection of components shared by all products within a platform. It provides a common set of interaction patterns that persist between and across products.

Overview
--------

.. figure:: /_static/images/shell/carbondesignshell.png
    :alt: Carbon Design UI Shell
    :class: centered

    Carbon Design UI Shell Overview

The UI shell consists of three modular components: the header, the left panel, and the right panel. Each component can be used on its own, but they are designed to work seamlessly together, providing a consistent and flexible user experience across different products and platforms.

Live demo
---------

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Header w/ Navigation Actions and Side Nav

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-ui-shell-header--header-w-navigation-actions-and-side-nav&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin" style="height: 35rem;"></iframe>

        .. code-block:: kv

            MDScreen:

                UIShell:
                    id: left_panel_shell

                    UIShellLeftPanel:
                        panel_shell: left_panel_shell
                        visibility: shell_menu_btn.active

                        UIShellPanelLayout:

                            UIShellPanelSelectionLayout:

                                UIShellPanelSelectionItem:
                                    default: True
                                    text: "Home"
                                    right_icon: "home"
                                    left_icon: "incomplete"

                                UIShellPanelSelectionItem:
                                    text: "Profile"
                                    right_icon: "account"
                                    left_icon: "incomplete"

                UIShell:
                    id: shell

                    UIShellHeader:
                        id: shell_header

                        UIShellHeaderMenuButton:
                            id: shell_menu_btn

                        UIShellHeaderName:
                            text: "Header name"

                        CAnchorLayout:
                            anchor_x: "right"

                            CGridLayout:
                                adaptive: [True, True]
                                rows: 1

                                UIShellButton:
                                    icon: "search"

                                UIShellButton:
                                    icon: "notification"

                                UIShellButton:
                                    icon: "switcher"

.. Individual components
.. ---------------------

.. The :class:`~carbonkivy.uix.shell.UIShell` inherits from :class:`~carbonkivy.uix.stacklayout.CStackLayout` holds different individual components.

.. UI shell header
.. ~~~~~~~~~~~~~~~

.. The UI shell header serves as the primary navigation and orientation element for users within the interface. It can function independently or be integrated with the UI shell's left and right panels to support more advanced navigation scenarios.

.. Let us explore different scenarios available for the ui shell header.

.. 1. default



API
---

.. automodule:: carbonkivy.uix.shell.shell
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
