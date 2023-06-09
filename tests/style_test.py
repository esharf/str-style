from strstyle.str_style import black, blue, blue_background, bold, cyan, \
    cyan_background, dark_grey, disabled, double_underline, green, \
    green_background, invisible, italic, light_blue, light_cyan, \
    light_grey, light_grey_background, purple_background, \
    red_background, sharp, light_red, orange, pink, purple, \
    red, strike_through, underline, yellow, yellow_background


HELLO_WORLD = 'Hello world'


def test_black():
    assert black(HELLO_WORLD) == '\x1b[30mHello world\x1b[0m'


def test_red():
    assert red(HELLO_WORLD) == '\x1b[31mHello world\x1b[0m'


def test_green():
    assert green(HELLO_WORLD) == '\x1b[32mHello world\x1b[0m'


def test_orange():
    assert orange(HELLO_WORLD) == '\x1b[33mHello world\x1b[0m'


def test_blue():
    assert blue(HELLO_WORLD) == '\x1b[34mHello world\x1b[0m'


def test_purple():
    assert purple(HELLO_WORLD) == '\x1b[35mHello world\x1b[0m'


def test_cyan():
    assert cyan(HELLO_WORLD) == '\x1b[36mHello world\x1b[0m'


def test_light_grey():
    assert light_grey(HELLO_WORLD) == '\x1b[37mHello world\x1b[0m'


def test_dark_grey():
    assert dark_grey(HELLO_WORLD) == '\x1b[90mHello world\x1b[0m'


def test_light_red():
    assert light_red(HELLO_WORLD) == '\x1b[91mHello world\x1b[0m'


def test_yellow():
    assert yellow(HELLO_WORLD) == '\x1b[93mHello world\x1b[0m'


def test_light_blue():
    assert light_blue(HELLO_WORLD) == '\x1b[94mHello world\x1b[0m'


def test_pink():
    assert pink(HELLO_WORLD) == '\x1b[95mHello world\x1b[0m'


def test_light_cyan():
    assert light_cyan(HELLO_WORLD) == '\x1b[96mHello world\x1b[0m'


def test_bold():
    assert bold(HELLO_WORLD) == '\x1b[01mHello world\x1b[0m'


def test_disabled():
    assert disabled(HELLO_WORLD) == '\x1b[02mHello world\x1b[0m'


def test_underline():
    assert underline(HELLO_WORLD) == '\x1b[04mHello world\x1b[0m'


def test_sharp():
    assert sharp(HELLO_WORLD) == '\x1b[07mHello world\x1b[0m'


def test_invisible():
    assert invisible(HELLO_WORLD) == '\x1b[08mHello world\x1b[0m'


def test_strike_through():
    assert strike_through(HELLO_WORLD) == '\x1b[09mHello world\x1b[0m'


def test_italic():
    assert italic(HELLO_WORLD) == '\x1b[03mHello world\x1b[0m'


def test_red_background():
    assert red_background(HELLO_WORLD) == '\x1b[41mHello world\x1b[0m'


def test_green_background():
    assert green_background(HELLO_WORLD) == '\x1b[42mHello world\x1b[0m'


def test_yellow_background():
    assert yellow_background(HELLO_WORLD) == '\x1b[43mHello world\x1b[0m'


def test_blue_background():
    assert blue_background(HELLO_WORLD) == '\x1b[44mHello world\x1b[0m'


def test_purple_background():
    assert purple_background(HELLO_WORLD) == '\x1b[45mHello world\x1b[0m'


def test_cyan_background():
    assert cyan_background(HELLO_WORLD) == '\x1b[46mHello world\x1b[0m'


def test_light_grey_background():
    assert light_grey_background(HELLO_WORLD) == '\x1b[47mHello world\x1b[0m'


def test_double_underline():
    assert double_underline(HELLO_WORLD) == '\x1b[21mHello world\x1b[0m'
