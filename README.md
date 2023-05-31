[![PyPI version](https://badge.fury.io/py/str-style.svg)](https://badge.fury.io/py/str-style) [![GuardRails badge](https://api.guardrails.io/v2/badges/184958?token=4d9cc37be41ca42f0bc2daa171df4f9a3c2ec046a8f510df251890dd9cdd98d2)](https://dashboard.guardrails.io/gh/esharf/repos/184958) [![codecov](https://codecov.io/gh/esharf/str-style/branch/master/graph/badge.svg?token=X35CF3HYU0)](https://codecov.io/gh/esharf/str-style)
# str-style

str-style is a Python package that provides string styling functions to enhance the visual appearance of text.

#### Usage

To use the str-style package in CLI, yoiu simply need to run the following:
```bash
str-style red Hello world
```

This will print the string "<span style="color: red">Hello world</span>" with red styling applied.

To use the str-style package in your own python script, follow these steps:

1. Import the desired styling function(s) from strstyle module.
2. Apply the styling function(s) to your string(s) to modify their appearance.
Here's an example of how to use the red styling function:
```python
>>> from strstyle import red
>>> print(red('Hello world'))
```

This will print the string "<span style="color: red">Hello world</span>" with red styling applied.

#### Available CLI Styling
- bold
- disabled
- italic
- underline
- sharp
- invisible
- strike-through
- double-underline
- black
- red
- green
- orange
- blue
- purple
- cyan
- light-grey
- red-background
- green-background
- yellow-background
- blue-background
- purple-background
- cyan-background
- light-grey-background
- dark-grey
- light-red
- yellow
- light-blue
- pink
- light-cyan

#### Available Styling Functions
- bold
- disabled
- italic
- underline
- sharp
- invisible
- strike_through
- double_underline
- black
- red
- green
- orange
- blue
- purple
- cyan
- light_grey
- red_background
- green_background
- yellow_background
- blue_background
- purple_background
- cyan_background
- light_grey_background
- dark_grey
- light_red
- yellow
- light_blue
- pink
- light_cyan


#### Contributing
Contributions to str-style are welcome! If you encounter any issues, have suggestions, or want to contribute improvements, please feel free to open an [issue](https://github.com/esharf/str-style/issues) or submit a [pull request](https://github.com/esharf/str-style/pulls).

#### License
This package is licensed under the MIT License. See the [LICENSE](https://github.com/esharf/str-style/blob/master/LICENSE) file for more details.
