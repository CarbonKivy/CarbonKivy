.. _notification:

Notification
============

.. rst-class:: lead

    Notifications are messages that communicate information to the user.

Overview
--------

Low contrast
~~~~~~~~~~~~

.. figure:: /_static/images/notification/notification-style-low-contrast.png
    :alt: Carbon Design Notification
    :class: centered

High contrast
~~~~~~~~~~~~~

    Under Development

.. figure:: /_static/images/notification/notification-style-high-contrast.png
    :alt: Carbon Design Notification
    :class: centered

Notifications provide a method for communicating with users and sharing feedback. They come in four statuses which when combined with the right variants make notifications that are relevant, timely, and informative for each use case. Their status signifies the purpose of the information being conveyed and allow you to tailor the disruptiveness of the notification to the specific situation.

Live demo
---------

.. note::

    This live demo contains only a preview of functionality and styles available for this component. Actual widgets may not show the exact same behavior but similar to expected.

.. tab-set::

    .. tab-item:: Toast High Contrast

        .. raw:: html

            <iframe title="Component demo" class="StorybookDemo-module--iframe--dc8d2" src="https://react.carbondesignsystem.com/iframe.html?id=components-notifications-toast--default&globals=theme:white" frameborder="no" sandbox="allow-forms allow-scripts allow-same-origin"></iframe>

        .. code-block:: python

            # only low-contrast notification is available.

            CNotificationToast:
                status: "Error"
                title: "Notification title"
                subtitle: "Subtitle text goes here"
                time_caption_enabled: True

Status
------

There are four available status tokens for a notification:

- Error
- Info
- Success
- Warning

Use the :class:`~carbonkivy.uix.notification.notification.CBaseNotification.status` property to define the token for the notification status.

.. code-block:: python

    def notify_error(self, *args) -> None:
        self.notification = CNotificationToast(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
                time_caption_enabled=True,
            ).open()

Variant
-------

Two variants for notification are available:

- Inline
- Toast

You have three classes for creating a notification of different variants.

- :class:`~carbonkivy.uix.notification.notification.CNotification`
- :class:`~carbonkivy.uix.notification.notification.CNotificationInline`
- :class:`~carbonkivy.uix.notification.notification.CNotificationToast`

:class:`~carbonkivy.uix.notification.notification.CNotification`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It serves as a dynamic class for interchanging between variants :class:`Inline` and :class:`Toast` in real time whenever required.

Use the :class:`~carbonkivy.uix.notification.notification.CNotification.variant` property to define the token for the notification variant.

.. code-block:: python

    def notify_error(self, *args) -> None:
        self.notification = CNotification(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
                time_caption_enabled=True,
                variant="Toast"
            ).open()

:class:`~carbonkivy.uix.notification.notification.CNotificationInline`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inline notifications show up in task flows to notify users of the status of an action or system. Inline notifications usually appear at the top of the primary content area or close to the item needing attention

.. code-block:: python

    def notify_error(self, *args) -> None:
        self.notification = CNotificationInline(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
            ).open()

:class:`~carbonkivy.uix.notification.notification.CNotificationToast`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toast notifications are non-modal, time-based window elements used to display short messages; they usually appear at the top of the screen and disappear after a few seconds.

.. code-block:: python

    def notify_error(self, *args) -> None:
        self.notification = CNotificationToast(
                title="Server instance unavailable",
                subtitle="The server instance is no longer running because of an error.",
                status="Error",
                time_caption_enabled=True,
            ).open()

Actionable
----------

Actionable notifications are inline or toast notifications that have interactive elements. Only one action is allowed for each notification, and this action frequently takes users to a flow or page related to the message where they can resolve the notification.

Use the :class:`~carbonkivy.uix.notification.notification.CBaseNotification.action_button` property to define the actionable element for the notification.

    Actionable element must inherit from :class:`~kivy.uix.behaviors.ButtonBehavior`.

.. code-block:: python

    from carbonkivy.uix.button import CButtonPrimary

    def notify_info(self, *args) -> None:
        self.notification = CNotificationToast(
                title="Server instance updated",
                subtitle="The server instance location has been updated.",
                status="Info",
                action_button=CButtonPrimary(
                    text="View Server",
                    on_press=self.resolve_notification()
                )
            ).open()

    def resolve_notification(self, *args) -> None:
        print("Resolved.")

Example
-------

.. seealso::

    `Notification Example - Github <https://github.com/CarbonKivy/CarbonKivy/tree/master/examples/Notification>`_

API
---

.. automodule:: carbonkivy.uix.notification.notification
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
