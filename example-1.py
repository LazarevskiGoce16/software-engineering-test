while True:
    try:
        age = int(input('How old are you? '))
        print(age)
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter age higher than 0!')
    else:
        print('Your input has been verified! Thank you!')
        break