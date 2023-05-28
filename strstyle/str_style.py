def black(str_body: str) -> str:
    return f'\033[30m{str_body}\033[0m'


def red(str_body: str) -> str:
    return f'\033[31m{str_body}\033[0m'


def green(str_body: str) -> str:
    return f'\033[32m{str_body}\033[0m'


def orange(str_body: str) -> str:
    return f'\033[33m{str_body}\033[0m'


def blue(str_body: str) -> str:
    return f'\033[34m{str_body}\033[0m'


def purple(str_body: str) -> str:
    return f'\033[35m{str_body}\033[0m'


def cyan(str_body: str) -> str:
    return f'\033[36m{str_body}\033[0m'


def lightgrey(str_body: str) -> str:
    return f'\033[37m{str_body}\033[0m'


def darkgrey(str_body: str) -> str:
    return f'\033[90m{str_body}\033[0m'


def lightred(str_body: str) -> str:
    return f'\033[91m{str_body}\033[0m'


def yellow(str_body: str) -> str:
    return f'\033[93m{str_body}\033[0m'


def lightblue(str_body: str) -> str:
    return f'\033[94m{str_body}\033[0m'


def pink(str_body: str) -> str:
    return f'\033[95m{str_body}\033[0m'


def lightcyan(str_body: str) -> str:
    return f'\033[96m{str_body}\033[0m'


def bold(str_body: str) -> str:
    return f'\033[01m{str_body}\033[0m'


def disabled(str_body: str) -> str:
    return f'\033[02m{str_body}\033[0m'


def underline(str_body: str) -> str:
    return f'\033[04m{str_body}\033[0m'


def reverse(str_body: str) -> str:
    return f'\033[07m{str_body}\033[0m'


def invisible(str_body: str) -> str:
    return f'\033[08m{str_body}\033[0m'


def strikethrough(str_body: str) -> str:
    return f'\033[09m{str_body}\033[0m'
