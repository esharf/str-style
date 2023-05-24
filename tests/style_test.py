from strstyle.str_style import black, blue, bold, cyan, darkgrey, disabled, \
    green, invisible, lightblue, lightcyan, lightgrey, reverse, lightred, \
    orange, pink, purple, red, strikethrough, underline, yellow


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


def test_lightgrey():
    assert lightgrey(HELLO_WORLD) == '\x1b[37mHello world\x1b[0m'


def test_darkgrey():
    assert darkgrey(HELLO_WORLD) == '\x1b[90mHello world\x1b[0m'


def test_lightred():
    assert lightred(HELLO_WORLD) == '\x1b[91mHello world\x1b[0m'


def test_yellow():
    assert yellow(HELLO_WORLD) == '\x1b[93mHello world\x1b[0m'


def test_lightblue():
    assert lightblue(HELLO_WORLD) == '\x1b[94mHello world\x1b[0m'


def test_pink():
    assert pink(HELLO_WORLD) == '\x1b[95mHello world\x1b[0m'


def test_lightcyan():
    assert lightcyan(HELLO_WORLD) == '\x1b[96mHello world\x1b[0m'


def test_bold():
    assert bold(HELLO_WORLD) == '\x1b[01mHello world\x1b[0m'


def test_disabled():
    assert disabled(HELLO_WORLD) == '\x1b[02mHello world\x1b[0m'


def test_underline():
    assert underline(HELLO_WORLD) == '\x1b[04mHello world\x1b[0m'


def test_reverse():
    assert reverse(HELLO_WORLD) == '\x1b[07mHello world\x1b[0m'


def test_invisible():
    assert invisible(HELLO_WORLD) == '\x1b[08mHello world\x1b[0m'


def test_strikethrough():
    assert strikethrough(HELLO_WORLD) == '\x1b[09mHello world\x1b[0m'
