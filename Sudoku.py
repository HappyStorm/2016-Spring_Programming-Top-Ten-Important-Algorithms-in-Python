
# coding: utf-8

# Sudoku Solver by Cheng-Wei Wu
# 
# 2016-2-15 @ Delta-107 National Tsing Hua University 

# In[64]:

import numpy as np
board = np.array([[0,3,0,9,8,7,0,0,6],
                  [4,0,0,0,0,0,5,0,0],
                  [0,6,0,0,0,0,8,0,0],
                  [0,1,7,0,3,4,0,6,8],
                  [8,5,6,0,0,0,1,3,4],
                  [0,2,0,6,1,0,7,5,0],
                  [0,0,3,4,0,0,0,2,5],
                  [0,0,1,0,0,0,0,0,7],
                  [5,0,0,8,7,3,0,4,0]])


# In[65]:

def sudoku_solver(board):
    '''Sudoku Solver by CWWU'''
    stack = [(0,board)]
    while stack:
        (curr_depth, curr_board) = stack.pop()
        if curr_depth == 81:
            return curr_board
        else:
            row,col = curr_depth // 9, curr_depth % 9
            if curr_board[row, col]:
                stack.append((curr_depth+1, curr_board.copy()))
            else:
                moves = ({1,2,3,4,5,6,7,8,9} - 
                         set(curr_board[row, :]) - 
                         set(curr_board[:, col]) -
                         set(curr_board[row//3*3:row//3*3+3,
                                        col//3*3:col//3*3+3].flatten()))
                for m in moves:
                    new_board = curr_board.copy()
                    new_board[row, col] = m
                    stack.append([(curr_depth+1), new_board])
    return None


# In[66]:

sudoku_solver(board)

