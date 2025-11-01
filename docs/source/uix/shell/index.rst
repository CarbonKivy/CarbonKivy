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

    .. tab-item:: Header w/ sideNav

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-ui-shell-header--header-w-side-nav&amp;globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin" style="height: 35rem;"></iframe>

        .. code-block:: kv

            CScreen:

                UIShellLayout:

                    CScrollView:

                        CStackLayout:
                            adaptive: [False, True]
                            padding: dp(16)
                            spacing: dp(16)

                            CLabel:
                                style: "heading_06"
                                text: "Purpose and function"

                            CLabel:
                                markup: True
                                text: f"The shell is perhaps the most crucial piece of any UI built with [color=#0f62fe]Carbon[/color]. It contains the shared navigation framework for the entire design system and ties the products in IBM’s portfolio together in a cohesive and elegant way. The shell is the home of the topmost navigation, where users can quickly and dependably gain their bearings and move between pages.\n\nThe shell was designed with maximum flexibility built in, to serve the needs of a broad range of products and users. Adopting the shell ensures compliance with IBM design standards, simplifies development efforts, and provides great user experiences. All IBM products built with Carbon are required to use the shell’s header.\n\nTo better understand the purpose and function of the UI shell, consider the “shell” of MacOS, which contains the Apple menu, top-level navigation, and universal, OS-level controls at the top of the screen, as well as a universal dock along the bottom or side of the screen. The Carbon UI shell is roughly analogous in function to these parts of the Mac UI. For example, the app switcher portion of the shell can be compared to the dock in MacOS."

                UIShell:
                    id: left_panel_shell

                    UIShellLeftPanel:
                        panel_shell: left_panel_shell
                        visibility: shell_menu_btn.active

                        ScrollView:
                            do_scroll_x: False

                            UIShellPanelLayout:

                                UIShellPanelSelectionLayout:

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        default: True
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                UIShell:
                    id: header_shell

                    UIShellHeader:
                        id: shell_header

                        UIShellHeaderMenuButton:
                            id: shell_menu_btn

                        UIShellHeaderName:
                            markup: True
                            text: "[font=ibmplexsans]IBM[/font] [Platform]"

    .. tab-item:: Header w/ actions and right panel

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-ui-shell-header--header-w-actions-and-right-panel&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin" style="height: 35rem;"></iframe>

        .. code-block:: kv

            CScreen:

                UIShellLayout:

                    CScrollView:

                        CStackLayout:
                            adaptive: [False, True]
                            padding: dp(16)
                            spacing: dp(16)

                            CLabel:
                                style: "heading_06"
                                text: "Purpose and function"

                            CLabel:
                                markup: True
                                text: f"The shell is perhaps the most crucial piece of any UI built with [color=#0f62fe]Carbon[/color]. It contains the shared navigation framework for the entire design system and ties the products in IBM’s portfolio together in a cohesive and elegant way. The shell is the home of the topmost navigation, where users can quickly and dependably gain their bearings and move between pages.\n\nThe shell was designed with maximum flexibility built in, to serve the needs of a broad range of products and users. Adopting the shell ensures compliance with IBM design standards, simplifies development efforts, and provides great user experiences. All IBM products built with Carbon are required to use the shell’s header.\n\nTo better understand the purpose and function of the UI shell, consider the “shell” of MacOS, which contains the Apple menu, top-level navigation, and universal, OS-level controls at the top of the screen, as well as a universal dock along the bottom or side of the screen. The Carbon UI shell is roughly analogous in function to these parts of the Mac UI. For example, the app switcher portion of the shell can be compared to the dock in MacOS."

                UIShell:
                    id: right_panel_shell

                    UIShellRightPanel:
                        panel_shell: right_panel_shell
                        visibility: shell_notification_btn.focus

                UIShell:
                    id: header_shell

                    UIShellHeader:
                        id: shell_header

                        UIShellHeaderName:
                            markup: True
                            text: "[font=ibmplexsans]IBM[/font] [Platform]"

                        CAnchorLayout:
                            anchor_x: "right"

                            CGridLayout:
                                adaptive: [True, True]
                                rows: 1

                                UIShellButton:
                                    id: shell_search_btn
                                    icon: "search"

                                UIShellButton:
                                    id: shell_notification_btn
                                    icon: "notification"

                                UIShellButton:
                                    id: shell_switcher_btn
                                    icon: "switcher"

    .. tab-item:: Header w/ navigation and actions

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-ui-shell-header--header-w-navigation-and-actions&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin" style="height: 35rem;"></iframe>

        .. code-block:: kv

            CScreen:

                UIShellLayout:

                    CScrollView:

                        CStackLayout:
                            adaptive: [False, True]
                            padding: dp(16)
                            spacing: dp(16)

                            CLabel:
                                style: "heading_06"
                                text: "Purpose and function"

                            CLabel:
                                markup: True
                                text: f"The shell is perhaps the most crucial piece of any UI built with [color=#0f62fe]Carbon[/color]. It contains the shared navigation framework for the entire design system and ties the products in IBM’s portfolio together in a cohesive and elegant way. The shell is the home of the topmost navigation, where users can quickly and dependably gain their bearings and move between pages.\n\nThe shell was designed with maximum flexibility built in, to serve the needs of a broad range of products and users. Adopting the shell ensures compliance with IBM design standards, simplifies development efforts, and provides great user experiences. All IBM products built with Carbon are required to use the shell’s header.\n\nTo better understand the purpose and function of the UI shell, consider the “shell” of MacOS, which contains the Apple menu, top-level navigation, and universal, OS-level controls at the top of the screen, as well as a universal dock along the bottom or side of the screen. The Carbon UI shell is roughly analogous in function to these parts of the Mac UI. For example, the app switcher portion of the shell can be compared to the dock in MacOS."

                UIShell:
                    id: left_panel_shell

                    UIShellLeftPanel:
                        panel_shell: left_panel_shell
                        visibility: shell_menu_btn.active

                        ScrollView:
                            do_scroll_x: False

                            UIShellPanelLayout:

                                UIShellPanelSelectionLayout:

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        default: True
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                UIShell:
                    id: right_panel_shell

                    UIShellRightPanel:
                        panel_shell: right_panel_shell
                        visibility: shell_notification_btn.focus

                UIShell:
                    id: header_shell

                    UIShellHeader:
                        id: shell_header

                        UIShellHeaderMenuButton:
                            id: shell_menu_btn

                        UIShellHeaderName:
                            markup: True
                            text: "[font=ibmplexsans]IBM[/font] [Platform]"

                        CAnchorLayout:
                            anchor_x: "right"

                            CGridLayout:
                                adaptive: [True, True]
                                rows: 1

                                UIShellButton:
                                    id: shell_search_btn
                                    icon: "search"

                                UIShellButton:
                                    id: shell_notification_btn
                                    icon: "notification"

                                UIShellButton:
                                    id: shell_switcher_btn
                                    icon: "switcher"

