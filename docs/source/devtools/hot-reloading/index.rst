.. _hot-reloading:

Hot Reloading
=============

CarbonKivy provides you with a utitlity class :class:`~carbonkivy.devtools.LiveApp` that integrates hot-reloading system to the app.

    Currently supports reloading of kvlang files only.

This module requires `Kaki <https://github.com/tito/kaki>`_ library.

.. code-block:: bash

    pip install kaki

Usage
-----

Inherit from the class :class:`~carbonkivy.devtools.LiveApp`, and use the :class:`build_app` function to construct your app. Within this function, initialize and return the main class (e.g., :class:`ScreenManager`, :class:`Screen`) for your application.

.. note:: 

    Do not manually load .kv files when using hot reload. The system will automatically watch all .kv files within the root directory of the app and its subdirectories, and load them at runtime.

Below is a minimal example of hot reload. Try modifying the properties of the widgets and save the file to see the changes in real-time.

.. tab-set::

    .. tab-item:: python

        .. code-block:: python

            from carbonkivy.app import CarbonApp
            from carbonkivy.devtools import LiveApp # importing live app utility
            from carbonkivy.uix.screenmanager import CScreenManager


            class UI(CScreenManager):
                pass


            class myapp(CarbonApp, LiveApp): # inheritance from LiveApp

                def __init__(self, *args, **kwargs) -> None:
                    super(myapp, self).__init__(*args, **kwargs)

                def build_app(self) -> UI:
                    self.manager_screens = UI() # initialization in build_app
                    return self.manager_screens


            if __name__ == "__main__":
                app = myapp()
                app.run()

    .. tab-item:: kvlang

        .. code-block:: kv

            <UI>:
                HomeScreen:
                    name: "home"

            <HomeScreen@CScreen>:

                CBoxLayout:
                    orientation: "vertical"
                    padding: dp(16)
                    spacing: dp(128)
                    adaptive: [True, True]
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    CLink:
                        url: "https://github.com/CarbonKivy/CarbonKivy"
                        external: True
                        pos_hint: {"center_y": 0.6}

                        CLinkText:
                            text: "Standalone Link"

                        CLinkIcon:
                            icon: "arrow--up-right"

                    CLink:
                        url: "https://github.com/CarbonKivy/CarbonKivy"
                        external: True
                        cstate: "visited"
                        pos_hint: {"center_y": 0.6}

                        CLinkText:
                            text: "Standalone Link Visited"

                        CLinkIcon:
                            icon: "arrow--up-right"

                    CLink:
                        url: "https://github.com/CarbonKivy/CarbonKivy"
                        external: True
                        cstate: "active"
                        pos_hint: {"center_y": 0.6}

                        CLinkText:
                            text: "Standalone Link Active"

                        CLinkIcon:
                            icon: "arrow--up-right"

                    CLink:
                        url: "https://github.com/CarbonKivy/CarbonKivy"
                        external: True
                        cstate: "disabled"
                        pos_hint: {"center_y": 0.6}

                        CLinkText:
                            text: "Standalone Link Disabled"

                        CLinkIcon:
                            icon: "arrow--up-right"
