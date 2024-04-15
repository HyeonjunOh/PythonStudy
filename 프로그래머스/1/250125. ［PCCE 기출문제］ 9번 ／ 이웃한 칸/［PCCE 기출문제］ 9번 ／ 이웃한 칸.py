def solution(board, h, w):
    board = [[0]*len(board)] + board + [[0]*len(board)]
    board = [[0]+i+[0] for i in board]
    return [board[h+1+i][w+1+j] for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]].count(board[h+1][w+1])