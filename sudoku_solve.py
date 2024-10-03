import random

def is_valid_move(matrix,row,column,num):
    for x in range(9):
        if matrix[row][x]==num:
            return False
        
    for x in range(9):
        if matrix[x][column]==num:
            return False
        
    corner_row=row - row%3
    corner_col=column - column%3
    for x in range(3):
        for y in range(3):
            if matrix[corner_row+x][corner_col+y]==num:
                return False
    return True


def generate_matrix():
    def pattern(r, c): return (3*(r%3)+r//3+c)%9
    def shuffle(s): return random.sample(s, len(s)) 
    rBase = range(3)
    rows  = [g*3 + r for g in shuffle(rBase) for r in shuffle(rBase)] 
    cols  = [g*3 + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums  = shuffle(range(1, 10))

    matrix = [[nums[pattern(r, c)] for c in cols] for r in rows]

    def remove_numbers(board, num_holes):
        for _ in range(num_holes):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            board[row][col] = 0

    remove_numbers(matrix, 40)
    return matrix

def solve(matrix,row,column):

    if column==9:
        if row==8:
            return True
        row+=1
        column=0
    if matrix[row][column]>0:
        return solve(matrix, row, column+1)
    for num in range(1,10):
        if is_valid_move(matrix,row,column,num):
            matrix[row][column]=num
            if solve(matrix,row,column+1):
                return True
        matrix[row][column]=0
    
    return False
puzzle=generate_matrix()
if solve(puzzle,0,0):
    for line in puzzle: print(line)
else:
    print("no sloution for this")




           
