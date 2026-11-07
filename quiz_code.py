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
    i1 = input("ai voie sa atnigi mingea cu mana la fotbal? ").lower()
    if i1 == "nu":
        print("corect")
        scor += 1   
    else:
        print("gresit")
    i2 = int(input("in ce an sa retras Ronaldo de la echipa nationala a portugaliei "))
    if i2 == 2026:
        print("corect")
        scor += 1
    else:
        print("gresit")
print(scor)


 