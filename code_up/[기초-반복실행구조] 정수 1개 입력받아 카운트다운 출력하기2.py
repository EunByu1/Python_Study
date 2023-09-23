def countdown(value):
    if (value == 0):
        return
    print(value-1)
    return countdown(value-1)

value = int(input())
countdown(value)
