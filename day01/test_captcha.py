from captcha import captcha, captcha_2

def test_1_captcha():
    input = "1122"
    expected_output = 3
    assert captcha(input) == expected_output

def test_2_captcha():
    input = "1111"
    expected_output = 4
    assert captcha(input) == expected_output

def test_3_captcha():
    input = "1234"
    expected_output = 0
    assert captcha(input) == expected_output

def test_4_captcha():
    input = "91212129"
    expected_output = 9
    assert captcha(input) == expected_output

def test_solve_puzzle_captcha():
    input = open('./day01/puzzle_input.txt', 'r').read()
    expected_output = 1089
    assert captcha(input) == expected_output

def test_1_captcha_2():
    input = "1212"
    expected_output = 6
    assert captcha_2(input) == expected_output

def test_2_captcha_2():
    input = "1221"
    expected_output = 0
    assert captcha_2(input) == expected_output

def test_3_captcha_2():
    input = "123425"
    expected_output = 4
    assert captcha_2(input) == expected_output

def test_4_captcha_2():
    input = "123123"
    expected_output = 12
    assert captcha_2(input) == expected_output

def test_5_captcha_2():
    input = "12131415"
    expected_output = 4
    assert captcha_2(input) == expected_output

def test_solve_puzzle_captcha_2():
    input = open('./day01/puzzle_input.txt', 'r').read()
    expected_output = 1156
    assert captcha_2(input) == expected_output
