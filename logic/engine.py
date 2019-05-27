def set_start_board(board):

    for row in range(6):
        for column in range(6):
            board[(row, column)] = '-' # empty string when pool without any checker

    # setting starting values for first player - 'v'
    board[(0, 0)] = board[(0, 2)] = board[(0, 4)] = 'v'
    board[(1, 1)] = board[(1, 3)] = board[(1, 5)] = 'v'

    # setting values for second player - 'b'
    board[(4, 0)] = board[(4, 2)] = board[(4, 4)] = 'b'
    board[(5, 1)] = board[(5, 3)] = board[(5, 5)] = 'b'

    return board

def sprawdz_zwyciestwo(board):
    sprawdzenie_niebieskich = sprawdzenie_fioletowych = 0

    if ('b' in board.values()) is True or ('b_k' in board.values()) is True:
        sprawdzenie_niebieskich = 1
    if ('v' in board.values()) is True or ('v_k' in board.values()) is True:
        sprawdzenie_fioletowych = 1

    if (sprawdzenie_fioletowych + sprawdzenie_niebieskich) > 1:
        return 2 #ilosc dostepnych stron
    else:
        if sprawdzenie_niebieskich == 1:
            return "Blue has won!"
        if sprawdzenie_fioletowych == 1:
            return "Purple has won!"

def check_legal_moves(rzad_start, kolumna_start, rzad_end, kolumna_end, board, turn):

            test_a = test_b = test_c = test_d = rzad_posredni = kolumna_posrednia = test_e = test_f = None

            # A. Ruch tylko swoim pionkiem
            if turn[1] == 'b':
                if board[(rzad_start,kolumna_start)] == 'b' or board[(rzad_start,kolumna_start)] == 'b_k':
                    test_a = True
                else:
                    return 'You cant move with opponent checker!'
            if turn[1] == 'v':
                if board[(rzad_start, kolumna_start)] == 'v' or board[(rzad_start,kolumna_start)] == 'v_k':
                    test_a = True
                else:
                    return 'You cant move with opponent checker!'

            # B. Tylko na puste pole
            if board[(rzad_end, kolumna_end)] == '-':
                test_b = True
            else:
                return 'You cant move on occupied box!'

            # C. Brak ruchu do tylu (kolumna nie moze byc wieksza dla jednych i mniejsza dla drugich)
            if turn[1] == 'b':
                if rzad_end < rzad_start and board[(rzad_start,kolumna_start)] != 'b_k':
                    test_c = True
                elif board[(rzad_start, kolumna_start)] == 'b_k':
                    test_c = True
                else:
                    return 'You arent moving forward!'

            if turn[1] == 'v':
                if rzad_end > rzad_start and board[(rzad_start,kolumna_start)] != 'v_k':
                    test_c = True
                elif board[(rzad_start, kolumna_start)] == 'v_k':
                    test_c = True
                else:
                    return 'You arent moving forward!'

            # D. Tylko na parzystych polach
            if (rzad_end + kolumna_end) % 2 == 0:
                test_d = True
            else:
                return 'You can only move diagonally!'

            # ?. Damka nie rusza się horyzontalnie
            if turn[1] == 'b' and  rzad_end == rzad_start and board[(rzad_start, kolumna_start)] == 'b_k':
                    return 'You arent moving forward!'
            if turn[1] == 'v' and  rzad_end == rzad_start and board[(rzad_start, kolumna_start)] == 'v_k':
                    return 'You arent moving forward!'

            # E. Maks dwa pola do przodu i w szerz
            if abs(rzad_end - rzad_start) <= 2 and abs(kolumna_end - kolumna_start) <=2:
                test_e = True
            else:
                return 'Your move is too large!'

            # F. Nie do przodu
            if kolumna_start != kolumna_end:
                test_f = True
            else:
                return 'You cant move in straight line!'

            if test_a == True and test_b == True and test_c == True and test_d == True and test_e == True and test_f == True:

                # Mechanizm zbicia (usuwa pośredni rząd)
                if abs(rzad_start - rzad_end) == 2:
                    if rzad_start > rzad_end:
                        rzad_posredni = rzad_start - 1
                    else:
                        rzad_posredni = rzad_end - 1

                    if kolumna_start > kolumna_end:
                        kolumna_posrednia = kolumna_start - 1
                    else:
                        kolumna_posrednia = kolumna_end - 1

                    if turn[1] == 'b':
                        if board[(rzad_posredni, kolumna_posrednia)] == 'v' or board[(rzad_posredni, kolumna_posrednia)] == 'v_k':
                            board[(rzad_posredni, kolumna_posrednia)] = '-'
                        else:
                            return 'You cant perform this capture!'

                    if turn[1] == 'v':
                        if board[(rzad_posredni, kolumna_posrednia)] == 'b' or board[(rzad_posredni, kolumna_posrednia)] == 'b_k':
                            board[(rzad_posredni, kolumna_posrednia)] = '-'
                        else:
                            return 'You cant perform this capture!'

            # Mechanizm zwykłego ruchu i zamiany na króla

                if turn[1] == 'b':

                    if rzad_end == 0:
                        board[(rzad_start, kolumna_start)] = '-'
                        board[(rzad_end, kolumna_end)] = "b_k"
                    else:
                        if board[(rzad_start, kolumna_start)] == 'b':
                            board[(rzad_start, kolumna_start)] = '-'
                            board[(rzad_end, kolumna_end)] = 'b'
                        elif board[(rzad_start, kolumna_start)] == 'b_k':
                            board[(rzad_start, kolumna_start)] = '-'
                            board[(rzad_end, kolumna_end)] = 'b_k'
                    turn[1] = 'v'

                elif turn[1] == 'v':

                    if rzad_end == 5:
                        board[(rzad_start, kolumna_start)] = '-'
                        board[(rzad_end, kolumna_end)] = 'v_k'
                    else:
                        if board[(rzad_start, kolumna_start)] == 'v':
                            board[(rzad_start, kolumna_start)] = '-'
                            board[(rzad_end, kolumna_end)] = 'v'
                        elif board[(rzad_start, kolumna_start)] == 'v_k':
                            board[(rzad_start, kolumna_start)] = '-'
                            board[(rzad_end, kolumna_end)] = 'v_k'
                    turn[1] = 'b'

                if sprawdz_zwyciestwo(board) == 2:
                    return 'Move completed!'
                else:
                    return sprawdz_zwyciestwo(board)

