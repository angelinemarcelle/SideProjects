n = int(input('n: '))

def createBoard():
    global board, dic
    board = []
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append(j+i*n)
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
    
    dic = {}
    for i in range(n*n):
        dic.update({f'{i}' : i})

def printBoard():
    for i in board:
        for x in range(len(i)-1):
            print('%2s'%i[x]+' ', end='')
        print('%2s'%i[len(i)-1])
    
def getQueen():
    global queen, dic
    queen = input("Queens: ").split(' ')
    for i in queen:
        board[int(i)//n][int(i)%n] = ' Q'
        dic[f'{i}'] = 'Q'

def checkQueen():
    global dic
    count = 0
    for i in board: #checking the row
        for ii in i:
            if ii == ' Q':
                count += 1
        if count > 1:
            print("--> FAIL <--")
            exit()
        count = 0
    for i in range(n): #checking the column
        for ii in range(n):
            if board[ii][i] == ' Q':
                count += 1
        if count > 1:
            print("--> FAIL <--")
            exit()
        count = 0
    for i in queen:
        kiri, kanan = int(i), int(i) #atas
        kiri_outofbound = False
        kanan_outofbound = False
        while not kiri_outofbound or not kanan_outofbound:
            prevrow_kanan = kanan // n
            prevrow_kiri = kiri //n 
            kanan += (n + 1)
            kiri += (n - 1)
            if (kanan//n) - (prevrow_kanan) > 1 or kanan > n ** 2 - 1:
                kanan_outofbound = True
            else: 
                if str(kanan) in queen and not kanan_outofbound:
                    print("--> FAIL <--")
                    return
            if (kiri//n) == prevrow_kiri or kiri > n ** 2 - 1 :
                kiri_outofbound = True
            else: 
                if str(kiri) in queen and not kiri_outofbound:
                    print("--> FAIL <--")
                    return
        while not kiri_outofbound or not kanan_outofbound:
            prevrow_kanan = int(kanan) // n
            prevrow_kiri = int(kiri) //n 
            kanan -= (n + 1)
            kiri -= (n - 1)
            if (kiri//n) - (prevrow_kiri) > 1 or kiri < 0:
                kiri_outofbound = True
            else:
                if str(kiri) in queen and not kiri_outofbound:
                    print("--> FAIL <--")
                    return
            if (kanan//n) == prevrow_kanan or kanan < 0 :
                kanan_outofbound = True      
            else: 
                if str(kanan) in queen and not kanan_outofbound:
                    print("--> FAIL <--")
                    return
    print("--> SUCCESS <--")

createBoard()
getQueen()
printBoard()
checkQueen()

