import copy

def est_valide(x, y, dimensions, echiquier):
    """
    Vérifie si la position (x, y) est valide sur l'échiquier de dimensions spécifiées et si la case est vide.
    """
    return 0 <= x < dimensions and 0 <= y < dimensions and echiquier[x][y] == 'vide'

def trouver_parcours_hamiltonien(dimensions):
    """
    Trouve un parcours hamiltonien pour le cavalier sur un échiquier de dimensions spécifiées.
    """
    # Initialiser l'échiquier avec toutes les cases vides.
    echiquier = [['vide' for _ in range(dimensions)] for _ in range(dimensions)]

    # Demander la position initiale du cavalier à l'utilisateur.
    x = int(input("Entrez la position en x du cavalier : "))
    y = int(input("Entrez la position en y du cavalier : "))

    # Marquer la position initiale comme étant visitée.
    echiquier[x][y] = 'plein'

    # Initialiser le parcours avec la position initiale.
    parcours = [(x, y)]

    # Définir les déplacements possibles du cavalier en L.
    deplacements = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    # Fonction récursive pour trouver un parcours hamiltonien.
    def trouver_parcours_recursif(x, y, etape_actuelle):
        # Si toutes les étapes ont été parcourues, on a trouvé un parcours hamiltonien.
        if etape_actuelle == dimensions**2:
            # Le plateau est en n * n cases donc n au carré
            return True

        # Essayer chaque déplacement possible.
        for dx, dy in deplacements:      #dx et dy pour 'déplacement x ou y'
            nx, ny = x + dx, y + dy      #nx et ny pour 'nouveau x ou y'
            if est_valide(nx, ny, dimensions, echiquier):
                # Marquer la case comme étant visitée et ajouter la position au parcours.
                echiquier[nx][ny] = 'plein'
                parcours.append((nx, ny))
                if trouver_parcours_recursif(nx, ny, etape_actuelle+1):
                    return True
                # Si on n'a pas trouvé de parcours hamiltonien, enlever la dernière position du parcours et marquer la case comme vide.
                echiquier[nx][ny] = 'vide'
                parcours.pop()

        return False

    # Trouver un parcours hamiltonien à partir de la position initiale.
    if trouver_parcours_recursif(x, y, 1):
        print("Parcours hamiltonien trouvé :")
        for i in range(dimensions):
            for j in range(dimensions):
                print(parcours.index((i,j))+1, end="\t")
            print("\n")
    else:
        print("Aucun parcours hamiltonien trouvé.")

    # Afficher l'ordre de parcours de chaque case sous forme de plateau.
    plateau = copy.deepcopy(echiquier)
    for i, (x, y) in enumerate(parcours):
        plateau[x][y] = str(i+1)

    print("Ordre de parcours de chaque case :")
    for ligne in plateau : print(ligne)

dimensions = int(input("Entrez la dimension de l'échiquier : "))
trouver_parcours_hamiltonien(dimensions)


# □