def ai(board, turn):

#Testowy mechanizm ruchu bez bicia

    for x in range(6):
        for y in range(6):

                if (x - 1 >= 0) and (y + 1 < 6) and (board[(x, y)] == 'b'):
                    if board[x - 1, y + 1] == '-' and ((x - 1) + (y + 1)) % 2 == 0:

                            board[(x - 1, y + 1)] = 'b'
                            board[(x, y)] = '-'
                            turn[1] = 'v'
                            return False

                    elif (x - 1 >= 0) and (y - 1 >= 0) and (board[(x, y)] == 'b'):
                        if board[x - 1, y - 1] == '-' and ((x - 1) + (y - 1)) % 2 == 0:

                            board[(x - 1, y - 1)] = 'b'
                            board[(x, y)] = '-'
                            turn[1] = 'v'
                            return False

    turn[1] = 'v'
    return False

'''
def wypisz(board):
    print("0: ", board[(0, 0)], board[(0, 1)], board[(0, 2)], board[(0, 3)], board[(0, 4)],
          board[(0, 5)])
    print("1: ", board[(1, 0)], board[(1, 1)], board[(1, 2)], board[(1, 3)], board[(1, 4)],
          board[(1, 5)])
    print("2: ", board[(2, 0)], board[(2, 1)], board[(2, 2)], board[(2, 3)], board[(2, 4)],
          board[(2, 5)])
    print("3: ", board[(3, 0)], board[(3, 1)], board[(3, 2)], board[(3, 3)], board[(3, 4)],
          board[(3, 5)])
    print("4: ", board[(4, 0)], board[(4, 1)], board[(4, 2)], board[(4, 3)], board[(4, 4)],
          board[(4, 5)])
    print("5: ", board[(5, 0)], board[(5, 1)], board[(5, 2)], board[(5, 3)], board[(5, 4)],
          board[(5, 5)])
    print("---", "0", "1", "2", "3", "4", "5")
    print("---", "-", "-", "-", "-", "-", "-")
    return None
'''