pos1_1,pos1_2,pos1_3,pos2_1,pos2_2,pos2_3,pos3_1,pos3_2,pos3_3='_','_','_','_','_','_','_','_','_'
play_filed = [[pos1_1,pos1_2,pos1_3],[pos2_1,pos2_2,pos2_3],[pos3_1,pos3_2,pos3_3]]
for i in range(len(play_filed)):
    for j in range(len(play_filed[i])):
        print(play_filed[i][j],end=' ')
    print()
count=0
flag=0
check='1,2,3'
while flag!=1:
    print('Введите координату, куда вы хотите поставить Х или О (сначала координата по оси Х потом по оси У) ')
    x,y=map(str,input().split())
    if x.isdigit() and y.isdigit() and (x in check) and (y in check):
        x=int(x)-1
        y=int(y)-1
        if play_filed[x][y] == '_':
            if count%2==0:
                play_filed[x][y] = 'X'
                if (play_filed[0][0] == 'X' and play_filed[0][1] == 'X' and play_filed[0][2] == 'X') or \
                (play_filed[1][0] == 'X' and play_filed[1][1] == 'X' and play_filed[1][2] == 'X') or \
                (play_filed[2][0] == 'X' and play_filed[2][1] == 'X' and play_filed[2][2] == 'X') or \
                (play_filed[0][0] == 'X' and play_filed[1][0] == 'X' and play_filed[2][0] == 'X') or \
                (play_filed[0][1] == 'X' and play_filed[1][1] == 'X' and play_filed[2][1] == 'X') or \
                (play_filed[0][2] == 'X' and play_filed[1][2] == 'X' and play_filed[2][2] == 'X') or \
                (play_filed[0][0] == 'X' and play_filed[1][1] == 'X' and play_filed[2][2] == 'X') or \
                (play_filed[2][0] == 'X' and play_filed[1][1] == 'X' and play_filed[0][2] == 'X'):
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end=' ')
                        print()
                    flag=1
                    print('Победа за крестиками')
                else:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end=' ')
                        print()
                    count+=1
                    if count == 9:
                        flag=1
                        print('Ничья')

            else:
                play_filed[x][y] = 'O'
                if (play_filed[0][0] == 'O' and play_filed[0][1] == 'O' and play_filed[0][2] == 'O') or \
                (play_filed[1][0] == 'O' and play_filed[1][1] == 'O' and play_filed[1][2] == 'O') or \
                (play_filed[2][0] == 'O' and play_filed[2][1] == 'O' and play_filed[2][2] == 'O') or \
                (play_filed[0][0] == 'O' and play_filed[1][0] == 'O' and play_filed[2][0] == 'O') or \
                (play_filed[0][1] == 'O' and play_filed[1][1] == 'O' and play_filed[2][1] == 'O') or \
                (play_filed[0][2] == 'O' and play_filed[1][2] == 'O' and play_filed[2][2] == 'O') or \
                (play_filed[0][0] == 'O' and play_filed[1][1] == 'O' and play_filed[2][2] == 'O') or \
                (play_filed[2][0] == 'O' and play_filed[1][1] == 'O' and play_filed[0][2] == 'O'):
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end=' ')
                        print()
                    flag=1
                    print('Победа за ноликами')
                else:
                    for i in range(len(play_filed)):
                        for j in range(len(play_filed[i])):
                            print(play_filed[i][j], end=' ')
                        print()
                    count+=1
        else:
            print('Это место уже занято, пожалуйста выберите другое')
    else:
        print('Некорректный ввод, попробуйте снова')