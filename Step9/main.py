def tribonacci(signature, n):
    # on déclare notre tableau pour le stockage
    arr = []
    # on boucle jusqu'à n - 1
    for i in range(n):
        # les 3 premiers nombres seront forcément la signature
        # append permet de rajouter une case à notre tableau
        if i < 3:
            arr.append(signature[i])
        # on calcule la sommme des 3 derniers nombres et on l'ajoute à notre tableau
        else:
            arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
    return arr