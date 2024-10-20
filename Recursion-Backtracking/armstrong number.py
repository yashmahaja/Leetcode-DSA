def is_armstrong(number):
    # num_str = str(number)
    # num_digits = len(num_str)
    # sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # return sum_of_powers == number

    string = str(number)
    length = len(string)
    add = 0
    for i in string:
        add += int(i)**length
    return add == number

number = 15345
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
