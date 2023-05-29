from sys import argv, exit
from strstyle import *


COMMAND_TO_FUNCTION_MAP = {
    "bold": bold,
    "disabled": disabled,
    "italic": italic,
    "underline": underline,
    "sharp": sharp,
    "invisible": invisible,
    "strikethrough": strikethrough,
    "double-underline": double_underline,
    "red": red,
    "black": black,
    "green": green,
    "orange": orange,
    "blue": blue,
    "purple": purple,
    "cyan": cyan,
    "lightcyan": lightcyan,
    "darkgrey": darkgrey,
    "lightred": lightred,
    "yellow": yellow,
    "lightblue": lightblue,
    "pink": pink,
    "lightgrey": lightgrey,
    "red-background": red_background,
    "green-background": green_background,
    "yellow-background": yellow_background,
    "blue-background": blue_background,
    "purple-background": purple_background,
    "cyan-background": cyan_background,
    "lightgrey-background": lightgrey_background,
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
                    *list(map(lambda x: f"- {x}", COMMAND_TO_FUNCTION_MAP.keys())),
                ]))
        exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
