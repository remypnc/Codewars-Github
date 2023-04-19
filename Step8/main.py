def solution(n):
    # Création d'un tableau de tuples avec les valeurs des chiffres romains
    # On y stock aussi tous les cas spéciaux (par ex: '4' et '9') pour avoir leurs valeurs prédéfinis.
    arr = [('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50), ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), ('CM', 900), ('M', 1000)]
    roman = ""
    
    # On inverse la liste pour commencer par la dernière valeur du tableau
    for num, value in reversed(arr):
        # Lorsque la valeur actuelle est plus grande ou égale à 'n' 
        while n >= value:
            # Ajoute le chiffre romain actuel au résultat
            roman += num       
            # Soustrais la valeur actuelle de la valeur restante
            n -= value
    
    return roman

# Pour cela, j'ai suivi ma logique des calculs : 
# - avec des valeurs prédéfinis de tous les cas spéciaux car trop complexe de faire "if I before V and I before X",
# - sachant que les chiffres romains se lisent du plus grand au plus petit (reversed)
# Du coup, le résultat est forcément supérieur à la valeur du chiffre romain actuel,
# et ainsi on calcule le résultat
