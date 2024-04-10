
def print_board(play_board):
    print("  A B C D E F G H")
    for i in range(8):
        print(1 + i, end=" ")
        for j in range(8):
            print(play_board[i][j], end=" ")
        print(" ")
    print("  A B C D E F G H")

motion = 0

def figure_moving(play_board, start, end):
    global motion
    piece = play_board[start[0]][start[1]]
    play_board[start[0]][start[1]] = '_'
    play_board[end[0]][end[1]] = piece
    motion += 1


def correct_move(play_board, start, end):
    piece = play_board[start[0]][start[1]]
    
    #Функция для хода пешек
    if piece == '_':
        return False

    if play_board[end[0]][end[1]] == '_':
        if piece.isupper():
            if start[0] == 6 and start[0] - end[0] == 2 and start[1] == end[1]:
                return True
            elif start[0] - end[0] == 1 and start[1] == end[1]:
                return True
        else:
            if start[0] == 1 and end[0] - start[0] == 2 and start[1] == end[1]:
                return True
            elif end[0] - start[0] == 1 and start[1] == end[1]:
                return True


    if piece.isupper() != play_board[end[0]][end[1]].isupper():
        if piece == 'P' and start[0] - end[0] == 1 and abs(start[1] - end[1]) == 1:
            return True
        elif piece == 'p' and end[0] - start[0] == 1 and abs(start[1] - end[1]) == 1:
            return True


    if piece == '_':
        return False
    
    if play_board[end[0]][end[1]] == '_': #если ходим на клетку с пустой фигурой
        
        if piece.isupper():
            #Проверка для ладьи
            if piece == 'R' or piece == 'r':
                if start[0] == end[0] or start[1] == end[1]:
                    if start[0] == end[0]:
                        for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                            if play_board[start[0]][i] != '_':
                                return False
                    else:
                        for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                            if play_board[i][start[1]] != '_':
                                return False
                    return True
            
            #Проверка для коня    
            elif piece == 'N' or piece == 'n':
                if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                    return True
                elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                    return True
                
            elif piece == 'K' or piece == 'k':
                if (abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1):
                    return True
                
            #Проверка для слона
            elif piece == 'B' or piece == 'b':
                if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                    row_b = 1 if end[0] - start[0] > 0 else -1
                    col_dir = 1 if end[1] - start[1] > 0 else -1
                    for i in range(1, abs(start[0] - end[0])):
                        if play_board[start[0] + (i * row_b)][start[1] + (i * col_dir)] != '_':
                            return False
                    return True
        
        else: #случай, когда ходим на клетку с фигурой
            #Проверка для ладьи
            if piece == 'R' or piece == 'r':
                if start[0] == end[0] or start[1] == end[1]:
                    if start[0] == end[0]:
                        for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                            if play_board[start[0]][i] != '_':
                                return False
                    else:
                        for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                            if play_board[i][start[1]] != '_':
                                return False
                    return True
            #Проверка для коня
            elif piece == 'N' or piece == 'n':
                if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                    return True
                elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                    return True
            
            elif piece == 'K' or piece == 'k':
                if (abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1):
                    return True
                
            #Проверка для слона
            elif piece == 'B' or piece == 'b':
                if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                    if end[0] - start[0] > 0:
                        row_b = 1 
                    else:
                        row_b = -1
                
                    if end[1] - start[1] > 0:
                        col_dir = 1 
                    else:
                        col_dir = -1
                    for i in range(1, abs(start[0] - end[0])):
                        if play_board[start[0] + (i * row_b)][start[1] + (i * col_dir)] != '_':
                            return False
                    return True

    #Отвечает за срубание фигур другими фигурами
    if piece.isupper() != play_board[end[0]][end[1]].isupper():
        
        if piece == 'R' or piece == 'r':
            if start[0] == end[0] or start[1] == end[1]:
                if start[0] == end[0]:
                    for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                        if play_board[start[0]][i] != '_':
                            return False
                else:
                    for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                        if play_board[i][start[1]] != '_':
                            return False
                return True
            
        elif piece == 'N' or piece == 'n':
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
                return True
            elif abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
                return True
        
        elif piece == 'K' or piece == 'k':
                if (abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1):
                    return True
                
        elif piece == 'B' or piece == 'b':
            if abs(start[0] - end[0]) == abs(start[1] - end[1]):
                if end[0] - start[0] > 0:
                    row_b = 1 
                else:
                    row_b = -1
                
                if end[1] - start[1] > 0:
                    col_dir = 1 
                else:
                    col_dir = -1

                for i in range(1, abs(start[0] - end[0])):
                    if play_board[start[0] + (i * row_b)][start[1] + (i * col_dir)] != '_':
                        return False
                return True

    if piece.upper() != 'Q':
        return False

    if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]) + 1, max(start[1], end[1])):
                if play_board[start[0]][i] != '_':
                    return False
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]) + 1, max(start[0], end[0])):
                if play_board[i][start[1]] != '_':
                    return False
        else:
            row_b = abs(start[0] - end[0])
            col_dir = abs(start[1] - end[1])
            
            for i in range(1, row_b):
                if start[0] < end[0]:
                    row = start[0] + i
                else:
                    row = start[0] - i
                if start[1] < end[1]:
                    col = start[1] + i
                else:
                    col = start[1] - i
                if play_board[row][col] != '_':
                    return False
        return True

    piece = play_board[start[0]][start[1]]
    

    
