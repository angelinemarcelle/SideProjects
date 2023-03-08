import random
r = random.Random()
seed = int(input('Welcome to PIG. Enter a seed (int): '))
n = int(input('Number of players (int, 2-6): '))
dice = r.randrange(1, 7)
if seed != -1:
    r.seed(seed)
atm = 0
total_p1 = 0
total_p2 = 0
total_p3 = 0
total_p4 = 0
total_p5 = 0
total_p6 = 0


if n == 2:
    while total_p1 < 50 or total_p2 < 50:
        rh_1 = input('P1 (r/h): ')
        atm = 0
        if rh_1 == 'r':
            dice = r.randrange(1, 7)
            print('\tP1 rolls a ...', dice, '!')
        atm = dice
        while dice != 1 :
            rh_1 = input('P1 (r/h): ')
            if rh_1 == 'r':
                dice = r.randrange(1, 7)
                print('\tP1 rolls a ...', dice, '!')
            else:
                total_p1 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 total:', total_p1, '/', total_p2,  ' <--------')
        if (total_p1 >= 50):
            print('>>> Congratulation P1 <<<')
            break
        rh_2 = input('P2 (r/h): ')
        atm = 0
        if rh_2 == 'r':
            dice = r.randrange(1, 7)
            print('\tP2 rolls a ...', dice, '!')
        atm = dice
        while dice != 1 :
            rh_2 = input('P2 (r/h): ')
            if rh_2 == 'r':
                    dice = r.randrange(1, 7)
                    print('\tP2 rolls a ...', dice, '!')
            else:
                total_p2 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 total:', total_p1, '/', total_p2,  ' <--------')
        if (total_p2 >= 50):
            print('>>> Congratulation P2 <<<')
            break
