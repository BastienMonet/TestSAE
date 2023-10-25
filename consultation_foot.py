import histoire2foot
import csv

with open("histoire1.csv", "r", encoding="utf8", errors='ignore') as file:
    csv_reader = csv.reader(file)

    liste_simple=histoire2foot.charger_matchs("histoire1.csv")

    intro_nom = False
    intro_tuto = False

    # Ici vos fonctions dédiées aux interactions
    intro_nom = False
    name = input("Bonjour, quel est votre nom?\n")
    while intro_nom == False:
        print('est ce que votre nom est bien', name ,"?")
        is_it_true = input("\t//tapper \"y\" si oui//\n")
        if is_it_true == "y":
            print("enchanté" , name , "!")
            intro_nom = True
        else:
            name = input("Oh, alors quel est votre nom?\n")

    while intro_nom == True and intro_tuto == False:
        is_it_true = False
        print("bienvenue dans le terminal python match ,ici tu peut retrouver tout tes matchs\nfavoris.")
        wait = input("\t//appuyer sur une touche pour continuer//")
        print("veux tu une petite introduction au fonctionalité présente?")
        is_it_true = input("\t//tapper \"y\" si oui//")
        if is_it_true == 'y':
            print("...")
        print("d'accord, alors amuse toi bien", name ,"!")
        print("\n")
        print("\n")
        intro_tuto = True

    while intro_tuto == True:
        do = input("\t//.Alors, que voulez vous faire mtn?//\n" )
        
        if do == 'lire':
            do = input("\t//Avec quels paramètre voulez vous lire?//\n")
            if do == 'tout':
                print("êtes vous sûr d'afficher TOUT les matchs")
                is_it_true = input("\t//tapper \"y\" si oui//\n")
                if is_it_true == "y":
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
                    print("\n")
                    print(histoire2foot.nb_buts_marques_liste(liste_simple))
                    print("\n")
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
            print("non, désoler" ,name,", je ne connais pas cette commande, tapper \"aide\" si vraiment vous êtes perdu ;)")






# ici votre programme principal
def programme_principal():

    ...
