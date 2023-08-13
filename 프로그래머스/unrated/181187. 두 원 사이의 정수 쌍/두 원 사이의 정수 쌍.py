import math
def solution(r1, r2):
    result = 0
    for x in range(1, r2 + 1):
        if x <= r1:
            result += math.floor((r2 ** 2 - x ** 2) ** 0.5) - math.ceil((r1 ** 2 - x ** 2) ** 0.5) + 1
        else:
            result += math.floor((r2 ** 2 - x ** 2) ** 0.5) + 1
    return 4*result