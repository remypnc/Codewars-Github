# on check si chaque block ne contient bien qu'une seule fois chaque chiffre
def check_block(board, x, y):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    # on parcours notre tableau de référence afin de tester tous les chiffres de 1 à 9
    for nb in arr:
        count = 0
        # on parcours un block de 3 par 3 en partant de (x,y) (coordonnées du coin supérieur gauche)
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                # on compte le nombre d'occurence de chaque chiffres
                if board[i][j] == nb:
                    count += 1
        # si le nombre d'occurence d'un chiffre est != de 1 alors on return False
        if count != 1:
            return False
    return True

# on check si la grille contient un 0
def check_for_0(board):
    for line in board:
        for digit in line:
            if digit == 0:
                return False
    return True

def valid_solution(board):
    # on déclare notre tableau de référence qui contient tous les chiffres que doit contenir chaque lignes, colonnes et blocks selon les règles du sudoku
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    # on check si la grille contient un 0
    if check_for_0(board) == False:
        return False

    # on compte le nombre d'occurence de chaque chiffre dans chaque ligne si != 1 alors on return False
    for digit in arr:
        for line in board:
            # line.count(1) (par exemple) permet d'obtenir le nombre d'occurence du chiffre 1 dans chaque ligne
            if line.count(digit) != 1:
                return False

    # on compte le nombre d'occurence de chaque chiffre dans chaque colonne si != 1 alors on return False
    for nb in arr:
        for i in range(9):
            count = 0
            for line in board:
                if nb == line[i]:
                    count += 1
            if count != 1:
                return False

    # on appelle la fonction qui check les block en envoyant les coordonnées du coin supérieur gauche du block
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            if check_block(board, x, y) == False:
                return False

    # si la grille a passé tous les tests alors on peut return True
    return True