def solution(park, routes):
    w = len(park[0])
    h = len(park)
    x, y = 0, 0
    for idx, row in enumerate(park):
        if "S" in row:
            x, y = (idx, row.index("S"))
    direction = {"S": (1, 0), "N": (-1, 0), "E": (0, 1), "W": (0, -1)}
    for route in routes:
        d, n = route.split()
        dx, dy = direction[d]
        tmp_x, tmp_y = x, y
        for i in range(int(n)):
            if 0 <= tmp_x+dx < h and 0 <= tmp_y+dy < w and park[tmp_x+dx][tmp_y+dy] != "X":
                tmp_x += dx
                tmp_y += dy
            else:
                break
        else:
            x, y = tmp_x, tmp_y
    return [x, y]