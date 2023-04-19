def is_triangle(a, b, c):
    # on check d'abord si un des côtés est <= à 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # on check simplement si la somme de 2 côté est bien supérieure à la longueur du 3ème
    if a < b + c and b < a + c and c < a + b:
        return True
    
    return False