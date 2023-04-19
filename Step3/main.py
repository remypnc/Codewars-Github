def monkey_count(n):
    # on créer un tableau vide pour le stockage
    x = [0] * n
    # on fait une boucle de 0 à n
    # on stocke i + 1 car la boucle va de 0 à n - 1
    for i in range(n):
        x[i] = i + 1
    return x