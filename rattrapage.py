# Déclarer une classe
class PointGeo:
    def __init__(self, nom: str, x: int, y: int):
        self.nom = nom  # Caractère représentant le nom du point
        self.x = x      # Coordonnée X du point
        self.y = y      # Coordonnée Y du point   
        
# Définir une fonction qui appelle 3 valeurs depuis l'utilisateur, constituant un ensemble de 3 variables définissant un point.
def creerPoint():
    nom = input('Entrez le nom du point: ')
    X = int(input('Entrez la coordonnée X du point: '))
    Y = int(input('Entrez la coordonnée Y du point: '))
    point = (nom, X, Y)
    return point 
#print(creerPoint()) 

# Définir une fonction qui prends 3 variables en Paramètres et qui les affiche proprement à l'écran.
def Affichage(nom:str, X:int, Y:int):
    print(f'Point {nom}, de coordonnées X = {X} et Y = {Y}')   
#Affichage('S', 12, 14)

# Définir une fonction qui reçoit 3 points avec leurs coordonnées, qui les affiches et qui vérifie l'alignement des points.
'''La fonction demande dans un premier temps d'entrer 3 fois de suite le nom d'un point avec ses coordonnées X et Y, puis les ajoute dans une liste. 
Ensuite les éléments de la liste sont affichés les uns après les autres sous la forme: nom du point, coordonnées X et Y. 
Enfin, si les points sont alignés, une phrase le spécifie. Pour cela, il a fallu déclarer quelques variables directement depuis les différents points dans la liste "points"
Je pourrai rendre mon code plus résilient en ajoutant une demande à mon utilisateur au tout début de la fonction (demander combien de points il souhaite déclarer), je pourrai 
aussi réduire un peu le nombre de lignes en utilisant plutôt la boucle for à la place de la boucle while (=préférence personnelle)'''
def Fonction():
    points = []
    i = 0
    while i < 3:
        #Point:
        nom = input('Entrez le nom du point: ')
        X = int(input('Entrez la coordonnée X du point: '))
        Y = int(input('Entrez la coordonnée Y du point: '))
        point = (nom, X, Y)
        points.append(point)
        i += 1
    #print(points)
        
    for point in points:
        nom, X, Y = point
        print(f'Point {nom} de coordonnées X = {X} et Y = {Y}')
    
    # On prends chaque ensemble d'éléments de la liste (chaque point) pour les attribuer à une variable chacune: chaque point constitue une variable.
    A = points[0]
    B = points[1]
    C = points[2]
    # On prends chaque coordonnée dans chaque ensemble d'éléments (chaque point) de la liste pour y appliquer la formule ci-après
    x0, y0 = A[1], A[2]
    x1, y1 = B[1], B[2]
    x2, y2 = C[1], C[2]
    
    if (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0):
        print('Aligné ? True')  
    else:
        print('Aligné ? False')            
                       
Fonction()
    
