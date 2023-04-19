def basic_op(operator, value1, value2):
    # If divide 0, it's not possible so :
    if value2 == 0 and operator == '/':
        return 'error'
    # On regarde quel opérateur est-ce qu'on reçoit et on fait applique l'opération en fonction
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '/': 
        return value1 / value2
    elif operator == '*':
        return value1 * value2