def play_game():
    motion = 0
    info_about_game = []
    print('Выберите режим игры: ')
    print('1 - если хотите начать обычную игру')
    print('2 - если хотите загрузить партию с файла')
    type_of_game = int(input())
    if type_of_game == 1:
        play_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

        while True:
            print_board(play_board)
            print('Введите в консоли "exit", чтобы завершить партию и предоставить файл со всеми ходами')
            if motion % 2 == 0:
                print("Ход белых:")
            else:
                print("Ход черных:")
            start = input("Введите координату фигуры (сначала буква, потом цифра): ")

            if start == 'exit':
                f = open('info_about_game.txt', 'w')
                f.writelines(info_about_game)
                f.close()
                print('Партия успешно записана в файл под названием: "info_about_game"!')
                return False
            
            end = input("Введите координату места, куда хотите перставить фигуру (сначала буква, потом цифра): ")
            start_row = int(start[1]) - 1
            start_col = ord(start[0]) - ord('a')
            end_row = int(end[1]) - 1
            end_col = ord(end[0]) - ord('a')

            stroke_with_motion = str(motion + 1) + '.' + ' ' + start + ':' + end + '\n'
            info_about_game.append(stroke_with_motion)

            if correct_move(play_board, (start_row, start_col), (end_row, end_col)):
                figure_moving(play_board, (start_row, start_col), (end_row, end_col))
                motion += 1
            else:
                print("Некорректный ход. Попробуйте еще раз.")
            print('Кол-во сделанных ходов', motion)


    if type_of_game == 2:
        #chess_match.txt
        name_of_match = input('Введите название файла, где хранится партия: ')
        with open(name_of_match, 'r') as file:
            play_board = []
            array = []
            for i in range(8):
                stroke = file.readline()[:-1]
                for el in range(len(stroke)):
                    array.append(stroke[el])
                play_board.append(array)
                array = []
        
        while True:
            print_board(play_board)
            print('Введите в консоли "exit", чтобы завершить партию и предоставить файл со всеми ходами')
            if motion % 2 == 0:
                print("Ход белых:")
            else:
                print("Ход черных:")
            start = input("Введите координату фигуры (сначала буква, потом цифра): ")

            if start == 'exit':
                f = open('info_about_game.txt', 'w')
                f.writelines(info_about_game)
                f.close()
                print('Партия успешно записана в файл под названием: "info_about_game"!')
                return False
            
            end = input("Введите координату места, куда хотите перставить фигуру (сначала буква, потом цифра): ")
            start_row = int(start[1]) - 1
            start_col = ord(start[0]) - ord('a')
            end_row = int(end[1]) - 1
            end_col = ord(end[0]) - ord('a')

            stroke_with_motion = str(motion + 1) + '.' + ' ' + start + ':' + end + '\n'
            info_about_game.append(stroke_with_motion)

            if correct_move(play_board, (start_row, start_col), (end_row, end_col)):
                figure_moving(play_board, (start_row, start_col), (end_row, end_col))
                motion += 1
            else:
                print("Некорректный ход. Попробуйте еще раз.")
            print('Кол-во сделанных ходов', motion)

play_game()