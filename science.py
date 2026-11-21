def play():
    scor = 0
    print("===============\n SCIENCE")

    i1 = input("Care este formula chimica a apei distilate? ").lower()
    if i1 in "h2o":
        print("Corect!")
        scor += 1
    else:
        print("Gresit! Raspunsul corect este H2O")

    i2 = input("Cand focul arde, ce elibereaza si ce consuma? ").lower()
    if "oxigen" in i2 and ("co2" in i2 or "dioxid de carbon" in i2):
        print("Corect!")
        scor += 1
    else:
        print("Gresit! Raspunsul corect este: Consuma oxigen si produce CO2")

    i3 = input("Care din urmatoarele elemente este radioactiv: Fier, Uraniu, Oxigen? ").lower()
    if "uraniu" in i3:
        print("Corect!")
        scor += 1
    else:
        print("Gresit! Raspunsul corect este Uraniu")
    return scor

play()