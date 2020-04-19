#!/usr/bin/env python
#coding:utf-8
import math
import copy
import time
import numpy as np
import sys
"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def domain_builder(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    #board is a dictionary
    name = []
    domain_board = {}
    for location in board:
        if board[location] == 0:
            domain_board.update({location: domain_finder(board, location, board[location])})
    #solved_board = board
    #print (domain_board)
    return domain_board

def MRV(domain):
    sorted_domain = sorted(domain, key=lambda key: len(domain[key]))
    #print (sorted_domain[0])
    
    #print (domain[MRV_key])
    return sorted_domain[0]

def check_goal(board):
    flag = 0
    for key in board:
        if board[key] == 0:
            flag = 1
    if flag == 1:
        return False
    else:
        return True
    
def backtracking_search(board, domain_board, MRV_key):
    #print (goal_check(board))
    #print ((len(domain_board[MRV_key])))
    if len(domain_board[MRV_key]) == 0:
        return None
    if check_goal(board) != True and (len(domain_board[MRV_key]) != 0):  
        #print ("check")
        for i in domain_board[MRV_key]:   
            board.update({MRV_key: i})
            if check_goal(board) == True:
                break
            domain = domain_builder(board)
            key = MRV(domain)
            result = backtracking_search(copy.deepcopy(board), domain, key)
            if result == None:
                continue
            elif check_goal(result):
                return result
    return board


def backtracking(board):
    domain = domain_builder(board)
    #for name, values in domain:
        #print ("values", values)
    MRV_key = MRV(domain)
    #print ("Key is", MRV_key)
    #print (domain[MRV_key])
    solved_board = backtracking_search(board,domain, MRV_key)
    return solved_board
    

def domain_finder(board, key, value):
    grid = {
            (1,1): ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"],
            (1,2): ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"],
            (1,3): ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"],
            (2,1): ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"],
            (2,2): ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"],
            (2,3): ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"],
            (3,1): ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"],
            (3,2): ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"],
            (3,3): ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"],
            }
    global_set = set((1,2,3,4,5,6,7,8,9))
    #for location, value in board.values():
    location = key
    value_comp = set()
    #print (location[0])
    for c in COL:
        x = str(location[0] + c)
        #print(board[x])
        value_comp.add(board[x])    
    for r in ROW:
        y = str(r + location[1])
        #beta = set((board[y]))
        value_comp.add(board[y])
    b = math.ceil(int(location[1])/3)
    a = math.ceil((ord(location[0]) - 64)/3)
    for i in grid[(a,b)]:
         value_comp.add(board[i])
    value_comp = global_set.difference(value_comp)
    #print (value_comp)
    return value_comp


if __name__ == '__main__':
    #  Read boards from source.
    line = sys.argv[1]

    '''src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()'''

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")
    time_board = []
    # Solve each board using backtracking
    '''for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue'''

        # Parse boards to dict representation, scanning board L to R, Up to Down
    board = { ROW[r] + COL[c]: int(line[9*r+c])
              for r in range(9) for c in range(9)}
    solved_board = backtracking(board)
    # Print starting board. TODO: Comment this out when timing runs.
        #print_board(board)
        

        # Solve with backtracking
    '''start_time = time.time()

    end_time = time.time()
    time_board.append(end_time - start_time)'''
    

        # Print solved board. TODO: Comment this out when timing runs.
        #print_board(solved_board)

        # Write board to file
    outfile.write(board_to_string(solved_board))
    outfile.write('\n')
    outfile.close()
    #print (end_time - start_time)
    '''print (min(time_board), max(time_board), np.mean(time_board), np.std(time_board))
    print("Finishing all boards in file.")'''