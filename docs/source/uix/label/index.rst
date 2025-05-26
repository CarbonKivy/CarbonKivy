.. _label:

Label
=====

.. rst-class:: lead

	Labels are used to display text in Kivy's interface.

Overview
--------

.. figure:: /_static/images/label/carbondesignlabels.png
    :alt: Carbon Design Label
    :class: centered

    Carbon Design Labels Overview

The :class:`~kivy.uix.label.Label` widget is used to display non-editable text in a Kivy application. It is primarily employed for presenting static content such as titles, descriptions, instructions, messages, and status indicators throughout the user interface.

The :class:`~carbonkivy.uix.label.label.CLabel` class extends the functionality of :class:`~kivy.uix.label.Label` by introducing additional properties aligned with the Carbon Design System. These enhancements enable consistent typography, styling, and sizing based on the **IBM Plex** typeface, ensuring a cohesive and modern visual experience.

Typeface: IBM Plex
------------------

Carbon uses the open-source typeface IBM Plex. IBM Plex can be accessed and downloaded from the `Plex GitHub Repo <https://github.com/ibm/plex>`_.

CarbonKivy provides you with three available typefaces:

- IBM Plex Sans
- IBM Plex Serif
- IBM Plex Mono

Use the :class:`~carbonkivy.uix.label.label.CLabel.typeface` property to define the token for the typeface.

.. code-block:: kv

    CScreen:

        CLabel:
            text: "IBM Plex Sans"
            typeface: "IBM Plex Sans"
            halign: "center"
            pos_hint: {"center_y": 0.8}

        CLabel:
            text: "IBM Plex Serif"
            typeface: "IBM Plex Serif"
            halign: "center"
            pos_hint: {"center_y": 0.5}

        CLabel:
            text: "IBM Plex Mono"
            typeface: "IBM Plex Mono"
            halign: "center"
            pos_hint: {"center_y": 0.2}

Style
-----

Typography creates purposeful texture, guiding users to read and understand the hierarchy of information. The right typographic treatment and the controlled usage of type styles helps manage the display of content, keeping it useful, simple, and effective.

Type Sets
~~~~~~~~~

Carbon uses a clear naming approach and type tokens to manage typography across complex and layered layouts and patterns, and these tokens sit within two type sets: expressive and productive.

- Productive styles are named with a suffix of :confval:`_01`. e.g. :confval:`body_01`, :confval:`label_01`.
- Expressive styles are named with a suffix of :confval:`_02`. e.g. :confval:`body_02`, :confval:`label_02`.

Use the :class:`~carbonkivy.uix.label.label.CLabel.style` property to define the token for the font style.

For a complete list of available type tokens refer the below link.

.. note::

    All style tokens are used in `Snake case <https://en.wikipedia.org/wiki/Snake_case>`_ style, in small letters.

.. seealso::

    `Type Sets <https://carbondesignsystem.com/elements/typography/type-sets/>`_

.. code-block:: kv

    CLabel:
        text: "IBM Plex Sans"
        typeface: "IBM Plex Sans"
        style: "heading_04"
        halign: "center"
        pos_hint: {"center_y": 0.8}

Weights
~~~~~~~

There are 14 available weight style tokens:

- Bold
- BoldItalic
- ExtraLight
- ExtraLightItalic
- Italic
- Light
- LightItalic
- Medium
- MediumItalic
- Regular
- SemiBold
- SemiBoldItalic
- Thin
- ThinItalic

Use the :class:`~carbonkivy.uix.label.label.CLabel.weight_style` property to define the token for the weight style.

.. code-block:: kv

    CLabel:
        text: "IBM Plex Sans"
        typeface: "IBM Plex Sans"
        style: "heading_04"
        weight_style: "Medium"
        halign: "center"
        pos_hint: {"center_y": 0.8}

Size (Scale)
------------

    Font sizes and line heights are attained dynamically based on the style of the label.

You have the priviledge to change the :confval:`font_size` any time.
CarbonKivy provides you with 18 size tokens that can be accessed as variables in kvlang.

- plex_12
- plex_14
- plex_16
- plex_18
- plex_20
- plex_24
- plex_28
- plex_32
- plex_36
- plex_42
- plex_48
- plex_54
- plex_60
- plex_68
- plex_76
- plex_84
- plex_92


.. code-block:: kv

    CLabel:
        text: "IBM Plex Sans"
        typeface: "IBM Plex Sans"
        weight_style: "Medium"
        font_size: plex_14
        halign: "center"
        pos_hint: {"center_y": 0.8}

API
---

.. automodule:: carbonkivy.uix.label.label
    :members:
    :undoc-members:
    :show-inheritance:
    :no-index:
