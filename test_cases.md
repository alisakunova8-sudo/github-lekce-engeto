# Testovací případy

## 1. hlavni_menu()

### Testovací případ 1: Spuštění funkce pridat_ukol() přes hlavní menu.

**Popis:**  
Ověření, že volba čísla 1 v hlavním menu správně spustí funkci `pridat_ukol()`.

**Vstupní podmínky:**  
Program zobrazuje hlavní menu.

**Kroky testu:**
1. Spusťte program.
2. Ověřte, že se zobrazuje hlavní menu.
3. Zadejte číslo `1`.

**Očekávaný výsledek:**  
Program spustí funkci `pridat_ukol()`

**Skutečný výsledek:**  
Program spustil funkci `pridat_ukol()`a zobrazil výzvu k zadání názvu úkolu.

**Stav:**  
Pass

**Poznámky:**  
 Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.

### Testovací případ 2: Ukončení programu

**Popis:**
Ověření, že poslední platná možnost hlavního menu správně ukončí program.

**Vstupní podmínky:**
Program je spuštěný a zobrazuje hlavní menu.

**Kroky testu:**

1. Spusťte program.
2. Zadejte číslo `4`.
3. Stiskněte Enter.

**Očekávaný výsledek:**
Program zobrazí hlášku `Konec programu.` a ukončí se.

**Skutečný výsledek:**
Program zobrazil hlášku `Konec programu.` a ukončil se.

**Stav:**
Pass

**Poznámky:**
Hraniční test ověřuje poslední platnou možnost hlavního menu.



## 2. pridat_ukol()

### Testovací případ 1: Spuštění funkce pridat_ukol().

**Popis**
Ověření, že funkce pridat_ukol() správně přidá nový úkol s názvem a popisem.

**Vstupní podmínky:** 
Program je spuštěný a funkce pridat_ukol() je připravená k použití.

**Kroky testu**
1. Spusťte funkci pridat_ukol().
2. Zadejte název úkolu Dokončit projekt od Engeta.
3. Stiskněte Enter.
4. Zadejte popis úkolu Dneska nebo zitra.
5. Stisknete Enter.

**Očekávaný výsledek:**
Úkol se správně přidá do seznamu úkolů a program zobrazí hlášku Úkol byl přidán.

**Skutečný výsledek**:
Program spustil funkci a úkol byl přidán.

**Stav**:
Pass

**Poznámky**:
Test ověřuje správné přidání úkolu s názvem a popisem.

### Testovací případ 2: Prázdný název úkolu.

**Popis:**
Ověření, že program nepovolí přidat úkol bez názvu.

**Vstupní podmínky:**
Program je spuštěný a funkce `pridat_ukol()` je připravená k použití.

**Kroky testu:**
1. Spusťte funkci `pridat_ukol()`.
2. Nechte název úkolu prázdný.
3. Stiskněte Enter.

**Očekávaný výsledek:**
Program zobrazí hlášku `Název úkolu nesmí být prázdný.` a znovu požádá o zadání názvu úkolu.

**Skutečný výsledek:**
Program zobrazil hlášku `Název úkolu nesmí být prázdný.` a znovu požádal o zadání názvu úkolu.

**Stav:**
Pass

**Poznámky:**
Test ověřuje, že program nepovolí prázdný název úkolu.

### Testovací případ 3: Přidání úkolu s minimálním platným vstupem

**Popis:**
Ověření, že funkce přijme nejkratší platný název a popis úkolu.

**Vstupní podmínky:**
Program je spuštěný a funkce `pridat_ukol()` je připravená k použití.

**Kroky testu:**

1. Spusťte funkci `pridat_ukol()`.
2. Jako název zadejte `A`.
3. Jako popis zadejte `B`.
4. Stiskněte Enter.

**Očekávaný výsledek:**
Program přijme název i popis a úkol přidá.

**Skutečný výsledek:**
Program přijal název `A` a popis `B` a úkol přidal.

**Stav:**
Pass

**Poznámky:**
Hraniční test ověřuje nejkratší platný vstup pro název a popis úkolu.


## 3. zobrazit_ukoly()

### Testovací případ 1: Zobrazení uloženého úkolu

**Popis:**
Ověření, že funkce `zobrazit_ukoly()` správně zobrazí uložený úkol včetně názvu a popisu.

**Vstupní podmínky:**
V seznamu je uložen alespoň jeden úkol.

**Kroky testu:**

1. Přidejte nový úkol s názvem `cvičit`.
2. Zadejte popis `behat 10 minut`.
3. Zvolte možnost `2. Zobrazit úkoly`.
4. Stiskněte Enter.

**Očekávaný výsledek:**
Program zobrazí úkol ve formátu `1. cvičit - behat 10 minut`.

**Skutečný výsledek:**
Program zobrazil úkol ve formátu `1. cvičit - behat 10 minut`.

**Stav:**
Pass

**Poznámky:**
Test ověřuje správné zobrazení uloženého úkolu včetně názvu a popisu.

### Testovací případ 2: Zobrazení prázdného seznamu

**Popis:**
Ověření, že funkce `zobrazit_ukoly()` správně zobrazí hlášku, pokud nejsou uložené žádné úkoly.

**Vstupní podmínky:**
Seznam úkolů je prázdný.

**Kroky testu:**

1. Odstraňte všechny uložené úkoly.
2. Zvolte možnost `2. Zobrazit úkoly`.
3. Sledujte výpis programu.

**Očekávaný výsledek:**
Program zobrazí hlášku `Seznam úkolů je prázdný.`

**Skutečný výsledek:**
Program zobrazil hlášku `Seznam úkolů je prázdný.`

**Stav:**
Pass

**Poznámky:**
Hraniční test ověřuje chování funkce při prázdném seznamu úkolů.


## 4. odstranit_ukol()

### Testovací případ 1: Odstranění uloženého úkolu

**Popis:**
Ověření, že funkce `odstranit_ukol()` správně odstraní vybraný úkol ze seznamu.

**Vstupní podmínky:**
V seznamu je uložen alespoň jeden úkol.

**Kroky testu:**

1. Zvolte možnost `3. Odstranit úkol`.
2. Ověřte, že se zobrazí seznam úkolů.
3. Zadejte číslo úkolu, který chcete odstranit.
4. Stiskněte Enter.

**Očekávaný výsledek:**
Vybraný úkol bude odstraněn a program zobrazí potvrzení o odstranění.

**Skutečný výsledek:**
Úkol `cvičit` byl odstraněn.

**Stav:**
Pass

**Poznámky:**
Test ověřuje správné odstranění vybraného úkolu ze seznamu.


### Testovací případ 2: Odstranění posledního úkolu

**Popis:**
Ověření, že program správně zvládne odstranění posledního úkolu ze seznamu.

**Vstupní podmínky:**
V seznamu je uložen pouze jeden úkol.

**Kroky testu:**

1. Zvolte možnost `3. Odstranit úkol`.
2. Zadejte číslo `1`.
3. Úkol se odstraní.
4. Zvolte znovu možnost `3. Odstranit úkol`.

**Očekávaný výsledek:**
Program zobrazí hlášku `Seznam úkolů je prázdný.`

**Skutečný výsledek:**
Po odstranění posledního úkolu program zobrazil hlášku `Seznam úkolů je prázdný.`

**Stav:**
Pass

**Poznámky:**
Hraniční test ověřuje chování programu po odstranění posledního úkolu ze seznamu.







