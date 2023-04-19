# on check la direction du bateau
# si la case de droite contient un 1 on return 'r' pour right
# si la case du bas contient un 1 on return 'b' pour bottom
# sinon on return 0
    # ce qui voudra dire que le bateau est de taille 1
def check_dir(field, x, y):
    if x + 1 < 10:
        if field[y][x + 1] == 1:
            return 'r'
    if y + 1 < 10:
        if field[y + 1][x] == 1:
            return 'b'
    return '0'

# on check si le bateau que l'on examine est en collision avec un autre bateau déjà trouvé
# on regarde toutes les cases autour de la case actuelle sauf celle d'ou l'on vient
    # si le bateau est vertical on ne regarde pas la case du haut qui appartiendrait au meme bateau
    # si le bateau est horizontal on ne regarde pas la case de gauche
# à chaque fois que l'on check une case on vérifie d'abord si elle n'est pas out of range
def check_collisions(field, x, y, dir):
    if dir != 'r':
        if x - 1 >= 0:
            if field[y][x - 1] == 2:
                return True
    if x + 1 < 10:
        if field[y][x + 1] == 2:
            return True
    if dir != 'b':
        if y - 1 >= 0:
            if field[y - 1][x] == 2:
                return True
    if y + 1 < 10:
        if field[y + 1][x] == 2:
            return True

    if x - 1 >= 0 and y - 1 >= 0:
        if field[y - 1][x - 1] == 2:
            return True
    if x + 1 < 10 and y - 1 >= 0:
        if field[y - 1][x + 1] == 2:
            return True
    if x - 1 >= 0 and y + 1 < 10:
        if field[y + 1][x - 1] == 2:
            return True
    if x + 1 < 10 and y + 1 < 10:
        if field[y + 1][x + 1] == 2:
            return True
    return False

# la fonction check_ship permet de parcourir le bateau afin de connaître sa taille
# au fur et à mesure on le marque en remplaçant le 1 par un 2 afin de savoir que l'on est déjà passé par là
def check_ship(field, x, y, dir):
    count = 0
    # si le bateau est vertical on incrémente y afin de 'descendre' dans le field
        # on incrémente y tant que l'on trouve un 1 (qui correspond à la suite du bateau) et que y ne sort pas des limites du terrain
    # on marque la case par un 2 et on incrémente 'count' afin de connaître sa taille
    # à chaque fois que l'on check un case on regarde si elle n'est pas en collision avec un bateau déjà connu
    if dir == 'b':
        while y < 10 and field[y][x] == 1:
            if check_collisions(field, x, y, dir) == True:
                return -1
            field[y][x] = 2
            count += 1
            y += 1
    else:
        while x < 10 and field[y][x] == 1:
            if check_collisions(field, x, y, dir) == True:
                return -1
            field[y][x] = 2
            count += 1
            x += 1
    return count
        
    
def validate_battlefield(field):
    # on créer le tableau de référence: 4 ship of size 1, 3 ship of size 2 etc..
    ship_amount = [(4, 1), (3, 2), (2, 3), (1, 4)]
    # tableau pour stocker le nombre de bateau trouvé
    ship_count = [0, 0, 0, 0]
    
    # on parcours notre battlefield
    for y in range(0, len(field)):
        for x in range(0, len(field[y])):
            # si on trouve le début d'un bateau on commence les opérations
            if field[y][x] == 1:
                # on appelle check_dir pour savoir si le bateau est vertical ou horizontal
                dir = check_dir(field, x, y)
                # si dir == 0 alors le bateau est de taille 1
                if dir != '0':
                    # on appelle la fonction check_ship et on récupère la taille du bateau trouvé
                    count = check_ship(field, x, y, dir)
                    # si count > à 4 le bateau est trop grand, si count < à 0 on a détecté un erreur
                    # sinon on compte le bateau trouvé
                    if count > 4 or count < 0:
                        return False
                    else:
                        ship_count[count - 1] += 1
                else:
                    # si on a trouvé un bateau de taille 1 on le marque et on le compte
                    field[y][x] = 2
                    ship_count[0] += 1
                    if check_collisions(field, x, y, dir) == True:
                        return False
    
    # on vérifie qu'on a bien trouvé le bon nombre de bateau
    for i in range(4):
        if ship_count[i] != ship_amount[i][0]:
            return False
    return True