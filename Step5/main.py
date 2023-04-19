def square_digits(num):
    # on convertit num en string pour pouvoir le split
    n = str(num)
    # on split n en le stockant dans un tableau
    num = [int(i) for i in n]
    # on déclare notre var pour stocker le résultat
    res = ""

    # on parcour notre tableau et on ajoute le carré de chaque nombre à notre string res
    for i in num:
        res += str(i ** 2)
    return int(res)