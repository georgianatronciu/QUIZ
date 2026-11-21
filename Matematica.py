def play():
    print("Categoria Matematica")
    scor=0
    #intrebarea 1
    i1=input("care este cmmdc al numerelor 2 si 4?").lower()
    if i1=="2":
        print("adevarat")
        scor+=1
    else:
        print("gresit")
    #intrebarea 2
    i2=input("ce este 2+2?").lower()
    if i2=="4":
        print("adevarat")
        scor+=1
    else:
        print("gresit")
    #intrebarea 3
    i3=input("care este 2*2?").lower()
    if i3=="4":
        print("adevarat")
        scor+=1
    else:
        print("gresit")
    # la final returnam scorul
    return scor

play() #apelul functiei