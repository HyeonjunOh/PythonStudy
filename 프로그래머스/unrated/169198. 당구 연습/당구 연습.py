def distance(a, b, x, y):
    return (a - x) ** 2 + (b - y) ** 2


def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        if startX == x:
            tmp = float('inf')
            if startY - y < 0:
                tmp = distance(startX, startY, x, -y)
            else:
                tmp = distance(startX, startY, x, 2 * n - y)
            answer.append(min(distance(startX, startY, -x, y), distance(startX, startY, 2 * m - x, y), tmp))
        elif startY == y:
            tmp = float('inf')
            if startX - x < 0:
                tmp = distance(startX, startY, -x, y)
            else:
                tmp = distance(startX, startY, 2 * m - x, y)
            answer.append(min(distance(startX, startY, x, -y), distance(startX, startY, x, 2 * n - y), tmp))
        else:
            answer.append(min(distance(startX, startY, x, -y),
                              distance(startX, startY, x, 2 * n - y),
                              distance(startX, startY, -x, y),
                              distance(startX, startY, 2 * m - x, y)))
    return answer