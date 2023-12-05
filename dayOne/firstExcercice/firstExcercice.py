nom_fichier = "input.txt"

total = 0
chiffre = ""

with open(nom_fichier, "r") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        chiffres = [caractere for caractere in ligne if caractere.isdigit()]
        if chiffres:
            premier_chiffre = chiffres[0]
            dernier_chiffre = chiffres[-1]
            chiffre = premier_chiffre + dernier_chiffre
            total = total + int(chiffre)
    print(total)


        