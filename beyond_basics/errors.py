def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "\nZero division Error"
print(divide(1,0))
