def play():
    print("===============")
    print("MUZICA")
    print("===============")

scor=0
i1 = input("Cine a fost Beethoven? a)compozitor de melodii b)fotbalist c)tiktoker ").lower()
if i1 == "a":
    print("bravo!")
    scor+=1
else:
    print("BRO A FOST ATAT DE SIMPLU, GRESIT")

i2 = input("Cum se numește fenomenul când o melodie ți se blochează în cap și nu mai pleacă, deși n-ai invitat-o? ").lower()
if i2 == "earworm":
    print("wow,ai stiut")
    scor+=1
else:
    print("era greu,recunosc")
