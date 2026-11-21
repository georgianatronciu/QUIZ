def play():
    print("========================")
    print("Jocuri video")
    print("========================")
    scor = 0

    i3=input("Ce joc s-a lansat in 2026(acest joc a fost facut de Rockstar Games)").lower()
    if i3 == "gta 6":
        print("Ai PlayStotion 5")
        scor+=1
    else:
        print("Nu ai PlayStation 5")

    i3=input("Primele calculatoare s-au lansat in 1970-1980.Este adevarata afirmatia sau falsa.").lower()
    if i3 == "falsa":
        print("Corect,deoarece in enunt scria cand au aparut calculatoarele,si calculatoarele au aparut(estimata) in 1940.")
        scor+=1
    else:
     print("Gresit.Deoarece in enunt scria cand au aparut calculatoarele,si calculatoarele au aparut(estimata) in 1940.Si dupa aceea au aparut in 1970-1980 au aparut calculatoarele in casa oamenilor.")
play()