import histoire2foot
import csv


# ici votre programme principal
programme_tourne=False
Menu_principal=0
nom_fichier="histoire2.csv"





def formatage_liste_de(liste_res):
    try:
        liste_res.sort()
        for elt in liste_res:
            res=print(elt)   
        return res
    except:
        print("Erreur: Veuiller verifier l'intégriter du fichier")

def bonne_equipe():
    if histoire2foot.plus_de_victoires_que_defaites(liste_complexe, recherche) == True:
        res="Il s'agit d'une bonne equipe"
    else:
        res="Il ne s'agit pas d'une très bonne equipe"
    return res



    
liste_simple=histoire2foot.charger_matchs("Sauver_histoire2.csv")
liste_simple=histoire2foot.sauver_matchs(liste_simple,"Histoire2.csv")
liste_simple=histoire2foot.charger_matchs("Histoire2.csv")


do_you_want=input("voulez vous chargez un fichier? sinon histoire2.csv sera executé par defaut (oui si oui)\n vous pourrez changer à tout moment dans les paramètres\n")
if do_you_want=="oui":
    nom_fichier=input("entrer le nom d'un fichier\n") 
    liste_simple=histoire2foot.charger_matchs(nom_fichier)
programme_tourne=True
        
    
    


intro_nom = False
intro_tuto = False
liste_res=""
tout_est_supprimer=0

