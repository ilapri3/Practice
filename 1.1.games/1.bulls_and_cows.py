from random import randint
from itertools import permutations
cor=list(permutations('0123456789',r=4))
r_num=randint(0,len(cor))
z_num=''.join(cor[r_num])
count=0
flag=0
while flag!=1:
    print('Введите ваше число')
    ans_num=input()
    if ans_num.isdigit() and (len(ans_num) == len(z_num)):
        cows=0
        bulls=0
        for i in range(len(z_num)):
            if ans_num[i] == z_num[i]:
                bulls+=1
            elif (ans_num[i] in z_num) and (ans_num[i] != z_num[i]):
                cows+=1
        count+=1
        if bulls==4 and cows == 0:
            flag=1
            print('быки ',bulls,'коровы ',cows, 'Попытка номер',count, 'ИГРА ОКОНЧЕНА')
        else:
            print('быки ',bulls,'коровы ',cows, 'Попытка номер',count)
    else:
        count+=1
        print('Неверный формат ввода','Попытка номер',count)
