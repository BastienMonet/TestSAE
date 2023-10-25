import histoire2foot
import csv


# ici votre programme principal
programme_tourne=True
Menu_principal=0



def formatage_liste_de(liste_res):
    liste_res.sort()
    for elt in liste_res:
        res=print(elt)   
    return res

def def_equipe(equipe,liste_simple):
    print("L'equipe", equipe, "a joué", histoire2foot.nombre_de_match_joué() ,"")


    


liste_simple=histoire2foot.charger_matchs("histoire1.csv")

intro_nom = False
intro_tuto = False
liste_res=""
nombre_matchs=None
nombre_but=None

# Ici vos fonctions dédiées aux interactions
print("\n////////////////////////////////////////////////////")
recherche = input("Bonjour, Bienvenue dans le terminal python match quel information recherchez vous?\n 1-Recherche relative aux equipes (tapper \"equipes\")\n 2-Recherche relative aux matchs (tapper \"matchs\")\n 3-Paramètrage des fichier (tapper \"parametres\")\n 4-Quitter (tapper quitter)\n")
while programme_tourne == True:
    if recherche == "equipes":
        Menu_principal=1
        while Menu_principal==1:
            recherche = input("Pour quel équipe voulez vous des informations? Si vous voulez connaitre le nom des equipes disponible, tappez \"noms\"\n")

            if recherche == "noms":
                liste_res=histoire2foot.liste_des_equipes(liste_simple)
                print(formatage_liste_de(liste_res))
                liste_res=""

            elif recherche in histoire2foot.liste_des_equipes(liste_simple):
                liste_complexe=histoire2foot.liste_de_match_par_equipe(recherche,liste_simple)
                print(formatage_liste_de(liste_complexe))
                nombre_matchs =histoire2foot.nombre_de_match_joué(recherche,liste_complexe)
                nombre_but= histoire2foot.nb_buts_marques_liste(liste_complexe)
                moyen_but= histoire2foot.nombre_moyen_buts_sans_argument(liste_complexe)
                ecart_but=histoire2foot.ecart_score
                premier_gagne=histoire2foot.premiere_victoire(liste_complexe, recherche)
                ecart_score=histoire2foot.ecart_score_tout(liste_complexe)
                print("L'equipe", recherche, "a joué",nombre_matchs ,"matchs depuis le debut, pour un total de", nombre_but,"but(s)\n -Nombre moyen de but:", moyen_but,"\n -date premier match gagné:",premier_gagne,"\n -ecart relatif de but:", ecart_score,"dans l'ordre" )

            else:
                print("Desoler, je ne connais pas l'équipe,", recherche)
    elif recherche == "matchs":
        a=2






















"""intro_nom = False
name = input("Bonjour, quel est votre nom?\n")
while intro_nom == False:
    print('est ce que votre nom est bien', name ,"?")
    is_it_true = input("\t//tapper \"oui\" si oui//\n")
    if is_it_true == "oui":
        print("enchanté" , name , "!")
        intro_nom = True
    else:
        name = input("Oh, alors quel est votre nom?\n")

while intro_nom == True and intro_tuto == False:
    is_it_true = False
    print("bienvenue dans le terminal python match ,ici tu peut retrouver tout tes matchs\nfavoris.")
    wait = input("\t//appuyer sur une touche pour continuer//")
    print("veux tu une petite introduction au fonctionalité présente?")
    is_it_true = input("\t//tapper \"oui\" si oui//")
    if is_it_true == 'oui':
        print("...")
    print("d'accord, alors amuse toi bien", name ,"!")
    print("\n")
    print("\n")
    intro_tuto = True

while intro_tuto == True:
    do = input("\t//.Alors, que voulez vous faire mtn?//\n" )
    print("\n")
    
    if do == 'lire':
        do = input("\t//Avec quels paramètre voulez vous lire?//\n")
        if do == 'tout':
            print("êtes vous sûr d'afficher TOUT les matchs")
            is_it_true = input("\t//tapper \"oui\" si oui//\n")
            if is_it_true == "oui":
                is_it_true == None
                print("\n")
                print(liste_simple)
                print("\n")
            else:
                print("non, désoler" ,name,", je ne connais pas cette commande dans \"lire\"")

    elif do == 'calcul':
        do = input("\t//Avec quel paramètre voulez vous Calculer?//\n")
        if do == 'tout':
            do = input("\t//Que voulez vous Calculer avec toutes les valeurs de tout les matchs?//\n")
            if do == 'totbut':
                liste_res=histoire2foot.nb_buts_marques_liste(liste_simple)
                print(formatage(liste_res))
            elif do == 'ecartbut':
                print("\n")
                print(histoire2foot.ecart_score(liste_simple))
                print("j'ose espéré que cela vous aura aidez :p")
                print("\n")
            elif do == 'moyenbut':
                print("\n")
                print(histoire2foot.nombre_moyen_buts_sans_argument(liste_simple))
                print("\n")
            elif do == 'maxbut':
                print("\n")
                print(histoire2foot.max_but(liste_simple))
                print("\n")
            elif do == 'minbut':
                print("\n")
                print(histoire2foot.min_but(liste_simple))
                print("\n")

            else:
                print("non, désoler" ,name,", je ne connais pas cette commande dans \"liste\"")

    elif do == 'liste':
        do = input("\t//Avec quel paramètre voulez vous Listez?//\n")
        if do == 'tout':
            do = input("\t//Que voulez vous Listez avec toutes les valeurs de tout les matchs?//\n")
            if do == 'equipe':
                print("\n")
                print(histoire2foot.liste_des_equipes(liste_simple))
                print("\n")
            elif do == 'localisation':
                print("\n")
                print(histoire2foot.liste_des_localisations(liste_simple))
                print("\n")
            elif do == 'tournoi':
                print("\n")
                print(histoire2foot.liste_des_tournois(liste_simple))
                print("\n")

            else:
                print("non, désoler" ,name,", je ne connais pas cette commande dans \"liste\"")

    elif do == 'gagne':
        do = input("\t//Avec quel paramètre voulez vous Listez?//\n")
        if do == 'tout':
            print("\n")
            print(histoire2foot.equipe_gagnante_liste(liste_simple))
            print("\n")

        else:
            print("non, désoler" ,name,", je ne connais pas cette commande dans \"gagne\"")
                
    
    else:
        print("non, désoler" ,name,", je ne connais pas cette commande, tapper \"aide\" si vraiment vous êtes perdu ;)")"""









