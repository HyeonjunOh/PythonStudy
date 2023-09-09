from collections import deque

def solution(board):
    answer = -1
    start = [0, 0]
    board = ["D"+i+"D" for i in board]
    board = ["D"*len(board[0])] + board + ["D"*len(board[0])]
    visited = [[-1]*len(board[0]) for _ in range(len(board))]
    q = deque()
    for col, line in enumerate(board):
        if line.find("R") != -1:
            start = col, line.find("R")
            visited[col][line.find("R")] = 0
            q.append([*start, 0])

    while q:
        col, row, bump = q.popleft()
        if board[col][row] == "G":
            return bump
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tmp_col, tmp_row = col, row
            while board[tmp_col + i][tmp_row + j] != "D":
                tmp_col += i
                tmp_row += j
            if visited[tmp_col][tmp_row] == -1 or visited[tmp_col][tmp_row] > bump+1:
                q.append([tmp_col, tmp_row, bump+1])
                visited[tmp_col][tmp_row] = bump+1
    return answer