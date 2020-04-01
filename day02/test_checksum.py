from checksum import find_max, find_min

def test_max():
    input = [5, 6, 9, 1, 5]
    expected_output = 9
    assert find_max(input) == expected_output

def test_min():
    input = [5, 6, 9, 1, 5]
    expected_output = 1
    assert find_min(input) == expected_output