snippets = {
    "buttonsnippet" : """
CGridLayout:
    cols: 2
    adaptive: [False, True]
    spacing: dp(4)

    CButtonPrimary:
        text: "Primary"
        icon: "arrow--right"
        role: "Large Productive"
        size_hint_x: 0.4

    CButtonSecondary:
        text: "Secondary"
        icon: "arrow--right"
        role: "Large Productive"
        size_hint_x: 0.4

    CButtonGhost:
        text: "Ghost"
        icon: "arrow--right"
        role: "Large Productive"
        size_hint_x: 0.4

    CButtonTertiary:
        text: "Tertiary"
        icon: "arrow--right"
        role: "Large Productive"
        size_hint_x: 0.4

    CButtonDanger:
        text: "Primary"
        icon: "arrow--right"
        role: "Large Productive"
        size_hint_x: 0.4

""",
    "notificationsnippet": """
See Base app implementation for source codes.
""",
    "loadingsnippet": """
CGridLayout:
    cols: 1
    padding: dp(16)
    spacing: dp(16)
    adaptive: [False, True]

    AnchorLayout:
        size_hint: 1, None
        height: dp(150)

        CLoadingIndicator:
            role: "Large"

    AnchorLayout:
        size_hint: 1, None
        height: dp(150)

        CLoadingIndicator:
            role: "Small"

    CFloatLayout:
        size_hint: 1, None
        height: dp(150)

        CLabel:
            text: "Overlay"
            halign: "center"
            pos_hint: {"center_y": 0.5, "center_x": 0.5}
            style: "heading_05"

        CLoadingLayout:
            pos_hint: {"center_y": 0.5, "center_x": 0.5}
            CLoadingIndicator:
                role: "Large"

"""
}
