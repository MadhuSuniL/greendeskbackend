import random
from .Tic_Toe_Patterns import get_pattern

tic_tac_toe_matrix = ['','','',
                      '','','',         
                      '','O','O',]
win_patterns = [
  # Rows
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Columns
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Diagonals
  [0, 4, 8],
  [2, 4, 6],
];

Player = 'X'
Computer = 'O'


def fill_tac_toe_matrix_cell(cell = None, ref = Player, tic_tac_toe_matrix = tic_tac_toe_matrix):
    if cell is None:
        return tic_tac_toe_matrix
    tic_tac_toe_matrix[cell] = ref
    return tic_tac_toe_matrix

def is_fill(tic_tac_toe_matrix, cell, ref):
    if tic_tac_toe_matrix[cell] == ref:
        return True
    return False 

def is_unfill(cell,tic_tac_toe_matrix):
    # if cell is None:
    #     return False
    return tic_tac_toe_matrix[cell] == ''

def get_filled_cells(tic_tac_toe_matrix,ref):
    filled_index = []
    for cell_index in range(len(tic_tac_toe_matrix)):
        if tic_tac_toe_matrix[cell_index] == ref:
            filled_index.append(cell_index)
    return filled_index

def get_besides_indexes(tic_tac_toe_matrix,cell):
    besides_indexes = []
    for indexes in win_patterns:
        if cell in indexes:
            besides_indexes+= indexes
    besides_indexes = list(set(besides_indexes))
    if cell in besides_indexes:
        besides_indexes.remove(cell)
    return besides_indexes

def get_empty_indexes(tic_tac_toe_matrix,cells):
    empty_cells = []
    if cells is not None:
        for cell in cells:
            if tic_tac_toe_matrix[cell] == '':
                empty_cells.append(cell)
        return empty_cells    
    for index in range(len(tic_tac_toe_matrix)):
        if tic_tac_toe_matrix[index] == '':
            empty_cells.append(index)
    return empty_cells    
        
def checking_win_move(tic_tac_toe_matrix,ref):
    for indexes in win_patterns:
        index_1 = indexes[0]    
        index_2 = indexes[1]    
        index_3 = indexes[2]    
        if is_fill(tic_tac_toe_matrix, index_1, ref):
            if is_fill(tic_tac_toe_matrix, index_2, ref):
                return index_3
            elif is_fill(tic_tac_toe_matrix,index_3, ref):
                return index_2
        elif is_fill(tic_tac_toe_matrix,index_2, ref):
            if is_fill(tic_tac_toe_matrix,index_3, ref):
                return index_1
    return None


def check_win(tic_tac_toe_matrix,type_of_pattern,cell):
    for indexes in win_patterns:
        index_1_value = tic_tac_toe_matrix[indexes[0]]
        index_2_value = tic_tac_toe_matrix[indexes[1]]
        index_3_value = tic_tac_toe_matrix[indexes[2]]
        player_win_check = index_1_value == Player and index_2_value == Player and index_3_value == Player
        computer_win_check = index_1_value == Computer and index_2_value == Computer and index_3_value == Computer
        if player_win_check:
            return get_pattern('user_winning_texts',cell),True
        if computer_win_check:
            return get_pattern('chatbot_winning_texts',cell), True
    
    return get_pattern(type_of_pattern,cell), False




def play(cell = None,ref = Player, tic_tac_toe_matrix = tic_tac_toe_matrix):
    tic_tac_toe_matrix = fill_tac_toe_matrix_cell(cell, ref, tic_tac_toe_matrix)
    #cheking computer winning move
    computer_move = checking_win_move(tic_tac_toe_matrix, Computer)
    if computer_move is not None and is_unfill(computer_move,tic_tac_toe_matrix):
        cell = computer_move
        return fill_tac_toe_matrix_cell(cell, Computer, tic_tac_toe_matrix),check_win(tic_tac_toe_matrix,'chatbot_winning_texts',cell)
    else:
        #cheking player winning move
        computer_move = checking_win_move(tic_tac_toe_matrix,Player)     
    if computer_move is not None and is_unfill(computer_move,tic_tac_toe_matrix):
        cell = computer_move
        return fill_tac_toe_matrix_cell(cell, Computer, tic_tac_toe_matrix), check_win(tic_tac_toe_matrix,'blocking_moves',cell)
    else:
        #cheking center cell 
        computer_move = 4        
        if is_unfill(computer_move,tic_tac_toe_matrix):
            cell = computer_move
            return fill_tac_toe_matrix_cell(cell, Computer, tic_tac_toe_matrix), check_win(tic_tac_toe_matrix,'surprising_moves',cell)
        else:
            filled_cells = get_filled_cells(tic_tac_toe_matrix, Computer)
            if not len(filled_cells):
                besides_cells = []
                for cell in filled_cells:
                    besides_cells += get_empty_indexes(tic_tac_toe_matrix,get_besides_indexes(tic_tac_toe_matrix, cell))
                if len(besides_cells):
                    random_cell = random.choice(besides_cells)
                    return fill_tac_toe_matrix_cell(random_cell, Computer, tic_tac_toe_matrix), check_win(tic_tac_toe_matrix,'strategic_moves',random_cell)
                else:
                    empty_cells = get_empty_indexes(tic_tac_toe_matrix,cells=None)
                    if len(empty_cells) == 0:
                        return tic_tac_toe_matrix, (get_pattern('draw_texts',postion = None), True)
                    random_cell = random.choice(empty_cells)
                    return fill_tac_toe_matrix_cell(random_cell, Computer, tic_tac_toe_matrix), check_win(tic_tac_toe_matrix,'regular_moves',random_cell)
            else:
                empty_cells = get_empty_indexes(tic_tac_toe_matrix,cells=None)
                if len(empty_cells) == 0:
                    return tic_tac_toe_matrix, (get_pattern('draw_texts',postion = None), True)
                random_cell = random.choice(empty_cells)
                return fill_tac_toe_matrix_cell(random_cell, Computer, tic_tac_toe_matrix), check_win(tic_tac_toe_matrix,'regular_moves',random_cell)

                
