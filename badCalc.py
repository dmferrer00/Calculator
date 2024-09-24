def multiply(a, b):
    result = 0
    for i in range(abs(b)):
        result += a
    if b < 0:
        result =- result
    return result
