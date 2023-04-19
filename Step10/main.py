# fonction pour calculer le score d'un brelan
def countscore(n):
    if n != 1:
        return n * 100
    else:
        return 1000

# fonction pour calculer le score des 1 et 5 seuls
def countsingle(n, x):
    if n == 1:
        return 100 * x
    else:
        return 50 * x

def score(dice):
    result = 0
    count = 0
    
    # on boucle de 1 à 6
    for i in range (1, 7):
        # on reset notre compteur
        count = 0
        # on parcour les dés que l'on reçoit en arg
        for x in dice:
            # on incrémente notre compteur pour chaque dés de même valeur 
            if i == x:
                count += 1
        # si on a au moins 3 occurence on ajoute le score du brelan
        if count >= 3:
            result += countscore(i)
        # si on est sur le 1 ou le 5 on calcul le score pour chaque occurence
        if (i == 1 or i == 5):
            if count > 3:
                result += countsingle(i, count - 3)
            elif count < 3:
                result += countsingle(i, count)
    return result