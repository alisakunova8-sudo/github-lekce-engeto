# Seznam pro ukládání úkolů
ukoly = []


def pridat_ukol():
    nazev = input("Zadejte název úkolu: ").strip()

    while nazev == "":
        print("Název úkolu nesmí být prázdný.")
        nazev = input("Zadejte název úkolu: ").strip()

    popis = input("Zadejte popis úkolu: ").strip()

    while popis == "":
        print("Popis úkolu nesmí být prázdný.")
        popis = input("Zadejte popis úkolu: ").strip()

    ukoly.append({
        "nazev": nazev,
        "popis": popis
    })

    print("Úkol byl přidán.")


# Funkce pro zobrazení seznamu úkolů
def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\n--- Seznam úkolů ---")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['nazev']} - {ukol['popis']}")


# Funkce pro odstranění úkolu ze seznamu
def odstranit_ukol():
    zobrazit_ukoly()

    if not ukoly:
        return

    try:
        ukol = int(input("\nZadejte číslo úkolu k odstranění: "))

        if 1 <= ukol <= len(ukoly):
            odstraneny = ukoly.pop(ukol - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Zadejte prosím číslo.")


# Hlavní menu
def hlavni_menu():
    while True:
        print("\n--- Správce úkolů - Hlavní menu ---")
        print("1. Přidat nový úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")

        volba = input("Vyberte možnost (1-4):").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste znovu.")


# Spuštění programu
if __name__ == "__main__":
    try:
        hlavni_menu()
    except KeyboardInterrupt:
      print("\nProgram byl ukončen uživatelem.")