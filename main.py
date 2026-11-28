from categoria_limbaje_de_programare import play as play_programare
from Matematica import play as play_mate
from Jocurivideoprimaintrebare import play as play_jocurivideo
from science import play as play_science
from muzica import play as play_muzica

scor_total = 0

while True:
    alegere = int(input("Alege categoria: "))

    if alegere == 0:
        break
    elif alegere == 1:
        scor_total += play_programare()
    elif alegere == 2:
        scor_total += play_mate()
    elif alegere == 3:
        scor_total += play_jocurivideo()
    elif alegere == 4:
        scor_total += play_science()
    elif alegere == 5:
        scor_total += play_muzica()
    else:
        print("Opțiune invalidă. Încearcă din nou.")
    

nume = input("Care e numele tau? ")

print(f"Salut {nume}!")

print("Succes! Ai fost inregistrat cu succes!")
print("===================================")
print("                QUIZ               ")
print("===================================")
print("numele echipei:")
print("            CeiMaiTariDinLume")
print("===================================")
print("       Georgiana Tronciu         ")
print("       Sara                      ")
print("       Matei Gabriel Cringasu    ")
print("       Mihai                      ")
print("       Matei Condrea               ")
print("       Alex                       ")
print("===================================")
