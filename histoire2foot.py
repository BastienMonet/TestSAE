"""Fichier source de la SAE 1.01 partie 1
    Historique des matchs de football internationaux
    """
import csv
from datetime import datetime

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire des tests
# ---------------------------------------------------------------------------------------------
    
# exemples de matchs de foot
match1 = ('2021-06-28', 'France', 'Switzerland', 3, 3, 'UEFA Euro', 'Bucharest', 'Romania', True)
match2 = ('1998-07-12', 'France', 'Brazil', 3, 0, 'FIFA World Cup', 'Saint-Denis', 'France', False)
match3 = ('1978-04-05', 'Germany', 'Brazil', 0, 1, 'Friendly', 'Hamburg', 'Germany', False)

# exemples de listes de matchs de foot
liste1 = [('1970-04-28', 'France', 'Bulgaria', 1, 1, 'Friendly', 'Rouen', 'France', False), 
        ('1970-04-28', 'France', 'Romania', 2, 0, 'Friendly', 'Reims', 'France', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste2 = [('1901-03-09', 'England', 'Northern Ireland', 3, 0, 'British Championship', 'Southampton', 'England', False), 
        ('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False), 
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False), 
        ('1902-05-03', 'England', 'Scotland', 2, 2, 'British Championship', 'Birmingham', 'England', False), 
        ('1903-02-14', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Wolverhampton', 'England', False), 
        ('1903-03-02', 'England', 'Wales', 2, 1, 'British Championship', 'Portsmouth', 'England', False), 
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1905-02-25', 'England', 'Northern Ireland', 1, 1, 'British Championship', 'Middlesbrough', 'England', False), 
        ('1905-03-27', 'England', 'Wales', 3, 1, 'British Championship', 'Liverpool', 'England', False), 
        ('1905-04-01', 'England', 'Scotland', 1, 0, 'British Championship', 'London', 'England', False), 
        ('1907-02-16', 'England', 'Northern Ireland', 1, 0, 'British Championship', 'Liverpool', 'England', False), 
        ('1907-03-18', 'England', 'Wales', 1, 1, 'British Championship', 'London', 'England', False), 
        ('1907-04-06', 'England', 'Scotland', 1, 1, 'British Championship', 'Newcastle', 'England', False), 
        ('1909-02-13', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Bradford', 'England', False), 
        ('1909-03-15', 'England', 'Wales', 2, 0, 'British Championship', 'Nottingham', 'England', False), 
        ('1909-04-03', 'England', 'Scotland', 2, 0, 'British Championship', 'London', 'England', False)
        ]
liste3 = [('1901-03-30', 'Belgium', 'France', 1, 2, 'Friendly', 'Bruxelles', 'Belgium', False),
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False),
        ('1903-04-04', 'Brazil', 'Argentina', 3, 0, 'Friendly', 'Sao Paulo', 'Brazil', False),
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste4 = [('1978-03-19', 'Argentina', 'Peru', 2, 1, 'Copa Ramón Castilla', 'Buenos Aires', 'Argentina', False), 
        ('1978-03-29', 'Argentina', 'Bulgaria', 3, 1, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-04-05', 'Argentina', 'Romania', 2, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-05-03', 'Argentina', 'Uruguay', 3, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-01', 'Germany', 'Poland', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-02', 'Argentina', 'Hungary', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-02', 'France', 'Italy', 1, 2, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-02', 'Mexico', 'Tunisia', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-03', 'Austria', 'Spain', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-03', 'Brazil', 'Sweden', 1, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-03', 'Iran', 'Netherlands', 0, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-03', 'Peru', 'Scotland', 3, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Argentina', 'France', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-06', 'Germany', 'Mexico', 6, 0, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Hungary', 'Italy', 1, 3, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-06', 'Poland', 'Tunisia', 1, 0, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-07', 'Austria', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-07', 'Brazil', 'Spain', 0, 0, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-07', 'Iran', 'Scotland', 1, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-07', 'Netherlands', 'Peru', 0, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-10', 'Argentina', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-10', 'France', 'Hungary', 3, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-10', 'Germany', 'Poland', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-11', 'Austria', 'Brazil', 0, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-11', 'Iran', 'Peru', 1, 4, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-11', 'Netherlands', 'Scotland', 2, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-11', 'Spain', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-14', 'Argentina', 'Poland', 2, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-14', 'Austria', 'Netherlands', 1, 5, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-14', 'Brazil', 'Peru', 3, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-14', 'Germany', 'Italy', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Argentina', 'Brazil', 0, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-18', 'Austria', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Germany', 'Netherlands', 2, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-18', 'Peru', 'Poland', 0, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Argentina', 'Peru', 6, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-21', 'Austria', 'Germany', 3, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-21', 'Brazil', 'Poland', 3, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Italy', 'Netherlands', 1, 2, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-24', 'Brazil', 'Italy', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-25', 'Argentina', 'Netherlands', 3, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False)
]

# -----------------------------------------------------------------------------------------------------
# listes des fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

# Fonctions à implémenter dont les tests sont fournis

def lire_liste4(liste4): #juste un test
    res=[]
    res= liste4
    return res


def equipe_gagnante(match):
    """retourne le nom de l'équipe qui a gagné le match. Si c'est un match nul on retourne None

    Args:
        match (tuple): un match

    Returns:
        str: le nom de l'équipe gagnante (ou None si match nul)
    """    
    if match[3]>match[4]:
        res= match[1]
    elif match[3] == match[4]:
        res = None
    else:
        res = match [2]
    return res

#print(equipe_gagnante(match1))

def victoire_a_domicile(match):
    """indique si le match correspond à une victoire à domicile

    Args:
        match (tuple): un match

    Returns:
        bool: True si le match ne se déroule pas en terrain neutre et que l'équipe qui reçoit a gagné
    """    
    if match[8] == True and match[3]>match[4]:
        res= True
    else:
        res= False
    return res

#print(victoire_a_domicile(match1))
#print(victoire_a_domicile(match2))
#print(victoire_a_domicile(match3))


def nb_buts_marques(match):
    """indique le nombre total de buts marqués lors de ce match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de buts du match 
    """    
    return match[3] + match[4]

#print(nb_buts_marques(match1))
#print(nb_buts_marques(match2))
#print(nb_buts_marques(match3))


def matchs_ville(ville, liste_matchs):
    """retourne la liste des matchs qui se sont déroulés dans une ville donnée
    
    Args:
        liste_matchs (list): une liste de matchs
        ville (str): le nom d'une ville

    Returns:
        list: la liste des matchs qui se sont déroulé dans la ville ville    
    """
    res=[]
    for i in range(len(liste_matchs)):
        if ville in liste_matchs[i][6]:
            res.append(liste_matchs[i])
    return res

#print(matchs_ville("Lyon",liste1))
#print(matchs_ville("Liverpool",liste2))


def nombre_moyen_buts(liste_matchs, nom_competition):
    """retourne le nombre moyen de buts marqués par match pour une compétition donnée

    Args:
        liste_matchs (list): une liste de matchs
        nom_competition (str): le nom d'une compétition
    
    Returns:
        float: le nombre moyen de buts par match pour la compétition
    """
    somme=0
    cpt=0
    for i in range(len(liste_matchs)):
        if nom_competition in liste_matchs[i][5]:
            somme += int(liste_matchs[i][3]) + int(liste_matchs[i][4])
            cpt += 1 
    return somme / cpt

#print(nombre_moyen_buts(liste2, "British Championship"))

def nombre_moyen_buts_sans_argument(liste_matchs):
    """retourne le nombre moyen de buts marqués dans toute la liste

    Args:
        liste_matchs (list): une liste de matchs
    
    Returns:
        float: le nombre moyen de buts par match pour la compétition
    """
    somme=0
    cpt=0
    for i in range(len(liste_matchs)):
            somme += int(liste_matchs[i][3]) + int(liste_matchs[i][4])
            cpt += 1 
    return somme / cpt

#print(nombre_moyen_buts_tout(liste2))



def est_bien_trie(liste_matchs):
    """vérifie si une liste de matchs est bien trié dans l'ordre chronologique
       puis pour les matchs se déroulant le même jour, dans l'ordre alphabétique
       des équipes locales

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        bool: True si la liste est bien triée et False sinon
    """ 
    cpt=0
    for i in range(1,len(liste_matchs)):
        if liste_matchs[i-1][0] >= liste_matchs[i][0]:
            if liste_matchs[i][0] == liste_matchs[i-1][0] and liste_matchs[i-1][1] <= liste_matchs[i][1]:
                cpt+=1
        else: 
            cpt+=1
    if cpt == len(liste_matchs)-1:
        return True
    else:
        return False

#print(est_bien_trie(liste1))
#print(est_bien_trie(liste2))


def fusionner_matchs(liste_matchs1, liste_matchs2):
    """Fusionne deux listes de matchs triées sans doublons en une liste triée sans doublon
    sachant qu'un même match peut être présent dans les deux listes

    Args:
        liste_matchs1 (list): la première liste de matchs
        liste_matchs2 (list): la seconde liste de matchs

    Returns:
        list: la liste triée sans doublon comportant tous les matchs de liste_matchs1 et liste_matchs2
    """
    res=[]
    ind1 = 0 
    ind2 = 0 
    while ind1 < len(liste_matchs1) and ind2 < len(liste_matchs2) :
        if liste_matchs1[ind1] < liste_matchs2[ind2]:
            if liste_matchs1[ind1] not in res:
                res.append(liste_matchs1[ind1])
            ind1+=1
        else:
            if liste_matchs2[ind2] not in res:
                res.append(liste_matchs2[ind2])
            ind2+=1
    
    if ind1 < len(liste_matchs1):
        while ind1 < len(liste_matchs1):
            if liste_matchs1[ind1] not in res:
                res.append(liste_matchs1[ind1])
            ind1+=1

    
    if ind2 < len(liste_matchs2):
        while ind2 < len(liste_matchs2):
            if liste_matchs2[ind2] not in res:
                res.append(liste_matchs2[ind2])
            ind2+=1
    return res


#print(fusionner_matchs(liste2,liste3))



def resultats_equipe(liste_matchs, equipe):
    """donne le nombre de victoire, de matchs nuls et de défaites pour une équipe donnée

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        tuple: un quadriplet d'entiers contenant, l'équipe choisi, le nombre de victoires, nuls et défaites de l'équipe
    """    
    victoire=0
    defaites=0
    nul=0
    for i in range(len(liste_matchs)):
        if liste_matchs[i][1] == equipe:
            if liste_matchs[i][3] > liste_matchs[i][4]:
                victoire+=1      
            elif liste_matchs[i][3] < liste_matchs[i][4]:
                defaites+=1
            else:
                nul+=1
        elif liste_matchs[i][2]:
            if liste_matchs[i][3] < liste_matchs[i][4]:
                victoire+=1
            elif liste_matchs[i][3] > liste_matchs[i][4]:
                defaites+=1
            else:
                nul+=1
    return equipe, victoire, defaites, nul 

#print(resultats_equipe(liste1,"Romania"))

def ecart_score(liste_matchs):
    """Retourne une liste des écart relatif du nombre de but d'une liste de match

    Args:
        liste_matchs (tuple): une liste des matchs

    Returns:
        list: la liste des écarts de but pendant un match
    """
    ecart=0
    rep=[]
    for i in range(len(liste_matchs)):
        if liste_matchs[i][3] >= liste_matchs[i][4]:
            ecart =liste_matchs[i][3] - liste_matchs[i][4]
            rep.append(ecart)
        elif liste_matchs[i][3] < liste_matchs[i][4]:
            ecart =liste_matchs[i][4] - liste_matchs[i][3]
            rep.append(ecart)
    return rep


#print(ecart_score(liste1))


def plus_gros_scores(liste_matchs):
    """retourne la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs avec le plus grand écart entre vainqueur et perdant
    """   
    rep=[]
    max_ecart = 0
    liste_ecart = ecart_score(liste_matchs)
    for i in range(len(liste_ecart)):
        if liste_ecart[i] > max_ecart:
            max_ecart = liste_ecart[i]
    for j in range(len(liste_ecart)):
        if liste_ecart[j] == max_ecart:
            rep.append(liste_matchs[j])
    return rep

#print(plus_gros_scores(liste1))
#print(plus_gros_scores(liste2))
#print(plus_gros_scores(liste3))



def liste_des_equipes(liste_matchs):
    """retourne la liste des équipes qui ont participé aux matchs de la liste
    Attention on ne veut voir apparaitre le nom de chaque équipe qu'une seule fois

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des équipes ayant jouer des matchs
    """
    rep=[]
    for i in range(len(liste_matchs)):
        if liste_matchs[i][1] not in rep:
            rep.append(liste_matchs[i][1])
        if liste_matchs[i][2] not in rep:
            rep.append(liste_matchs[i][2])
    return rep

#print(liste_des_equipes(liste1))

###
def equipe_gagnante_liste(liste_matchs):
    """retourne les noms des équipes qui ont gagné un match. Si c'est un match nul on retourne 0

    Args:
        liste_match (tuple): une liste de matchs

    Returns:
        list: le nom des équipes gagnantes
    """
    res=[]
    for i in range(len(liste_matchs)):    
        if liste_matchs[i][3]>liste_matchs[i][4]:
            res.append(liste_matchs[i][1])
        elif liste_matchs[i][3]<liste_matchs[i][4]:
            res.append(liste_matchs[i][2])
        else:
            res.append(0)
    return res

#print(equipe_gagnante_liste(liste2))
#print(equipe_gagnante_liste(liste1))
#print(equipe_gagnante_liste(liste4))
#assert equipe_gagnante_liste(liste1) == [0, "France", "France", "France"]


def premiere_victoire(liste_matchs, equipe):
    """retourne la date de la première victoire de l'equipe. Si l'equipe n'a jamais gagné de match on retourne None

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        str: la date de la première victoire de l'equipe
    """    
    for i in range(len(equipe_gagnante_liste(liste_matchs))):
        if equipe_gagnante_liste(liste_matchs)[i] == equipe:
            return liste_matchs[i][0]
    return None
        
#print(premiere_victoire(liste1,"Romania"))
assert premiere_victoire(liste2, "England") == "1901-03-09"
###
###
def nb_matchs_sans_defaites(liste_matchs, equipe):
    """retourne le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée.

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        int: le plus grand nombre de matchs consécutifs sans défaite du pays nom_pays
    """
    max=0
    cpt=0
    for i in range(len(equipe_gagnante_liste(liste_matchs))):
        if equipe_gagnante_liste(liste_matchs)[i] == equipe:
            cpt+=1
        if cpt > max:
            max=cpt
        else:
            cpt=0
    return max

#print(nb_matchs_sans_defaites(liste2, "England"))
#print(nb_matchs_sans_defaites(liste1, "France"))
#print(nb_matchs_sans_defaites(liste4, "Argentina"))
assert nb_matchs_sans_defaites(liste2, "England") == 2

def charger_matchs(nom_fichier):
    """charge un fichier de matchs donné au format CSV en une liste de matchs

    Args:
        nom_fichier (str): nom du fichier CSV contenant les matchs

    Returns:
        list: la liste des matchs du fichier
    """    
    res = []
    fic = open(nom_fichier,'r',encoding='utf8')
    fic.readline()
    for ligne in fic:
        l_champs = ligne.split(",")
        res.append((l_champs[0], l_champs[1], (l_champs[2]), int(l_champs[3]), int(l_champs[4]),l_champs[5], l_champs[6], (l_champs[7]), (l_champs[8])))
    fic.close()
    return res


def sauver_matchs(liste_matchs,nom_fichier):
    """sauvegarde dans un fichier au format CSV une liste de matchs

    Args:
        liste_matchs (list): la liste des matchs à sauvegarder
        nom_fichier (str): nom du fichier CSV

    Returns:
        None: cette fonction ne retourne rien
    """    
    fic = open(nom_fichier, 'w',encoding="utf8")
    fic.write("date,home team,away team,home score,tournament,city,country,neutral\n")
    for mat in liste_matchs:
        fic.write(mat[0]+","+mat[1]+","+mat[2]+","+str(mat[3])+","+str(mat[4])+","+mat[5]+","+mat[6]+","+mat[7]+","+mat[8])
    fic.close()
    return None


def sauver_charger(liste_matchs,fichier):
    rep = sauver_matchs(liste_matchs,fichier)
    res = charger_matchs(fichier)
    return rep,res

# Fonctions à implémenter dont il faut également implémenter les tests
def equipe_perdente_liste(liste_matchs):
    """retourne les noms des équipes qui ont Perdu un match. Si c'est un match nul on retourne 0

    Args:
        liste_match (tuple): une liste de matchs

    Returns:
        list: le nom des équipes gagnantes
    """
    res=[]
    for i in range(len(liste_matchs)):    
        if liste_matchs[i][3]<liste_matchs[i][4]:
            res.append(liste_matchs[i][1])
        elif liste_matchs[i][3]>liste_matchs[i][4]:
            res.append(liste_matchs[i][2])
        else:
            res.append(0)
    return res

#print(equipe_perdente_liste(liste2))
#print(equipe_perdente_liste(liste1))

def plus_de_victoires_que_defaites(liste_matchs, equipe):
    """vérifie si une équipe donnée a obtenu plus de victoires que de défaites
    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        bool: True si l'equipe a obtenu plus de victoires que de défaites
    """
    nb_gagne=0
    nb_perd=0
    for i in range(len(equipe_gagnante_liste(liste_matchs))):
        if equipe_gagnante_liste(liste_matchs)[i] == equipe:
            nb_gagne+=1
    for i in range(len(equipe_perdente_liste(liste_matchs))):
        if equipe_perdente_liste(liste_matchs)[i] == equipe:
            nb_perd+=1
    if nb_gagne > nb_perd:
        return True
    else:
        return False

#print(plus_de_victoires_que_defaites(liste2, "Scotland"))
#print(plus_de_victoires_que_defaites(liste1, "France"))

def matchs_spectaculaires(liste_matchs):
    """retourne la liste des matchs les plus spectaculaires, c'est à dire les
    matchs dont le nombre total de buts marqués est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs les plus spectaculaires
    """
    max=0
    total_but=0
    rep=[]
    for i in range(len(liste_matchs)):
        total_but=liste_matchs[i][3] + liste_matchs[i][4]
        if total_but > max:
            max=total_but
    for j in range(len(liste_matchs)):
        total_but=liste_matchs[j][3] + liste_matchs[j][4]
        if total_but == max:
            rep.append(liste_matchs[j])
    return rep

#print(matchs_spectaculaires(liste2))




def liste_nbre_defaite(liste_matchs):
    """créer un liste qui retourne le nombre des défaites de chaque équipe

    Args:
        liste_matchs (list): Une liste des matchs

    Returns:
        Liste: Retourne le nombre des défaites de chaque équipe
    """    
    defaite_equipe=[]
    ind1 = 0
    ind2 = 0
    nbre_defaite=0
    while ind1 < len(equipe_perdente_liste(liste_matchs)) and ind2 < len(liste_des_equipes(liste_matchs)):
        if equipe_perdente_liste(liste_matchs)[ind1] == liste_des_equipes(liste_matchs)[ind2]:
            nbre_defaite+=1
        ind1+=1
        if ind1 > len(equipe_perdente_liste(liste_matchs))-1:
            ind2+=1
            defaite_equipe.append(nbre_defaite)
            nbre_defaite=0
            ind1=0
    return defaite_equipe

#print(liste_nbre_defaite(liste1))
#print(liste_nbre_defaite(liste2))


def meilleures_equipes(liste_matchs):
    """retourne la liste des équipes de la liste qui ont le plus petit nombre de defaites

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des équipes qui ont le plus petit nombre de defaites
    """
    rep=[]
    min=float("+inf")
    for i in range(len(liste_nbre_defaite(liste_matchs))):
        if liste_nbre_defaite(liste_matchs)[i] < min:
            min=liste_nbre_defaite(liste_matchs)[i]
    for j in range(len(liste_nbre_defaite(liste_matchs))):
        if liste_nbre_defaite(liste_matchs)[j] == min:
            rep.append(liste_des_equipes(liste_matchs)[j])
    return rep


#print(meilleures_equipes(liste2))
assert meilleures_equipes(liste2) == ['England']


#def date_devient_int(date):   


 
 
    #indice="0123456789"
    #for elt in date:
        #if elt == date:

"""def requête_par_date(liste_matchs,date_debut,date_fin):
    res=[]
    test=None
    for i in range(len(liste_matchs)):
        if liste_matchs[i][0] >= date_debut and liste_matchs[i][0] <= date_fin:
            res.append(liste_matchs)
    return res

print(requête_par_date(liste1,"1", "100000000"))"""


def nb_buts_marques_liste(liste_matchs):
    """indique le nombre total de buts marqués dans toute la liste

    Args:
        match (tuple): une liste de matchs

    Returns:
        int: le nombre de buts du match 
    """
    res=0
    for i in range(len(liste_matchs)):
        res += liste_matchs[i][3] + liste_matchs[i][4]
    return res

#print(nb_buts_marques_liste(liste1))
assert nb_buts_marques_liste(liste1) == 11





################################"AIMEZ VOUS LES COPIER COLLER?"#############################




def liste_but(liste_matchs):
    """Retourne une liste des but totaux marqué lors d'un match 

    Args:
        liste_matchs (tuple): une liste des matchs

    Returns:
        list: la liste du nombre total de but pendant un match
    """
    but=0
    rep=[]
    for i in range(len(liste_matchs)):
            but =liste_matchs[i][3] + liste_matchs[i][4]
            rep.append(but)
    return rep

#print(liste_but(liste1))


def max_but(liste_matchs):
    """retourne la liste des matchs dont le total des but marquer est le plus élever

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs avec le total de but le plus élever
    """   
    rep=[]
    max = 0
    liste_max = liste_but(liste_matchs)
    for i in range(len(liste_max)):
        if liste_max[i] > max:
            max = liste_max[i]
    for j in range(len(liste_max)):
        if liste_max[j] == max:
            rep.append(liste_matchs[j])
    return rep

#print(max_but(liste1))


def min_but(liste_matchs):
    """retourne la liste des matchs dont le total des but marquer est le plus faible

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs avec le total de but le plus faible
    """   
    rep=[]
    min = float("+inf")
    liste_min = liste_but(liste_matchs)
    for i in range(len(liste_min)):
        if liste_min[i] < min:
            min = liste_min[i]
    for j in range(len(liste_min)):
        if liste_min[j] == min:
            rep.append(liste_matchs[j])
    return rep

#print(min_but(liste1))

def liste_des_tournois(liste_matchs):
    """retourne la liste des tournoi des matchs de la liste 
    Attention "Friendly" n'est pas un tournoi

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des tournois
    """
    rep=[]
    for i in range(len(liste_matchs)):
        if liste_matchs[i][5] not in rep and liste_matchs[i][5] != 'Friendly':
            rep.append(liste_matchs[i][5])
    return rep

#print(liste_des_tournois(liste1))


def liste_des_localisations(liste_matchs):
    """retourne la liste des villes suivi des pays de la liste 
    Attention "Friendly" n'est pas un tournoi

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des villes et des pays
    """
    rep=[]
    for i in range(len(liste_matchs)):
        if liste_matchs[i][6] not in rep:
            rep.append(liste_matchs[i][6])
            rep.append(liste_matchs[i][7])
            rep.append("/")
    return rep

#print(liste_des_localisations(liste1))