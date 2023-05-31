from sys import argv, exit
from strstyle import black, blue, blue_background, bold, cyan, \
    cyan_background, dark_grey, disabled, double_underline, green, \
    green_background, invisible, italic, light_blue, light_cyan, light_grey, \
    light_grey_background, light_red, orange, pink, purple, \
    purple_background, red, red_background, sharp, strike_through, underline, \
    yellow, yellow_background


COMMAND_TO_FUNCTION_MAP = {
    "bold": bold,
    "disabled": disabled,
    "italic": italic,
    "underline": underline,
    "sharp": sharp,
    "invisible": invisible,
    "strike-through": strike_through,
    "double-underline": double_underline,
    "black": black,
    "red": red,
    "green": green,
    "orange": orange,
    "blue": blue,
    "purple": purple,
    "cyan": cyan,
    "light-grey": light_grey,
    "red-background": red_background,
    "green-background": green_background,
    "yellow-background": yellow_background,
    "blue-background": blue_background,
    "purple-background": purple_background,
    "cyan-background": cyan_background,
    "light-grey-background": light_grey_background,
    "dark-grey": dark_grey,
    "light-red": light_red,
    "yellow": yellow,
    "light-blue": light_blue,
    "pink": pink,
    "light-cyan": light_cyan,
}


def main():
    if len(argv) < 3:
        print("your command should look like 'str-style [styles] <string>'")
        exit(1)
    try:
        s = argv[-1]
        for style in argv[1:-1]:
            s = COMMAND_TO_FUNCTION_MAP[style](s)
        print(s)

    except KeyError:
        print("\n".join([
            f"style: {style} does not exist available options are:",
            *list(map(lambda x: f"- {x}",
                      COMMAND_TO_FUNCTION_MAP.keys())),
        ]))
        exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
