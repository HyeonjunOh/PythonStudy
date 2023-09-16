from collections import deque

def bfs(maps, s, f):
    visited = set()
    q = deque([(s, 0)])
    while q:
        coord, step = q.popleft()
        if coord == f:
            return step
        for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            t_row, t_col, t_step = coord[0], coord[1], step
            if 0 <= t_row + r < len(maps) and 0 <= t_col + c < len(maps[0]) and maps[t_row+r][t_col+c] != "X":
                if (t_row+r, t_col+c) not in visited:
                    q.append(((t_row+r, t_col+c), t_step+1))
                    visited.add((t_row+r, t_col+c))
    return -1
def solution(maps):
    S, L, E = 0, 0, 0
    for idx, line in enumerate(maps):
        if line.find("S") != -1:
            S = idx, line.find("S")
        if line.find("L") != -1:
            L = idx, line.find("L")
        if line.find("E") != -1:
            E = idx, line.find("E")
    s_to_l = bfs(maps, S, L)
    l_to_e = bfs(maps, L, E)
    if s_to_l == -1 or l_to_e == -1:
        return -1
    else:
        return s_to_l+l_to_e