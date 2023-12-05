nom_du_fichier = "test.txt"

total = 0
chiffre = ""

with open (nom_du_fichier, "r") as fichier:
    for ligne in fichier:
        if ligne.find("onetwothreefourfivesixseveneightnine"):
            ligne = ligne.replace("one", "1")
            ligne = ligne.replace("two", "2")
            ligne = ligne.replace("three", "3")
            ligne = ligne.replace("four", "4")
            ligne = ligne.replace("five", "5")
            ligne = ligne.replace("six", "6")
            ligne = ligne.replace("seven", "7")
            ligne = ligne.replace("eight", "8")
            ligne = ligne.replace("nine", "9")
            print(ligne)
        chiffres = [caractere for caractere in ligne if caractere.isdigit()]
        if chiffres:
            premier_chiffre = chiffres[0]
            dernier_chiffre = chiffres[-1]
            chiffre = premier_chiffre + dernier_chiffre
            total = total + int(chiffre)
        print(total)