# Ici vos fonctions dédiées aux interactions
print("\n////////////////////////////////////////////////////")
while programme_tourne == True:
    recherche = input("Bonjour, Bienvenue dans le terminal python match quel information recherchez vous?\n 1-Recherche relative aux equipes (tapper \"equipes\")\n 2-Recherche relative aux matchs (tapper \"matchs\")\n 3-Accéder au paramètres (tapper \"parametres\")\n 4-Quitter (\"tapper quitter\")\n")
    if recherche == "equipes":
        Menu_principal=1

        while Menu_principal==1:
            recherche = input("Pour quel équipe voulez vous des informations?\n -Si vous voulez connaitre le nom des equipes disponible, tapper \"noms\"\n -Si vous voulez revenir en arrière, tapper \"retour\"\n")

            if recherche == "noms":
                liste_res=histoire2foot.liste_des_equipes(liste_simple)
                print(formatage_liste_de(liste_res))
                liste_res=""

            elif recherche== "retour":
                Menu_principal=0

            elif recherche in histoire2foot.liste_des_equipes(liste_simple):
                liste_complexe=histoire2foot.liste_de_match_par_equipe(recherche,liste_simple)

                nombre_matchs =histoire2foot.nombre_de_match_joué(recherche,liste_complexe)
                nombre_but= histoire2foot.nb_buts_marques_liste(liste_complexe)
                moyen_but= histoire2foot.nombre_moyen_buts_sans_argument(liste_complexe)
                premier_gagne=histoire2foot.premiere_victoire(liste_complexe, recherche)
                ecart_score=histoire2foot.ecart_score_tout(liste_complexe)
                sans_défaite=histoire2foot.nb_matchs_sans_defaites(liste_complexe, recherche)
                resultat=histoire2foot.resultats_equipe(liste_complexe,recherche)
                niveau_equipe=bonne_equipe()

                print("L'equipe", recherche, "a joué",nombre_matchs ,"matchs depuis le debut, pour un total de", nombre_but,"but(s) marqués\n -Nombre moyen de but:", moyen_but,"\n -date premier match gagné:",premier_gagne,"\n -ecart relatif de but:", ecart_score,"\n -nombre maximum de matchs sans défaite:",sans_défaite,"\nDans l'ordre, nombres de victoire, nombre de défaite, nombre de matchs nul:\n\n\t",resultat,"\n",niveau_equipe,"\n")
                is_it_true=input("voulez vous afficher la liste des match jouer par cette équipe? tapper oui si oui, tapper autre chose sinon\n")
                if is_it_true == "oui":
                    print(formatage_liste_de(liste_complexe))
            else:
                print("Desoler, je ne connais pas l'équipe,\"", recherche, "\"penser bien à mettre une majuscule à la première lettre du nom de l'equipe\n" )

    elif recherche == "matchs":
        Menu_principal=2

        while Menu_principal==2:
            recherche = input("Pour quel type de match voulez vous des renseignements?\n -Si vous voulez les matchs d'un tournoi précis, tapper \" tournois\"\n -Si vous voulez les matchs dans une localisation précise, tapper \"localisations\"\n -Si vous voulez revenir en arrière, tapper \"retour\"\n")

            if recherche == "tournois":
                Menu_principal=2.1
                while Menu_principal==2.1:
                    recherche = input("Pour quel tournoi voulez vous des informations?\n -Si vous voulez connaitre le nom des tournois disponible, tapper \"noms\"\n -Si vous voulez revenir en arrière, tapper \"retour\"\n")

                    if recherche=="noms":
                        liste_res=histoire2foot.liste_des_tournois(liste_simple)
                        print(formatage_liste_de(liste_res))
                        liste_res=""

                    elif recherche== "retour":
                        Menu_principal=2

                    elif recherche in histoire2foot.liste_des_tournois(liste_simple):
                        liste_complexe=histoire2foot.liste_de_match_par_tournoi(recherche,liste_simple)

                        nombre_matchs =histoire2foot.nombre_de_match_joué_tournoi(recherche,liste_complexe)

                        nombre_but= histoire2foot.nb_buts_marques_liste(liste_complexe)
                        moyen_but= histoire2foot.nombre_moyen_buts_sans_argument(liste_complexe)
                        début_date=histoire2foot.debut_date_liste(liste_complexe)
                        fin_date=histoire2foot.fin_date_liste(liste_complexe)
                        #dfense=histoire2foot.meilleures_equipes(liste_complexe)                  # demmande trop de temps
                        #attque=histoire2foot.meilleures_equipes_attaque(liste_complexe)           # demmande trop de temps
                        spectaculaire=histoire2foot.matchs_spectaculaires(liste_complexe)

                        print("Le tournoi", recherche, "possède",nombre_matchs ,"matchs depuis le debut, pour un total de", nombre_but,"but(s) marqués\n -Nombre moyen de but:", moyen_but,"\n -date du début du tournoi:",début_date,"\n -date du dernier match du tournoi",fin_date ,"\n -Match le plus spectaculaire(match avec le nombre de but le plus élever)\n",spectaculaire,"\n")
                        is_it_true=input("voulez vous afficher la liste des match du tournoi? tapper oui si oui, tapper autre chose sinon\n")
                        if is_it_true == "oui":
                            print(formatage_liste_de(liste_complexe))

                    else:
                        print("Desoler, je ne connais pas de tournoi nommé,\"", recherche, "\"penser bien à mettre les majuscule ou il faut\n" )

            if recherche == "localisations":
                Menu_principal=2.2
                while Menu_principal==2.2:
                    recherche = input("Pour quel localisation voulez vous des informations?\n -Si vous voulez connaitre le nom des localisation disponible, tapper \"noms\"\n -Si vous voulez revenir en arrière, tapper \"retour\"\n")

                    if recherche=="noms":
                        liste_res=histoire2foot.liste_des_localisations(liste_simple)
                        print(formatage_liste_de(liste_res))
                        liste_res=""

                    elif recherche== "retour":
                        Menu_principal=2

                    elif recherche in histoire2foot.liste_des_localisations(liste_simple):
                        liste_complexe=histoire2foot.liste_de_match_par_localisation(recherche,liste_simple)

                        nombre_matchs =histoire2foot.nombre_de_match_joué_localisation(recherche,liste_complexe)

                        nombre_but= histoire2foot.nb_buts_marques_liste(liste_complexe)
                        moyen_but= histoire2foot.nombre_moyen_buts_sans_argument(liste_complexe)
                        début_date=histoire2foot.debut_date_liste(liste_complexe)
                        fin_date=histoire2foot.fin_date_liste(liste_complexe)
                        #dfense=histoire2foot.meilleures_equipes(liste_complexe)           # demmande trop de temps
                        #attque=histoire2foot.meilleures_equipes_attaque(liste_complexe)    # demmande trop de temps
                        spectaculaire=histoire2foot.matchs_spectaculaires(liste_complexe)


                        print("La localiastion", recherche, "est l'endroit où a été joué",nombre_matchs ,"matchs depuis le debut, pour un total de", nombre_but,"but(s) marqués\n -Nombre moyen de but:", moyen_but,"\n -date du premier match à",recherche,":",début_date,"\n -date du dernier match connu",fin_date ,"\n -Match le plus spectaculaire(match avec le nombre de but le plus élever)\n",spectaculaire,"\n")
                        is_it_true=input("voulez vous afficher la liste des match de cette localisation ? tapper oui si oui, tapper autre chose sinon\n")
                        if is_it_true == "oui":
                            print(formatage_liste_de(liste_complexe))

                    else:
                        print("Desoler, je ne connais pas de localisation nommé,\"", recherche, "\"penser bien à mettre les majuscule ou il faut\n" )
            
            elif recherche== "retour":
                Menu_principal=0


    elif recherche=="parametres":
        Menu_principal=3
        while Menu_principal==3:
            recherche=input("Que voulez vous faire dans les paramètres?\n -Charger un nouveau fichier (tapper \"charger\")\n -Verifier le nombre de match présent (tapper \"verifie\")\n -Si vous voulez revenir en arrière, (tapper \"retour\")\n")

            if recherche=="charger":
                do_you_want=input("voulez vous chargez un fichier? sinon histoire2.csv sera executé par defaut (oui/non)\n vous pourrez changer à tout moment dans les paramètres\n")
                if do_you_want=="oui":
                    nom_fichier=input("entrer le nom d'un fichier\n") 
                    liste_simple=histoire2foot.charger_matchs(nom_fichier)
            
            elif recherche=="verifie":
                compte_ligne= histoire2foot.compteur_lignes(nom_fichier)
                print("\nPar defaut (histoire2.csv), le fichier contient:  42484 matchs\nActuellement, le fichier charger contient:  ",compte_ligne,"matchs\n")

            elif recherche=="retour":
                Menu_principal=0

            else:
                print("Desoler, cette commande n'existe pas")





    elif recherche=="quitter":
        programme_tourne=False
                       
    else:
        print("Veuiller réessayer, cela peut être dû à un problème d'orthographe\n")       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
