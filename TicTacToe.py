size = int(input('Size--> '))

def createBoard():
    global board
    board = []
    temp = []
    for i in range(size):
        for j in range(size):
            temp.append(j+i*size)
        board.append(temp)
        temp = []
    for i in board:
        for ii in i[:-1]:
            if ii <= 9:
                print(' ' + str(ii), end=" ")
            else:
                print(ii, end=" ")
        if i[-1] <= 9:
            print(' ' + str(i[-1]))
        else:
            print(i[-1])

def printBoard():
    for i in board:
        for x in range(len(i)-1):
            print('%2s'%i[x]+' ', end='')
        print('%2s'%i[len(i)-1])

def getXO(turn):
  steps = 0
  while True:
    while True:
      player = int(input(f"{turn}--> "))
      steps += 1
      row = int(player)//size
      col = int(player)%size
      x = str(board[row][col])
      if (x.isdigit()):
        break
      else:
        print("Invalid input!")
    board[row][col] = turn
    printBoard()
    if steps == size ** 2:
        print('Winner: None')
        exit()
    if turn == 'X':
      turn = 'O'
      won = detectWin()
    else:
      turn = 'X'
      won = detectWin()
    if won:
      break

def detectWin():
  rowX = [0]*size
  rowO = [0]*size
  for i in range(size): # i = 0 1 2
    for ii in range(size): # ii = 0 1 2
      if board[i][ii] == "X":
        rowX[i] += 1
      elif board[i][ii] == "O":
        rowO[i] += 1
  for item in rowX:  
    if item == size:
      print("Winner: X")        
      return True
  for item in rowO:  
    if item == size:
      print("Winner: O") 
      return True


  colX = [0]*size
  colO = [0]*size
  for i in range(size): # i = 0 1 2
    for ii in range(size): # ii = 0 1 2
      if board[i][ii] == "X":
        colX[ii] += 1
      elif board[i][ii] == "O":
        colO[ii] += 1
  for item in colX:  
    if item == size:
      print("Winner: X")        
      return True
  for item in colO:  
    if item == size:
      print("Winner: O") 
      return True

  digX = [0,0]
  digO = [0,0]
  for i in range(size): # i = 0 1 2
    for ii in range(size): # ii = 0 1 2
      if i == ii:
        if board[i][ii] == "X":
          digX[0] += 1
        elif board[i][ii] == "O":
          digO[0] += 1
      if (i + ii) == (size - 1):
        if board[i][ii] == "X":
          digX[1] += 1
        elif board[i][ii] == "O":
          digO[1] += 1
  for item in digX:  
    if item == size:
      print("Winner: X")        
      return True
  for item in digO:  
    if item == size:
      print("Winner: O") 
      return True
    

turn = 'X'
createBoard()
getXO(turn)

    
