number = input('>').upper()
roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
total = 0
for i in number:
    total += roman_numerals.get(i)
print(total)
