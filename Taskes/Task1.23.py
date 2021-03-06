# Дано  целое  число  N.  Преобразовать  число  так, чтобы его цифры следовали в порядке возрастания


print("Enter the number: ")


def make_ascending_numerals(number):
    transposition = True
    while transposition:
        transposition = False
        buffer_number = number
        decade = 10
        while buffer_number // 10 != 0:
            if buffer_number % 10 < (buffer_number // 10) % 10:
                last_numeral = buffer_number % 10
                pre_last_numeral = (buffer_number // 10) % 10
                number = number - ((pre_last_numeral - last_numeral) * decade - (pre_last_numeral - last_numeral) * decade//10)
                transposition = True
            decade *= 10
            buffer_number //= 10
    return number

print(make_ascending_numerals(int(input())))