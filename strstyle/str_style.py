def _paint(color_code: str, str_body: str) -> str:
    return f'\033[{color_code}m{str_body}\033[0m'


def black(str_body: str) -> str:
    return _paint('30', str_body)


def red(str_body: str) -> str:
    return _paint('31', str_body)


def green(str_body: str) -> str:
    return _paint('32', str_body)


def orange(str_body: str) -> str:
    return _paint('33', str_body)


def blue(str_body: str) -> str:
    return _paint('34', str_body)


def purple(str_body: str) -> str:
    return _paint('35', str_body)


def cyan(str_body: str) -> str:
    return _paint('36', str_body)


def lightgrey(str_body: str) -> str:
    return _paint('37', str_body)


def darkgrey(str_body: str) -> str:
    return _paint('90', str_body)


def lightred(str_body: str) -> str:
    return _paint('91', str_body)


def yellow(str_body: str) -> str:
    return _paint('93', str_body)


def lightblue(str_body: str) -> str:
    return _paint('94', str_body)


def pink(str_body: str) -> str:
    return _paint('95', str_body)


def lightcyan(str_body: str) -> str:
    return _paint('96', str_body)


def bold(str_body: str) -> str:
    return _paint('01', str_body)


def disabled(str_body: str) -> str:
    return _paint('02', str_body)


def underline(str_body: str) -> str:
    return _paint('04', str_body)


def reverse(str_body: str) -> str:
    return _paint('07', str_body)


def invisible(str_body: str) -> str:
    return _paint('08', str_body)


def strikethrough(str_body: str) -> str:
    return _paint('09', str_body)
