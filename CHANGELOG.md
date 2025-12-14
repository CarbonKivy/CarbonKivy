# Changelog

- # 0.0.4
  Massive implementations on new widgets.

  - `UIX`
    - Checkbox
    - Partition of Label
      - CLabel
      - CLabelCircular
    - DatePicker
    - Partition of Icon
      - CIcon
      - CIconCircular
    - Dropdown
    - LoadingIndicator
    - Modal
    - Notification
    - UIShellHeader
    - UIShellLeftPanel
    - UIShellRightPanel
    - UI Shell Components
    - Tab
    - Toggletip
    - Tooltip

  - `BEHAVORS`
    - ElevationBehavior
    - Partition of BackgroundColorBehavior
      - BackgroundColorBehaviorCircular
      - BackgroundColorBehaviorRectangular
    - SelectableBehavior
    - SelectionBehavior
    - TooltipBehavior

  - `THEMES`
    - [x] White
    - [ ] Gray10
    - [ ] Gray90
    - [x] Gray100

  - `Utilities`
    - `update_system_ui` for Android Status and Navbar styles.
    - Development utilities like `LiveApp` has been introduced for hot-reload setup.
    - Native file uploader for Kivy applications across multiple platforms: Windows, macOS, Linux, and Android has been introduced. (examples are available on github.)

  - An upgraded version of `StateFocusBehavior` has been introduced.
  - General bug fixes and improvements.
  
- # 0.0.3
  Major Upgrades and Improvements. Implementation of new widgets.

  - `UIX`
    - CodeSnippet
    - FocusContainer
    - GridLayout
    - TextInput
  
  - `BEHAVIORS`
    - HierarchicalLayerBehavior
    - StateFocusBehavior

  - Completed and improved Button component implmentation with all available styles.
  - Completed and improved Link component implmentation.
  - Completed and improved TextInput component implmentation.
  - Improved `focus` interactive state behavior.
  - General bug fixes and improvements.

- # 0.0.2
  - Bug fixes related to missing font files, add inclusion to packaging.
  - Improvements in CButton behaviors in different interactive states.

- # 0.0.1
  Introductory release with basic widgets and core utilities and behaviors.

  - `UIX`
    - AnchorLayout
    - BoxLayout
    - Button
    - Divider
    - FloatLayout
    - Icon
    - Image
    - Label
    - Link
    - RelativeLayout
    - Screen
    - ScreenManager
    - ScrollView
    - StackLayout

  - `BEHAVIORS`
    - AdaptiveBehavior
    - BackgroundColorBehavior
    - DeclarativeBehavior (Follows the same declarative pattern as [KivyMD's Declarative Behavior](https://github.com/kivymd/KivyMD/blob/master/kivymd/uix/behaviors/declarative_behavior.py).)
    - HoverBehavior

  - `THEMES`
    - [x] White
    - [ ] Gray10
    - [ ] Gray90
    - [ ] Gray100

  - `TYPOGRAPHY`
    - IBM Plex Sans
    - IBM Plex Serif
    - IBM Plex Mono
