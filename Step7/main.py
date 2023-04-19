def in_asc_order(arr):
    # on compte de 0 à la taille de arr - 1 car on compare arr[i + 1]
    for i in range(len(arr) - 1):
        # on compare arr[0] et arr[1] puis arr[1] et arr[2] etc..
        # si la 1ère valeur est plus grande que la seconde alors le tableau n'est pas trié
        if arr[i] > arr[i + 1]:
            return False
    # si on a parcouru tout le tableau sans trouver d'erreur alors le tableau est trié
    return True