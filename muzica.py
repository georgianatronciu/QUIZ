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

i3 = input("Care este cea mai tristă parte dintr-o piesă? ").lower()
if i3 == "reclama":
    print("simtim la felll,gandim la felll")
    scor+=1
else:
    print("ti-a murit creativitatea, boss?")

i4 = input("Ce instrument este cel mai probabil să fie folosit într-o ceartă? ").lower()
if i4 == "vioara":
    print("bravo,imi imaginez o cearta si pe fundal o vioara mica")
    scor+=1
else:
    print("bun bun,daaaaaaaaaaar,nu destul de creativ")


print(scor)
