multiplication = 1

while True:
    number = int(input("\nВведите число от 1 до 999: "))

    if number >= 1 and number <= 999:

        if len(str(number)) == 1:
            result = pow(number, 2)

        elif len(str(number)) == 2:
            while number > 0:
                num = number % 10
                multiplication *= num
                number //= 10
            result = multiplication
        
        else:

            reversal = 0
            while number != 0:
                num_rev = number % 10
                reversal = reversal * 10 + num_rev
                number //= 10
            result = reversal
            

    else:
        result = "Не входит в диапозон"
    
    print(result)
