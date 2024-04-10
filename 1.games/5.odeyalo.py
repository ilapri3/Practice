play_filed=[[' _',' _',' _',' _',' _'],[' _',' _',' _',' _',' _'],[' _',' _',' _',' _',' _'],[' _',' _',' _',' _',' _']]
for i in range(len(play_filed)):
    for j in range(len(play_filed[i])):
        print(play_filed[i][j], end='')
    print()
print('Символ для первого игрока - 1')
print('Символ для второго игрока - 2')
flag=0
count=0
player=1
check_box='1,2,3,4,5'
penalty_point1=0
penalty_point2=0
while flag!=1:
    print('Введите координату символа')
    x,y=map(str,input().split())
    if x in check_box and y in check_box:
        x=int(x)
        y=int(y)
        x-=1
        y-=1
        for i in range(len(play_filed)):
            for j in range(len(play_filed[i])):
                if play_filed[x][y] == ' _':
                    if player%2!=0:
                        play_filed[x][y] = ' 1'
                        if 0<=y<=3 and 0<=x<=2:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y+1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y+1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y+1] == play_filed[x][y]):
                                penalty_point1+=1
                        if y == 4 and 0<=x<=2:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point1+=1
                        if x == 3 and y == 4:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1

                        for i in range(len(play_filed)):
                            for j in range(len(play_filed[i])):
                                if play_filed[i][j] == ' _':
                                    count+=1
                        if count>=1:                              
                            player+=1
                            for i in range(len(play_filed)):
                                for j in range(len(play_filed[i])):
                                    print(play_filed[i][j], end='')
                                print()
                        else:
                            flag=1
                            for i in range(len(play_filed)):
                                for j in range(len(play_filed[i])):
                                    print(play_filed[i][j], end='')
                                print()
                            if penalty_point1 > penalty_point2:
                                print('Победа за 2')
                                print('Штрафные баллы 1 игрока',penalty_point1)
                                print('Штрафные баллы 2 игрока',penalty_point2)
                            else:
                                print('Победа за 1')
                                print('Штрафные баллы 1 игрока',penalty_point1)
                                print('Штрафные баллы 2 игрока',penalty_point2)
                        count=0
                    else:
                        play_filed[x][y] = ' 2'
                        if 0<=y<=3 and 0<=x<=2:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x-1][y+1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x][y+1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y+1] == play_filed[x][y]):
                                penalty_point2+=1
                        elif y == 4:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y-1] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point2+=1
                            if (play_filed[x+1][y] == play_filed[x][y]):
                                penalty_point2+=1
                        elif x == 3 and y == 4:
                            if (play_filed[x-1][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x-1][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y-1] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            if (play_filed[x][y] == play_filed[x][y]):
                                penalty_point1+=1
                            
                        for i in range(len(play_filed)):
                            for j in range(len(play_filed[i])):
                                if play_filed[i][j] == ' _':
                                    count+=1
                        if count>=1:                              
                            player+=1
                            for i in range(len(play_filed)):
                                for j in range(len(play_filed[i])):
                                    print(play_filed[i][j], end='')
                                print()
                        else:
                            flag=1
                            for i in range(len(play_filed)):
                                for j in range(len(play_filed[i])):
                                    print(play_filed[i][j], end='')
                                print()
                            if penalty_point1 > penalty_point2:
                                print('Победа за 2 игроком')
                                print('Штрафные баллы 1 игрока',penalty_point1)
                                print('Штрафные баллы 2 игрока',penalty_point2)
                            else:
                                print('Победа за 1 игроком')
                                print('Штрафные баллы 1 игрока',penalty_point1)
                                print('Штрафные баллы 2 игрока',penalty_point2)
                        count=0
    else:
        print('Некорректный ввод')