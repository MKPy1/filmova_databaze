"""
Filmová databáze
"""

def uvod():
    print("=" * 40)
    pom = "Vítejte ve 'filmové' databázi:".upper()
    print(pom.center(40))
    print("=" * 40)
uvod()

def oddelovac():
    print("=" * 40)


def nabidka():
    film1 = {
        "Nazev": "Vykoupení z věznice Shawshank",
        "Hodnoceni": 93,
        "Herci": ["Tim Robbins", "Morgan Freeman"],
        "Podivat se": True,
        "Rok": 1994,
        "Zanr": "Drama"
    }

    film2 = {
        "Nazev": "Statečné srdce",
        "Hodnoceni": 95,
        "Herci": ["Mel Gison", "Sophie Marceau"],
        "Podivat se": True,
        "Rok": 1995,
        "Zanr": "Historicky"
    }

    databaze = dict()
    databaze["Vykoupení z věznice Shawshank"] = film1
    databaze["Statečné srdce"] = film2


    print("V nabídce máme tyto filmy: ", list(databaze))
    oddelovac()


    zadej_nazev = input("Zadej název filmu: ")
    if not databaze.get(zadej_nazev):
        print("Nenachází se v DB")
        oddelovac()
        text = input("Chcete film s názvem " "'" + zadej_nazev.title() + "'" + " uložit (ANO/NE): ")
        if text == "ANO":
            film3 = {}
            film3["Název"] = zadej_nazev.title()
            film3["Hodnoceni"]: None
            film3["Herci"]: None
            film3["Podivat se"]: None
            film3["Rok"]: None
            film3["Zanr"]: None

            databaze[film3['Název']] = film3
            print("Film byl přidán do databáze: ", list(databaze))

            rozhodni = input("Chcete přidat další film/y A/N: ")

            while True:
                if rozhodni=="N":
                    break
                elif rozhodni=="A":
                    novy_slovnik = {}
                    kolikrat = int(input("Kolik filmů chcete přidat: "))
                    oddelovac()
                    for i in range(0,kolikrat):
                        nazev=input("Název filmu: ").title()

                        jmeno_klic=nazev
                        novy_slovnik[jmeno_klic] = {"Název":nazev}

                    databaze.update(novy_slovnik)
                    oddelovac()
                    print("V databázi jste momentálně tyto filmy: ",list(databaze))
                    break
                else:
                    print("Chybná volba")
                    exit()
        elif text == "NE":
            print("Film ukládat nebudeme")
        else:
            print("Nesprávné volba")
    else:
        print("Ano, film je v DB")
        print("""
                        MOŽNOSTI:
                        I)  Zobrazit detaily filmu (Z)
                        II) Smazat film            (S)
                          """)
        moznosti = input("Zadej danou klávesu pro spuštění akce, (X) pro ukončení: ")
        if moznosti == "X":
            print("Program se ukončí...")
            exit()
        elif moznosti == "S":
            if zadej_nazev == "Statečné srdce":
                databaze.pop("Statečné srdce")
                oddelovac()
                print("Film byl odebrán z DB...")
                oddelovac()
                print("Aktuální filmy v DB", list(databaze))
            elif zadej_nazev == "Vykoupení z věznice Shawshank":
                databaze.pop("Vykoupení z věznice Shawshank")
                oddelovac()
                print("Film byl odebrán z DB...")
                oddelovac()
                print("Aktuální filmy v DB", list(databaze))
            else:
                print("Film byl už smazán")
                exit()
        elif moznosti == "Z":
            if zadej_nazev == "Statečné srdce":
                print("Detaily k filmu Statečné srdce: ", databaze["Statečné srdce"])
            elif zadej_nazev == "Vykoupení z věznice Shawshank":
                print("Detaily k filmu Vykoupení z věznice Shawshank: ", databaze["Vykoupení z věznice Shawshank"])
            else:
                print("Film nenalezen")
                exit()

        oddelovac()

        pom = list(databaze)
        for i in range(len(pom)):
            print(str(i+1) + " " + pom[i])

        oddelovac()

nabidka()