if n == 3:
    while total_p1 < 100 or total_p2 < 100 or total_p3 < 100 or total_p4 < 100:
        rh_1 = input('P1 (r/h): ')
        atm = 0
        if rh_1 == 'r':
            dice = r.randrange(1, 7)
            print('\tP1 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_1 = input('P1 (r/h): ')
            if rh_1 == 'r':
                dice = r.randrange(1, 7)
                print('\tP1 rolls a ...', dice, '!')
            else:
                total_p1 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 total:', total_p1, '/', total_p2, '/', total_p3, ' <--------')
        if (total_p1 >= 50):
            print('>>> Congratulation P1 <<<')
            break
        rh_2 = input('P2 (r/h): ')
        atm = 0
        if rh_2 == 'r':
            dice = r.randrange(1, 7)
            print('\tP2 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_2 = input('P2 (r/h): ')
            if rh_2 == 'r':
                    dice = r.randrange(1, 7)
                    print('\tP2 rolls a ...', dice, '!')
            else:
                total_p2 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 total:', total_p1, '/', total_p2, '/', total_p3, ' <--------')
        if (total_p2 >= 50):
            print('>>> Congratulation P2 <<<')
            break
        rh_3 = input('P3 (r/h): ')
        atm = 0
        if rh_3 == 'r':
            dice = r.randrange(1, 7)
            print('\tP3 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_3 = input('P3 (r/h): ')
            if rh_3 == 'r':
                dice = r.randrange(1, 7)
                print('\tP3 rolls a ...', dice, '!')
            else:
                total_p3 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 total:', total_p1, '/', total_p2, '/', total_p3, ' <--------')
        if (total_p3 >= 50):
            print('>>> Congratulation P3 <<<')
            break
if n == 4:
    while total_p1 < 50 or total_p2 < 50 or total_p3 < 50 or total_p4 < 50:
        rh_1 = input('P1 (r/h): ')
        atm = 0
        if rh_1 == 'r':
            dice = r.randrange(1, 7)
            print('\tP1 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_1 = input('P1 (r/h): ')
            if rh_1 == 'r':
                dice = r.randrange(1, 7)
                print('\tP1 rolls a ...', dice, '!')
            else:
                total_p1 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, ' <--------')
        if (total_p1 >= 50):
            print('>>> Congratulation P1 <<<')
            break
        rh_2 = input('P2 (r/h): ')
        atm = 0
        if rh_2 == 'r':
            dice = r.randrange(1, 7)
            print('\tP2 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_2 = input('P2 (r/h): ')
            if rh_2 == 'r':
                    dice = r.randrange(1, 7)
                    print('\tP2 rolls a ...', dice, '!')
            else:
                total_p2 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, ' <--------')
        if (total_p2 >= 50):
            print('>>> Congratulation P2 <<<')
            break
        rh_3 = input('P3 (r/h): ')
        atm = 0
        if rh_3 == 'r':
            dice = r.randrange(1, 7)
            print('\tP3 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_3 = input('P3 (r/h): ')
            if rh_3 == 'r':
                dice = r.randrange(1, 7)
                print('\tP3 rolls a ...', dice, '!')
            else:
                total_p3 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, ' <--------')
        if (total_p3 >= 50):
            print('>>> Congratulation P3 <<<')
            break
        rh_4 = input('P4 (r/h): ')
        atm = 0
        if rh_4 == 'r':
            dice = r.randrange(1, 7)
            print('\tP4 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_4 = input('P4 (r/h): ')
            if rh_4 == 'r':
                dice = r.randrange(1, 7)
                print('\tP4 rolls a ...', dice, '!')
            else:
                total_p4 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, ' <--------')
        if (total_p4 >= 50):
            print('\t>>> Congratulation P4 <<<')
            break
if n == 5:
    while total_p1 < 50 or total_p2 < 50 or total_p3 < 50 or total_p4 < 50 or total_p5 < 50:
        rh_1 = input('P1 (r/h): ')
        atm = 0
        if rh_1 == 'r':
            dice = r.randrange(1, 7)
            print('\tP1 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_1 = input('P1 (r/h): ')
            if rh_1 == 'r':
                dice = r.randrange(1, 7)
                print('\tP1 rolls a ...', dice, '!')
            else:
                total_p1 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, ' <--------')
        if (total_p1 >= 50):
            print('>>> Congratulation P1 <<<')
            break
        rh_2 = input('P2 (r/h): ')
        atm = 0
        if rh_2 == 'r':
            dice = r.randrange(1, 7)
            print('\tP2 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_2 = input('P2 (r/h): ')
            if rh_2 == 'r':
                    dice = r.randrange(1, 7)
                    print('\tP2 rolls a ...', dice, '!')
            else:
                total_p2 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, ' <--------')
        if (total_p2 >= 50):
            print('>>> Congratulation P2 <<<')
            break
        rh_3 = input('P3 (r/h): ')
        atm = 0
        if rh_3 == 'r':
            dice = r.randrange(1, 7)
            print('\tP3 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_3 = input('P3 (r/h): ')
            if rh_3 == 'r':
                dice = r.randrange(1, 7)
                print('\tP3 rolls a ...', dice, '!')
            else:
                total_p3 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, ' <--------')
        if (total_p3 >= 50):
            print('>>> Congratulation P3 <<<')
            break
        rh_4 = input('P4 (r/h): ')
        atm = 0
        if rh_4 == 'r':
            dice = r.randrange(1, 7)
            print('\tP4 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_4 = input('P4 (r/h): ')
            if rh_4 == 'r':
                dice = r.randrange(1, 7)
                print('\tP4 rolls a ...', dice, '!')
            else:
                total_p4 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, ' <--------')
        if (total_p4 >= 50):
            print('\t>>> Congratulation P4 <<<')
            break
            rh_5 = input('P5 (r/h): ')
        atm = 0
        if rh_5 == 'r':
            dice = r.randrange(1, 7)
            print('\tP5 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_5 = input('P5 (r/h): ')
            if rh_5 == 'r':
                dice = r.randrange(1, 7)
                print('\tP5 rolls a ...', dice, '!')
            else:
                total_p5 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, ' <--------')
        if (total_p5 >= 50):
            print('\t>>> Congratulation P5 <<<')
            break
if n == 6:
    while total_p1 < 50 or total_p2 < 50 or total_p3 < 50 or total_p4 < 50 or total_p5 < 50 or total_p6 < 50:
        rh_1 = input('P1 (r/h): ')
        atm = 0
        if rh_1 == 'r':
            dice = r.randrange(1, 7)
            print('\tP1 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_1 = input('P1 (r/h): ')
            if rh_1 == 'r':
                dice = r.randrange(1, 7)
                print('\tP1 rolls a ...', dice, '!')
            else:
                total_p1 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p1 >= 50):
            print('>>> Congratulation P1 <<<')
            break
        rh_2 = input('P2 (r/h): ')
        atm = 0
        if rh_2 == 'r':
            dice = r.randrange(1, 7)
            print('\tP2 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_2 = input('P2 (r/h): ')
            if rh_2 == 'r':
                    dice = r.randrange(1, 7)
                    print('\tP2 rolls a ...', dice, '!')
            else:
                total_p2 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p2 >= 50):
            print('>>> Congratulation P2 <<<')
            break
        rh_3 = input('P3 (r/h): ')
        atm = 0
        if rh_3 == 'r':
            dice = r.randrange(1, 7)
            print('\tP3 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_3 = input('P3 (r/h): ')
            if rh_3 == 'r':
                dice = r.randrange(1, 7)
                print('\tP3 rolls a ...', dice, '!')
            else:
                total_p3 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p3 >= 50):
            print('>>> Congratulation P3 <<<')
            break
        rh_4 = input('P4 (r/h): ')
        atm = 0
        if rh_4 == 'r':
            dice = r.randrange(1, 7)
            print('\tP4 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_4 = input('P4 (r/h): ')
            if rh_4 == 'r':
                dice = r.randrange(1, 7)
                print('\tP4 rolls a ...', dice, '!')
            else:
                total_p4 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p4 >= 50):
            print('\t>>> Congratulation P4 <<<')
            break
        rh_5 = input('P5 (r/h): ')
        atm = 0
        if rh_5 == 'r':
            dice = r.randrange(1, 7)
            print('\tP5 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_5 = input('P5 (r/h): ')
            if rh_5 == 'r':
                dice = r.randrange(1, 7)
                print('\tP5 rolls a ...', dice, '!')
            else:
                total_p5 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p5 >= 50):
            print('\t>>> Congratulation P5 <<<')
            break
        rh_6 = input('P6 (r/h): ')
        atm = 0
        if rh_6 == 'r':
            dice = r.randrange(1, 7)
            print('\tP6 rolls a ...', dice, '!')
        else:
            dice = 1
        atm = dice
        while dice != 1 :
            rh_6 = input('P6 (r/h): ')
            if rh_6 == 'r':
                dice = r.randrange(1, 7)
                print('\tP6 rolls a ...', dice, '!')
            else:
                total_p6 += atm
                break
            if dice == 1:
                atm = 0
                break
            else:
                atm += dice
        print('--------> P1 / P2 / P3 / P4 / P5 / P6 total:', total_p1, '/', total_p2, '/', total_p3, '/', total_p4, '/', total_p5, '/', total_p6, ' <--------')
        if (total_p6 >= 50):
            print('\t>>> Congratulation P6 <<<')
            break


    
    
    
