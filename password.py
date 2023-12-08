import string
import hashlib
import json
import random


liste_cara_speciaux = ["!", "?", "#", "$", "%", "^", "&", "*", "-", "_", ".", "&"]
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
liste = list(alphabet_lower)
liste2 = list(alphabet_upper) 


##################################################################################################################
  
def listeeternel() :
    #JSON ne peux avoir qu'un objet dans son fichier. Donc si je relance le programme il ecrasera le precedent. 
    # Pour l'eviter a a chaque lancement du programme je lis le fichier et je le copie/colle dans la liste afin de le conserver.
    with open("data.json", "r") as json_file :
        try :
            listejson = json.load(json_file)
        except :
            listejson = []
    return listejson

# Verifie si le mdp est conforme.       
def generated(k) :
    # Les variables count me permet plus tard de verifier si le cahier des charge est respecté.
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    # Pour chaque element de ma chaine de caractere, si il reponde a un critere un des compteurs est incrementé.
    for i in k :
        if i in liste :
            count += 1
        elif i in liste2 :
            count2 += 1
        elif i in liste_cara_speciaux :
            count3 += 1
        elif i.isdigit() :
            count4 += 1
        elif i == " " :
            print("Error : ne mettez aucun espace dans votre mot de passe.")
            break
    # Uniquement si tout est respecte, le mdp est valide.
    if count >= 1 and count2 >= 1 and count3 >= 1 and count4 >= 1 :
        if len(k) >= 8 :
            count5 += 1
            print("Votre mot de passe est valide.")
        else :
            print("Votre mot de passe doit etre superieur ou egal à 8.")
    else :
        print("Error : Votre mot de passe doit contenir au moins 8 caracteres dont au moins 1 minuscule, 1 majuscule, une à caractere special, une avec un chiffre. Veuillez rééssayer.")
    return k, count5

#Je demande un mdp tant qu'il n'existe pas.             
def ask_passwd() :
    while True :
        ask = input("Veuillez entrer un mot de passe : ")
        for item in listejson :
            if (hashlib.sha256(ask.encode()).hexdigest()) in item.values() :
                print("Mot de passe deja enregistré")
                return ask, True
        ask, counting = generated(ask)
        if counting == 1 :
            break
        else :
            continue
    return ask, False

# Je genere une cle a partir du mdp.
def crypte(k) :
    print("Votre mot de passe a été géneré.")   
    h = hashlib.sha256(k.encode()).hexdigest()
    dico = {f"Mot de passe {k[0]}***{k[-1]}": h}
    listejson.append(dico)
    with open("data.json", "w") as json_file :
        json.dump(listejson, json_file, indent=4)
    return k


#################################################################################################

listejson = listeeternel()

while True :
    yn = input("Souhaitez vous un mot de passe généré aléatoirement ?(y/n) ").lower()
    if yn == "y" :
        generated_password = liste_cara_speciaux + liste + liste2 + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        gp = "".join(random.sample(generated_password,16))
        check = input(f"Le mot de passe {gp} vous convient il ?(y/n) ").lower()
        if check == "y" :
            crypte(gp)
            print("Si vous souhaitez consulter votre liste de mot de passe, relancez le programme.")
            print("Merci à bientot.")
            exit()
        elif check == "n" :
            continue 
        else :
            print("Error : Votre reponse doit etre uniquement 'y' ou 'n'.")
    elif yn == "n" :
        break
    else : 
        print("Error : Votre reponse doit etre uniquement 'y' ou 'n'.")
            

while True :
    new, verif = ask_passwd()
    if verif == False :
        crypte(new)
    yn = input("Souhaitez vous entrer un nouveau mot de passe ?(y/n) ").lower()
    if yn == "y" :
        continue
    elif yn == "n" :
        break 
    else :
        print("Error : Votre reponse doit etre uniquement 'y' ou 'n'.")
        
while True :
    on = input("Souhaitez vous voir l'integraliter de vos tokens ?(y/n) ").lower()
    if on == "y" :
        with open("data.json", "r") as json_file :
            data = json.load(json_file)
            print(data)
    elif on == "n" :
        break
    else :
        print("Error : Votre reponse doit etre uniquement 'y' ou 'n'.")
    
    