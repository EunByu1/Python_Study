def countdown(value):
    if (value == 0):
        return
    print(value)
    return countdown(value-1)

value = int(input())
countdown(value)
