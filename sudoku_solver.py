grid = []
grid.append([0, 0, 0, 2, 6, 0, 7, 0, 1])
grid.append([6, 8, 0, 0, 7, 0, 0, 9, 0])
grid.append([1, 9, 0, 0, 0, 4, 5, 0, 0])
grid.append([8, 2, 0, 1, 0, 0, 0, 4, 0])
grid.append([0, 0, 4, 6, 0, 2, 9, 0, 0])
grid.append([0, 0, 0, 0, 0, 3, 0, 2, 8])
grid.append([0, 0, 9, 3, 0, 0, 0, 7, 4])
grid.append([0, 4, 0, 0, 5, 0, 0, 3, 6])
grid.append([7, 0, 3, 0, 0, 8, 0, 0, 0])

def can_be_put(board,row_position,col_position,number):
    row = board[row_position]
    #If the number isn't already in the row -> continue checking
    if number not in row:
        col = []
        for i in range (len(row)):
            #Filling the column
            col.append(board[i][col_position])
        #If the number isn't already in the column -> continue checking
        if number not in col:
            #Identify which of the 9 squares we are working on and asign it into a variable
            square=[]
            if row_position<3:
              if col_position<3:
                square=[board[i][0:3] for i in range(0,3)]
              elif col_position<6:
                square=[board[i][3:6] for i in range(0,3)]
              else:
                square=[board[i][6:9] for i in range(0,3)]
            elif row_position<6:
              if col_position<3:
                square=[board[i][0:3] for i in range(3,6)]
              elif col_position<6:
                square=[board[i][3:6] for i in range(3,6)]
              else:
                square=[board[i][6:9] for i in range(3,6)]
            else:
              if col_position<3:
                square=[board[i][0:3] for i in range(6,9)]
              elif col_position<6:
                square=[board[i][3:6] for i in range(6,9)]
              else:
                square=[board[i][6:9] for i in range(6,9)]
            #If the number isn't already in the row,column and square it's okay to put it there
            for i in range (3):
                if number in square[i]:
                    return False
            return True
    return False

def print_board(board):
    for i in range (len(board)):
        print(board[i])

def is_correct(board):
    for i in range (9):
        for j in range (9):
            if board[i][j] == 0:
                return "It's not well made"
            ##I temporaly set it to -1 to check and then revert it
            number = board[i][j]
            board[i][j] = -1
            if not can_be_put(board,i,j,number):
                return "It's not well made"
            else:
                board[i][j] = number
    return "It's well made"

def solve(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        for num in range(1,10):
          if can_be_put(board,i,j,num):
            board[i][j] = num
            solve(board)
            board[i][j] = 0
        return
  print_board(board)
  print(is_correct(board))
  input('More?')


solve(grid)