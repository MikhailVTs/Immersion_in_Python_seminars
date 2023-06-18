multiplication = 1

while True:
    number = int(input("Введите число от 1 до 999 "))

    if number >= 1 and number <= 999:

        if len(str(number)) == 1:
            print(pow(number, 2))

        elif len(str(number)) == 2:
            while number > 0:
                digit = number % 10
                multiplication *= digit
                number //= 10
            print(multiplication)

        else:
            pass

    else:
        result = "Не входит в диапозон"

print(result)
