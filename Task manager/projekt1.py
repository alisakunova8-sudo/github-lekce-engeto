# Seznam pro ukládání ukolů
ukoly = []

def pridat_ukol():
   ukol = input("Zadejte novy ukol: ")
   ukoly.append(ukol)
   print("Ukol byl přidan.")

#Funkce pro zobrazeni seznamu ukolu 
def zobrazit_ukoly():
      if not ukoly:
         print("Seznam ukolu je prazdny.")
      else:
         print ("\n--- Seznam ukolu ---")
         for index, ukol in enumerate (ukoly, start = 1):
            print (f"{index}. {ukol}")

#Funkce pro odstraneni ukolu ze seznamu 
def odstranit_ukol():
   if not ukoly:
      print("Seznam ukolu je prazdny.")
   else:
      try:
         ukol = int(input("\nZadejte ukol k odstraneni: "))
         if 1 <= ukol <= len(ukoly):
            odstraneny = ukoly.pop(ukol - 1)
            print(f"Ukol '{odstraneny}' byl odstraněn.")
            print("Ukol byl odstraněn.")
         else:
            print("Neplatny cislo ukolu.")
      except ValueError:
         print("Zadejte prosim cislo.")


 # Hlavni menu 
def hlavni_menu():
    while True:
       print("\n--- Hlavni menu ---")
       print("1. Pridat ukol")
       print("2. Zobrazit ukoly")
       print("3. Odstranit ukol")
       print("4. Konec")

       volba = input("Vyberte moznost: ")

       if volba == "1":
          pridat_ukol()
       elif volba == "2":
          zobrazit_ukoly()
       elif volba == "3":
          odstranit_ukol()
       elif volba == "4":
          print("Konec programu." ) 
          break 
       else:
          print("Neplatna volba zkusite znovu.")           
   

# spusteni programu
hlavni_menu()
 