"""if recherche=="ajouts":
                nom_liste_modifier = input("Entrer le nom du fichier que vous voulez ajouter\n -Si vous voulez revenir en arrière tapper \"retour\")\n")                               
                liste_simple=histoire2foot.charger_matchs(nom_liste_modifier)
                liste_simple=histoire2foot.ajouts_matchs("Histoire2.csv",liste_simple)

                print("\n--le fichier à bien été ajouter--\n")
                tout_est_supprimer=0                              

            if recherche=="supprimes":
                supprimer = input("Voulez vous vraiment supprimer tout les fichiers? tapper oui si oui\n")
                if supprimer=='oui':
                    liste_simple=histoire2foot.effecer_matchs("histoire2.csv")
                    print("\n--tout les fichiers ont bien été supprimer--\n")
                    tout_est_supprimer=1
                else:
                    tout_est_supprimer=2

            if recherche=="verifie":
                compte_ligne= histoire2foot.compteur_lignes("histoire2.csv")
                print("Par defaut, le fichier contient:  42484 matchs\nActuellement, le fichier contient:  ",compte_ligne,"matchs")

            
            elif recherche== "retour":
                if tout_est_supprimer==0:
                    Menu_principal=2
                else:
                    print("\n==================================================================================================================")
                    print("  ! ! !  Désoler mais pour pouvoir revenir en arrière,il vous faut au moins un match dans le fichier ! ! !  ")
                    print("==================================================================================================================\n")
            else:
                print("Desoler, je ne connais pas de fonction nommé,\"", recherche, "\"penser bien au s a la fin" )
                if tout_est_supprimer !=0:
                    print("Ne faite pas attention au message au dessus")
                    if tout_est_supprimer==2:
                        tout_est_supprimer=0"""

    
                    
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








