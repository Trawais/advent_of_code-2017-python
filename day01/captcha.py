def captcha(input):
    digits = __process_input_string(input)
    
    sum = 0
    for index in range(len(input)):
        current_digit = digits[index]
        
        # last element of list
        if index == (len(input) - 1):
            next_digit = digits[0]
        else:
            next_digit = digits[index + 1]

        if current_digit == next_digit:
            sum = sum + current_digit
    
    return sum

def captcha_2(input):
    digits = __process_input_string(input)

    sum = 0
    half = int(len(digits) / 2)
    for index in range(half):
        if digits[index] == digits[index + half]:
            sum = sum + digits[index]
    return sum * 2

def __process_input_string(vstup):
    digits = []
    for digit in vstup:
        digits.append(int(digit))
    return digits