Individual components
---------------------

The class :class:`~carbonkivy.uix.shell.shell.UIShell` inherits from the class :class:`~carbonkivy.uix.stacklayout.stacklayout.CStackLayout` and holds different individual components.

UI shell header
~~~~~~~~~~~~~~~

The UI shell header serves as the primary navigation and orientation element for users within the interface. It can function independently or be integrated with the UI shell's left and right panels to support more advanced navigation scenarios.

UI shell left panel
~~~~~~~~~~~~~~~~~~~

The left panel contains secondary navigation and is positioned below the header and fixed to the left. Both links and sub-menus can be used in the side-nav and may be mixed together.

UI shell right panel
~~~~~~~~~~~~~~~~~~~~

The right panel is invoked by icons on the right side of the header, and remains anchored to that icon. Right panels have a consistent width, span the full height of the viewport, and are flush to the right edge of the viewport.

Example
~~~~~~~

.. tab-set::

    .. tab-item:: python

        .. code-block:: python

                from kivy.clock import Clock
                from kivy.core.window import Window


                def set_softinput(*args) -> None:
                    Window.keyboard_anim_args = {"d": 0.2, "t": "in_out_expo"}
                    Window.softinput_mode = "below_target"


                Window.on_restore(Clock.schedule_once(set_softinput, 0.1))

                from carbonkivy.app import CarbonApp
                from carbonkivy.uix.screen import CScreen
                from carbonkivy.uix.screenmanager import CScreenManager


                class UI(CScreenManager):
                    pass


                class HomeScreen(CScreen):
                    pass


                class myapp(CarbonApp):
                    def __init__(self, *args, **kwargs) -> None:
                        super(myapp, self).__init__(*args, **kwargs)
                        self.load_all_kv_files(self.directory)

                    def build(self) -> UI:
                        self.manager_screens = UI()
                        self.manager_screens.add_widget(HomeScreen(name="home"))
                        return self.manager_screens


                if __name__ == "__main__":
                    myapp().run()

    .. tab-item:: kvlang

        .. code-block:: kv

            <HomeScreen>:

                UIShellLayout:

                    CScrollView:

                        CStackLayout:
                            adaptive: [False, True]
                            padding: dp(16)
                            spacing: dp(16)

                            CLabel:
                                style: "heading_06"
                                text: "Purpose and function"

                            CLabel:
                                markup: True
                                text: f"The shell is perhaps the most crucial piece of any UI built with [color=#0f62fe]Carbon[/color]. It contains the shared navigation framework for the entire design system and ties the products in IBM’s portfolio together in a cohesive and elegant way. The shell is the home of the topmost navigation, where users can quickly and dependably gain their bearings and move between pages.\n\nThe shell was designed with maximum flexibility built in, to serve the needs of a broad range of products and users. Adopting the shell ensures compliance with IBM design standards, simplifies development efforts, and provides great user experiences. All IBM products built with Carbon are required to use the shell’s header.\n\nTo better understand the purpose and function of the UI shell, consider the “shell” of MacOS, which contains the Apple menu, top-level navigation, and universal, OS-level controls at the top of the screen, as well as a universal dock along the bottom or side of the screen. The Carbon UI shell is roughly analogous in function to these parts of the Mac UI. For example, the app switcher portion of the shell can be compared to the dock in MacOS."

                UIShell:
                    id: left_panel_shell

                    UIShellLeftPanel:
                        panel_shell: left_panel_shell
                        visibility: shell_menu_btn.active

                        ScrollView:
                            do_scroll_x: False

                            UIShellPanelLayout:

                                UIShellPanelSelectionLayout:

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        default: True
                                        text: "Category title"
                                        left_icon: "incomplete"
                                        right_icon: "chevron--down"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                                    UIShellPanelSelectionItem:
                                        text: "Link"
                                        left_icon: "incomplete"

                UIShell:
                    id: right_panel_shell

                    UIShellRightPanel:
                        panel_shell: right_panel_shell
                        visibility: shell_notification_btn.focus

                UIShell:
                    id: header_shell

                    UIShellHeader:
                        id: shell_header

                        UIShellHeaderMenuButton:
                            id: shell_menu_btn

                        UIShellHeaderName:
                            markup: True
                            text: "[font=ibmplexsans]IBM[/font] [Platform]"

                        CAnchorLayout:
                            anchor_x: "right"

                            CGridLayout:
                                adaptive: [True, True]
                                rows: 1

                                UIShellButton:
                                    id: shell_search_btn
                                    icon: "search"

                                UIShellButton:
                                    id: shell_notification_btn
                                    icon: "notification"

                                UIShellButton:
                                    id: shell_switcher_btn
                                    icon: "switcher"

API
---

.. automodule:: carbonkivy.uix.shell.shell
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
