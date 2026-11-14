print("==============================")
print("      QUIZ-UL FULGERELOR        ")
print("==============================")
nume=input("Cum te cheama? ")
print(f"Salut, {nume}! Alege o categorie: ")
print("1. Sport")
print("2. Animale")
print("3. Jocuri video")
print("4. Stiinta")
print("0. Iesire")
raspuns=int(input("Ce numar alegi? "))
scor = 0
if raspuns == 1:
    i1 = input("ai voie sa atingi mingea cu mana la fotbal? ").lower()
    if i1 == "nu":
        print("corect")
        scor += 1   
    else:
        print("gresit")
    i2 = int(input("in ce an sa retras Ronaldo de la echipa nationala a portugaliei? "))
    if i2 == 2026:
        print("corect")
        scor += 1
    else:
        print("gresit")
print(scor)

if raspuns == 2:
    i1=input("care este cel mai inalt animal din lume?").lower()
    if i1=="girafa":
        print("adevarat")
        scor+=1
    else:
        print("gresit")

    i2=input("care este cel mai greu mamifer din lume?").lower()
    if i2=="balena albastra":
        print("adevarat")
        scor+=1
    else:
        print("gresit")

if raspuns == 4:
    i1 = input("Ce organ pompează sângele în corp?\n A) Plămânii \n B) Inima\n C) Ficatul\n").lower()
    if i1 == "b":
        print("adevarat")
        scor+=1
    else:
        print("Gresit")


    i1 = input("Care este simbolul chimic al oxigenului?\n A) O \n B) Ox\n C) Og\n").lower()
    if i1 == "a":
        print("adevarat")
        scor+=1
    else:
        print("Gresit")

    i1 = input("În ce unitate se măsoară temperatura?\n A) Kilogram \n B) Metru\n C) Grad Celsius\n").lower()
    if i1 == "c":
        print("adevarat")
        scor+=1
    else:
        print("Gresit")
    print(scor)