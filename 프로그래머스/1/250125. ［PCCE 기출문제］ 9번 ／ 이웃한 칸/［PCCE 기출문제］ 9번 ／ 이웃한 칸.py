def solution(board, h, w):
    board = [[0] * (len(board) + 2)] + [[0] + row + [0] for row in board] + [[0] * (len(board) + 2)]
    return [board[h+1+i][w+1+j] for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]].count(board[h+1][w+1])