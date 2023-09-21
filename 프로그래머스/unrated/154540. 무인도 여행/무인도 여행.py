from collections import deque
def bfs(maps, x, y):
    visited = set()
    result = 0
    q = deque([(x, y)])
    lenx, leny = len(maps), len(maps[0])
    while q:
        tmp_x, tmp_y = q.popleft()
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = tmp_x, tmp_y
            if 0 <= tx+i < lenx and 0 <= ty+j < leny and maps[tx+i][ty+j] != 'X':
                if (tx+i, ty+j) not in visited:
                    q.append((tx+i, ty+j))
                    visited.add((tx+i, ty+j))
        result += int(maps[tmp_x][tmp_y])
        maps[tmp_x] = maps[tmp_x][:tmp_y] + "X" + maps[tmp_x][tmp_y+1:]
    return result

def solution(maps):
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                answer.append(bfs(maps, i, j))
    if answer:
        return sorted(answer)
    else:
        return [-1]