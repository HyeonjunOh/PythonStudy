def check_if_lined(board, ox):
    tmp_board = board.copy()
    tmp_board += ["".join(i) for i in zip(*tmp_board)]
    tmp_board.append(board[0][0]+board[1][1]+board[2][2])
    tmp_board.append(board[2][0]+board[1][1]+board[0][2])
    return tmp_board.count(ox*3)
    
def solution(board):
    tmp_board = "".join(board)
    cnt_o, cnt_x = tmp_board.count("O"), tmp_board.count("X")
    if cnt_x > cnt_o:
        return 0
    elif cnt_x == cnt_o:
        if check_if_lined(board, "O") != 0:
            return 0
        else:
            return 1
    else:
        if check_if_lined(board,"X") != 0 or cnt_x+1 < cnt_o:
            return 0
        else:
            return 1
            
            
        
        