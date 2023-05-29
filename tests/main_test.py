import pytest
from strstyle import bold, red
from strstyle.__main__ import main


data_test_main_fail = [
    ['file', 'red'],
    ['file', 'not-a-style', 'Hello world'],
    ['file', 'red', 'not-a-style', 'Hello world'],
]


@pytest.mark.parametrize('argv_input', data_test_main_fail)
def test_main_fail(mocker, argv_input):
    mocker.patch('strstyle.__main__.argv', argv_input)
    with pytest.raises(SystemExit):
        main()


HELLO_WORLD = 'Hello world'
data_test_main = [
    (['red'], f'{red(HELLO_WORLD)}\n'),
    (['red', 'bold'], f'{bold(red(HELLO_WORLD))}\n'),
]


@pytest.mark.parametrize('input_styles, expected_print', data_test_main)
def test_main(capsys, mocker, input_styles, expected_print):
    mocker.patch('strstyle.__main__.argv', ['file', *input_styles, HELLO_WORLD])
    main()
    stdout = capsys.readouterr().out
    assert stdout == expected_print
