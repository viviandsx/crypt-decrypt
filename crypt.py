import hashlib

def crypt(): #Fonction qui permet de crypter le nombre en sha256.
    texte = str(input("Entrez un nombre à crypter : "))
    crypt = hashlib.sha256(str.encode(texte)).hexdigest()
    print(crypt) #Nombre de l'uilisateur crypter.
    choix = int(input("""
Voulez vous décrypter ce nombre ?
1- Oui
2- Non
"""))
    if choix == 1:
        bruteforce(crypt)
    
def bruteforce(password):  # Fonction qui permet de bruteforce un nombre crypter en sha256, en testant chaque nombre 1 par 1.

    trial = 0
    while trial != password:
        trial = str(int(trial) + 1)

        trialencoded = hashlib.sha256(str.encode(trial)).hexdigest()  # Permet de crypter chaque nombre 1 par 1.

        print(">>> " + trial + " <<<")

        if trialencoded == password:  # Permet de comparer le nombre crypter au nombre à décrypter.
            print("Le nombre hashed est " + trial + ".")
            break
                    
main = int(input("""
Ceci est un petit programme qui permet de crypter un nombre en sha256 et de le décrypter !
Merci de faire votre choix :
1- Crypter un nombre
2- Bruteforce
"""))

if main == 1:
    crypt()
elif main == 2:
    password = str(input("Entrez le nombre hashed :"))
    bruteforce(password)
