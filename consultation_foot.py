import histoire2foot



# Ici vos fonctions dédiées aux interactions
intro_nom = False
name = input("Bonjour, quel est votre nom?\n")
while intro_nom == False:
    print('est ce que votre nom est bien', name ,"?")
    is_it_true = input("tapper \"y\" si oui\n")
    if is_it_true == "y":
        print("enchanté" , name , "!\n")
        intro_nom == True
    else:
        name = input("Oh, alors quel est votre nom?\n")

    print("bienvenue dans le terminal python bash, ici tu peut retrouver tout tes matchs\n favoris.")
    wait = input("appuyer sur une touche pour continuer") 



# ici votre programme principal
def programme_principal():

    ...
