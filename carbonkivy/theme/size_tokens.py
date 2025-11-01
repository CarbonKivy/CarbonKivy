from kivy.metrics import dp, sp

spacing_tokens = {
    "spacing_01": dp("2"),
    "spacing_02": dp("4"),
    "spacing_03": dp("8"),
    "spacing_04": dp("12"),
    "spacing_05": dp("16"),
    "spacing_06": dp("24"),
    "spacing_07": dp("32"),
    "spacing_08": dp("40"),
    "spacing_09": dp("48"),
    "spacing_10": dp("64"),
    "spacing_11": dp("80"),
    "spacing_12": dp("96"),
    "spacing_13": dp("160"),
}

font_style_tokens = {
    # Productive set suffix '_01'
    # Expressive set suffix '_02'
    "code_01": {
        "font_size": sp("12"),
        "line_height": sp("16"),
    },
    "code_02": {
        "font_size": sp("14"),
        "line_height": sp("20"),
    },
    "label_01": {
        "font_size": sp("12"),
        "line_height": sp("16"),
    },
    "label_02": {
        "font_size": sp("14"),
        "line_height": sp("18"),
    },
    "helper_text_01": {
        "font_size": sp("12"),
        "line_height": sp("16"),
    },
    "helper_text_02": {
        "font_size": sp("14"),
        "line_height": sp("18"),
    },
    "legal_01": {
        "font_size": sp("12"),
        "line_height": sp("16"),
    },
    "legal_02": {
        "font_size": sp("14"),
        "line_height": sp("18"),
    },
    "body_compact_01": {
        "font_size": sp("14"),
        "line_height": sp("18"),
    },
    "body_compact_02": {
        "font_size": sp("16"),
        "line_height": sp("22"),
    },
    "body_01": {
        "font_size": sp("14"),
        "line_height": sp("20"),
    },
    "body_02": {
        "font_size": sp("16"),
        "line_height": sp("24"),
    },
    "heading_compact_01": {
        "font_size": sp("14"),
        "line_height": sp("18"),
        "weight_style": "SemiBold",
    },
    "heading_compact_02": {
        "font_size": sp("16"),
        "line_height": sp("22"),
        "weight_style": "SemiBold",
    },
    "heading_01": {
        "font_size": sp("14"),
        "line_height": sp("20"),
        "weight_style": "SemiBold",
    },
    "heading_02": {
        "font_size": sp("16"),
        "line_height": sp("24"),
        "weight_style": "SemiBold",
    },
    "heading_03": {
        "font_size": sp("20"),
        "line_height": sp("28"),
    },
    "heading_04": {
        "font_size": sp("28"),
        "line_height": sp("36"),
    },
    "heading_05": {
        "font_size": sp("32"),
        "line_height": sp("40"),
    },
    "heading_06": {
        "font_size": sp("42"),
        "line_height": sp("50"),
        "weight_style": "Light",
    },
    "heading_07": {
        "font_size": sp("54"),
        "line_height": sp("64"),
        "weight_style": "Light",
    },
}

button_size_tokens = {
    "Small": dp("32"),
    "Medium": dp("40"),
    "Large Productive": dp("48"),
    "Large Expressive": dp("48"),
    "Extra Large": dp("64"),
    "2XL": dp("80"),
}
