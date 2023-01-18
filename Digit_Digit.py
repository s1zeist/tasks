def square_digits(num):
    result = ""
    for d in str(num):
        result += str(int(d) ** 2)
    return int(result)
