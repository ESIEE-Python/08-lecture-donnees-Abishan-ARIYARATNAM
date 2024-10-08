"""
Lecture de données
"""


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,mode='r',encoding='utf8') as f:
        l=f.readlines()
        l = [i.strip() for i in l]
        l = [i.split(";") for i in l]
        l = [[int(j) for j in i] for i in l]
    return l

def get_list_k(data, k):
    """
    prend en argument la liste de listes retournée par read_data() 
    et un indice k et retourne la kième liste
    """
    return data[k]

def get_first(l):
    """
    prend en argument une liste et retourne le premier élément de cette liste
    """
    return l[0]

def get_last(l):
    """
    prend en argument une liste et retourne le dernier élément de cette liste
    """
    return l[-1]

def get_max(l):
    """
    prend en argument une liste et retourne le maximum de cette liste
    """
    return max(l)

def get_min(l):
    """
    prend en argument une liste et retourne le minimum de cette liste
    """
    return min(l)

def get_sum(l):
    """
    prend en argument une liste et retourne la somme de cette liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Programme principal permettant de tester les fonctions
    """
    data = read_data(FILENAME)
    print(data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
