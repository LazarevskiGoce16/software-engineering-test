def sum(x, y):
    try:
        return x + y
    except TypeError:
        print('Please enter numbers!')
print(sum(5, 5))