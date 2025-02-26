from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import hex_colormap

from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.dynamic_color import DynamicColor


KV = """
<ColorCard>
    orientation: "vertical"
    spacing: 20
    size_hint_y: None
    height: "60dp"
    radius: [15]

    MDLabel:
        text: root.text
        color: "grey"

    MDCard:
        theme_bg_color: "Custom"
        md_bg_color: root.bg_color
        size_hint_y: None
        height: "45dp"


MDScreen:
    md_bg_color: app.theme_cls.surfaceContainerLowColor

    MDIconButton:
        on_release: app.open_menu(self)
        pos_hint: {"top": .98}
        x: "12dp"
        icon: "menu"

    MDRecycleView:
        id: card_list
        viewclass: "ColorCard"
        bar_width: 0
        size_hint: 1, 0.92

        RecycleGridLayout:
            cols: 2
            spacing: 50
            padding: [25, 45, 25, 100]
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint: 1, None
            height: self.minimum_height
"""


class ColorCard(BoxLayout):
    text = StringProperty()
    bg_color = ColorProperty()


class Example(MDApp):
    menu: MDDropdownMenu = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.schemes_name_colors = [
            attr
            for attr in vars(DynamicColor)
            if not callable(getattr(DynamicColor, attr)) and not attr.startswith("__")
        ]
        return Builder.load_string(KV)

    def get_instance_from_menu(self, name_item):
        index = 0
        rv = self.menu.ids.md_menu
        opts = rv.layout_manager.view_opts
        datas = rv.data[0]

        for data in rv.data:
            if data["text"] == name_item:
                index = rv.data.index(data)
                break

        instance = rv.view_adapter.get_view(index, datas, opts[index]["viewclass"])

        return instance

    def open_menu(self, menu_button):
        menu_items = []
        for item, method in {
            "Set palette": lambda: self.set_palette(),
            "Switch theme style": lambda: self.theme_switch(),
        }.items():
            menu_items.append({"text": item, "on_release": method})
        self.menu = MDDropdownMenu(
            caller=menu_button,
            items=menu_items,
        )
        self.menu.open()

    def set_palette(self):
        instance_from_menu = self.get_instance_from_menu("Set palette")
        available_palettes = [
            name_color.capitalize() for name_color in hex_colormap.keys()
        ]

        menu_items = []
        for name_palette in available_palettes:
            menu_items.append(
                {
                    "text": name_palette,
                    "on_release": lambda x=name_palette: self.switch_palette(x),
                }
            )
        MDDropdownMenu(
            caller=instance_from_menu,
            items=menu_items,
        ).open()

    def switch_palette(self, selected_palette) -> None:
        self.theme_cls.primary_palette = selected_palette
        Clock.schedule_once(self.generate_cards, 0.5)

    def theme_switch(self) -> None:
        self.theme_cls.switch_theme()
        Clock.schedule_once(self.generate_cards, 0.5)

    def generate_cards(self, *args) -> None:
        self.root.ids.card_list.data = []
        for color in self.theme_cls.schemes_name_colors:
            value = f"{color}"
            print(getattr(self.theme_cls, value))
            self.root.ids.card_list.data.extend(
                [
                    {
                        "bg_color": getattr(self.theme_cls, value),
                        "text": value,
                    }
                ]
            )

    def on_start(self):
        Clock.schedule_once(self.generate_cards)


Example().run()
