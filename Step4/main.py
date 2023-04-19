# première solution 'brutforce'
"""
def shortcut( s ):
    s = s.replace('a', '')
    s = s.replace('e', '')
    s = s.replace('i', '')
    s = s.replace('o', '')
    s = s.replace('u', '')
    return s
"""
# on créer un tableau pour stocker les char que l'on veut suppr
# on parcour ce tableau et on applique la fonction replace sur chaque char
# dans notre cas la fonction replace parcour toute la string 's' en remplaçant les char par rien
def shortcut( s ):
    tab = ['a','e','i','o','u']
    for i in tab:
        s = s.replace(i, '')
    return s