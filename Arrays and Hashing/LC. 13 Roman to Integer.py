def romanToInt(s):
    roman_to_numerical = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    suma = 0

    for char in range(len(s)):
        if char < len(s) - 1 and roman_to_numerical[s[char]] < roman_to_numerical[s[char + 1]]:
            suma -= roman_to_numerical[s[char]]
        else:
            suma += roman_to_numerical[s[char]]
    return suma

s = "XD"
print(romanToInt(s))