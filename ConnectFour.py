def createBoard():
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = '  '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)

def makeMove(board, player, col):
    r = len(board)
    for row in range(r):
        if board[row][col]!='·' and board[row+1][col]=='·':
            board[row+1][col] = player
            break
        elif board[row][col]=='·':
            board[row][col] = player
            break

def illegal(board, move):
    if move.isalpha():
        if 'e' != move:
            return True
        else:
            return False
    if move.isdigit():
        if board[-1][int(move)] != '·':
            return True
        if int(move) > len(board[0]):
            return True
        else:
            return False

def detectWin(board):
    #checkrow
    row = len(board)
    col = len(board[0])
    for i in range(row):
        countx = 0
        counto = 0
        for j in range(col):
            if board[i][j] == 'X':
                counto = 0
                countx += 1
                if countx == 4:
                    return 1
            if board[i][j] == 'O':
                countx = 0
                counto += 1
                if counto == 4:
                    return 2
    for i in range(col):
        countx = 0
        counto = 0
        for j in range(row):
            if board[j][i] == 'X':
                counto = 0
                countx += 1
                if countx == 4:
                    return 1
            if board[j][i] == 'O':
                countx = 0
                counto += 1
                if counto == 4:
                    return 2
    for i in range(col):
        countx = 0
        counto = 0
        for j in range(row):
            temp = i+j
            if temp >= col:
                continue
            if board[j][temp] == 'X':
                counto = 0
                countx += 1
                if countx == 4:
                    return 1
            if board[j][temp] == 'O':
                countx = 0
                counto += 1
                if counto == 4:
                    return 2
    for i in range(col):
        countx = 0
        counto = 0
        for j in range(row):
            temp = i+j
            if temp >= col:
                continue
            if board[row - 1 - j][temp] == 'X':
                counto = 0
                countx += 1
                if countx == 4:
                    return 1
            if board[row - 1 - j][temp] == 'O':
                countx = 0
                counto += 1
                if counto == 4:
                    return 2
    return 0

def detectDraw(board):
    col = len(board[0])
    count = 0
    for i in range(col):
        if board[-1][i] != '·':
            count += 1
    if count == col:
        return True
    else: 
        return False
    
board = createBoard()
printBoard(board)
player = 'X'
while True:
    move = input( 'player'+player+' (col #): ')
    if illegal(board, move):
        printBoard(board)
        continue
    if move == 'e': break
    makeMove(board, player, int(move))
    win = detectWin(board)
    if win == 1:
        printBoard(board)
        print('Player X has won!') 
        break
    if win == 2:
        printBoard(board)
        print('Player O has won!') 
        break
    if detectDraw(board):
        printBoard(board)
        print('Draw!')
        break
    printBoard(board)
    if player == 'X': player = 'O'
    else: player = 'X'
print('bye')
