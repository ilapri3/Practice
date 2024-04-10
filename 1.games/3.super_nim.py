import random
count_chips=random.randint(6,10)
play_filed=[['1',' _',' _',' _',' _',' _',' _',' _',' _'],['2',' _',' _',' _',' _',' _',' _',' _',' _'],['3',' _',' _',' _',' _',' _',' _',' _',' _'],['4',' _',' _',' _',' _',' _',' _',' _',' _'],['5',' _',' _',' _',' _',' _',' _',' _',' _'],['6',' _',' _',' _',' _',' _',' _',' _',' _'],['7',' _',' _',' _',' _',' _',' _',' _',' _'],['8',' _',' _',' _',' _',' _',' _',' _',' _'],[' ',' a',' b',' c',' d',' e',' f',' g',' h']]
for i in range(count_chips):
    x=random.randint(0,7)
    y=random.randint(1,8)
    play_filed[x][y] = ' O'

for i in range(len(play_filed)):
    for j in range(len(play_filed[i])):
        print(play_filed[i][j], end='')
    print()
flag=0
player=0
while flag!=1:
    print('Введите строку, с которой вы хотите убрать пуговицы')
    check_num='1,2,3,4,5,6,7,8'
    check_alp='a,b,c,d,e,f,g,h'
    str=input()
    if str not in check_num and str not in check_alp:
        print('Некорректный ввод, попробуйте снова')
    else:
        count=0
        if str.isdigit() and (str in check_num):
            if str== '1':
                player+=1
                for i in range(1,9):
                    play_filed[0][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '2':
                player+=1
                for i in range(1,9):
                    play_filed[1][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '3':
                player+=1
                for i in range(1,9):
                    play_filed[2][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '4':
                player+=1
                for i in range(1,9):
                    play_filed[3][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '5':
                player+=1
                for i in range(1,9):
                    play_filed[4][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '6':
                player+=1
                for i in range(1,9):
                    play_filed[5][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '7':
                player+=1
                for i in range(1,9):
                    play_filed[6][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== '8':
                player+=1
                for i in range(1,9):
                    play_filed[7][i] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0


            

        else:
            if str== 'a':
                player+=1
                for i in range(0,8):
                    play_filed[i][1] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'b':
                player+=1
                for i in range(0,8):
                    play_filed[i][2] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'c':
                player+=1
                for i in range(0,8):
                    play_filed[i][3] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'd':
                player+=1
                for i in range(0,8):
                    play_filed[i][4] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'e':
                player+=1
                for i in range(0,8):
                    play_filed[i][5] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'f':
                player+=1
                for i in range(0,8):
                    play_filed[i][6] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'g':
                player+=1
                for i in range(0,8):
                    play_filed[i][7] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0

            if str== 'h':
                player+=1
                for i in range(0,8):
                    play_filed[i][8] = ' _'
                for k in range(len(play_filed)):
                    for l in range(len(play_filed[i])):
                        if play_filed[k][l] == ' O':
                            count+=1
                if count>=1:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end='')
                        print()
                else:
                    flag=1
                    if player%2==0:
                        print('Победа за 2ым игроком')
                    else:
                        print('Победа за 1ым игроком')
                count=0