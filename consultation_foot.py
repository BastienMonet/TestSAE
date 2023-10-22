import histoire2foot

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
    do = input("\t//Alors, que voullez vous faire mtn?//\n")
    if do == 'lire':
        do = input("\t//Que voullez vous lire?//\n")
        if do == 'tout':
            print(histoire2foot.charger_matchs(histoire1.csv))
            print("\n")
            print("\n")
    else:
        print("non, désoler" ,name,", je ne connais pas cette commande")






# ici votre programme principal
def programme_principal():

    ...
