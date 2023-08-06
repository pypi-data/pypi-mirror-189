import math
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}


def extract(string, types=float):
    num = ""
    for data in string:
        if (data in numbers):
            num += data
    if (types == int):
        return int(math.floor(float(num)))
    else:
        return types(num)
