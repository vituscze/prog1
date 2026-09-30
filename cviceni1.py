### Cvičení z Algoritmizace ###

# Tykání/vykání? Klidně mi tykejte.

# Jak získat zápočet
#
# * Docházka je doporučená, ale není povinná
#   - 1 extra bod za každé cvičení, na které přijdete
# * Domácí úlohy
#   - Nová úloha každý týden, první zadám na dalším cvičení
#   - Celkem bude 8 úloh, každá za 10 bodů
#   - 4 textové úlohy, 4 programovací úlohy (+-)
#   - 70% bodů (tj. 56 bodů) pro získání zápočtu
#   - Úlohy se odevzdávají přes ReCodEx (viz níže), udělejte si tam účet
#   - Pokud se na něčem zasknete, tak vám můžu dát nápovědu

# Studijní materiály
#
# * GitHub repozitář
# * Discord server (nepovinný)

## Hledání maxima ##

# Předpokládejme, že máme N krabic s různou hmotností a chceme najít tu nejtěžší.
# K dispozici máme váhy, které lze použít k porovnání hmotností dvou krabic.

# a) Jak najít nejtěžší krabici s minimálním použití váhy?
# b) Proč je předchozí výsledek optimální? Ukažte, že to nemůžeme udělat lépe.
# c) Jak najít nejtěžší a nejlehčí krabici pomocí ceil(3N/2) - 2 porovnání?
# d) [bonus] Jak najít dvě nejtěžší krabice pomocí N - 2 + ceil(log_2(N)) porovnání?

# a) Vybereme první krabici jako kandidáta na nejtěžší. Poté položíme kandidáta a druhou krabici na váhu.
# Pokud je druhá krabice těžší, nahradíme ji jako kandidáta. Toto uděláme pro všechny zbývající krabice.
# Nakonec je kandidátem nejtěžší krabice a provedli jsme N - 1 porovnání.

# b) Abychom pochopili, proč je to optimální, zvažte, co se stane s počtem krabic, které "prohrály" v
# alespoň jednom kole. Pokaždé, když použijeme váhu, se toto číslo zvýší maximálně o jednu. Pokud použijeme
# N - 2 (nebo méně) porovnání, budeme mít alespoň 2 krabice, které neprohrály kolo, a nedokážeme říct,
# která z těchto dvou je maximální.

# c) Pro jednoduchost předpokládejme, že N je sudé (pro liché N je to podobné). Nejprve zvážíme
# krabice ve dvojicích (první s druhou, třetí se čtvrtou atd.), což vyžaduje N/2 porovnání.
# Všimněte si, že nejtěžší krabice musí být mezi vítězi a nejlehčí mezi poraženými. Můžeme
# pak jednoduše použít přístup z a) na N/2 vítězů a N/2 poražených, což nám dává
# N/2 + N/2 - 1 + N/2 - 1 = 3N/2 - 2 porovnání.

## Druhá mocnina modulo 4 ##

# Je toto tvrzení pravdivé, nebo ne?
# Pro všechna celá čísla n platí n^2 mod 4 < 2.
# Dokažte svou odpověď.

# Připomínka: a mod b je zbytek po (celočíselném) dělení a div b.
# a = b * (a div b) + (a mod b); 0 <= a mod b < b.

# Začněme kontrolou, zda toto tvrzení platí pro několik malých čísel.
#   0^2 mod 4 = 0
#   1^2 mod 4 = 1
#   2^2 mod 4 = 0
#   3^2 mod 4 = 1
#   4^2 mod 4 = 0
#   5^2 mod 4 = 1
#   ...

# Zdá se, že pro sudá čísla dostaneme 0 a pro lichá čísla 1. Ale to není důkaz!
# Musíme ukázat, že výsledek je 0 (1) pro *libovolné* sudé (liché) číslo.

# Sudá čísla jsou dělitelná 2. Můžeme tedy libovolné sudé číslo n zapsat jako n = 2k (kde k je jiné celé číslo).
# Podívejme se, co se stane, když použijeme tuto identitu při výpočtu zbytku:
#
#   (2k)^2 mod 4 = 4k^2 mod 4 = 0
#
# 4k^2 je VŽDY násobkem 4, takže neexistuje zbytek.

# Podobně lze lichá čísla vyjádřit jako 2k + 1:
#
#   (2k+1)^2 mod 4 = 4k^2 + 4k + 1 mod 4 = 4(k^2 + k) + 1 mod 4 = 1
#
# Okamžitě vidíme, že číslo je vždy o 1 vyšší než násobek 4.

## Kuličky ##

# V urně máme *b* bílých a *c* černých kuliček. Postupně opakujeme následující tahy:
# Sáhneme do urny a vytáhneme dvě kuličky. Potom, pokud
# a) jsou obě bílé, jednu bílou vrátíme zpět
# b) je jedna bílá a druhá černá, vrátíme zpět černou
# c) jsou obě černé, do urny místo nich dáme jednu bílou

# Předpokládejme, že máme k dispozici neomezenou zásobu bílých kuliček.

# Lze s počáteční konfigurace *b* a *c* určit, jakou poslední kuličku z urny vytáhneme?

# Všimněte si, že se v každém kroku zmenší počet kuliček v urně o jednu. Nutně se tedy
# dostaneme do situace, kdy bude urna obsahovat jedinou kuličku (za předpokladu, že urna
# nebyla prázdná).

# Pokud b + c = 1, pak buď c = 0 (a poslední kulička je tedy bílá) nebo c = 1 (a poslední
# kulička je černá).

# Pokud b + c > 1: Podívejme se, jak se bude vyvíjet konfigurace *b* a *c*.
# a) (b, c) -> (b - 1, c)
# b) (b, c) -> (b - 1, c)
# c) (b, c) -> (b + 1, c - 2)

# *b* může (teoreticky) nabýt libovolné hodnoty. *c* se ale vždy pohybuje po dvou. Pokud
# bylo *c* na začátku sudé, tak bude sudé po celý zbytek procesu. Na konci tedy musí nastat
# případ c = 0. Stejně tak pro liché *c* a c = 1.

# Toto je případ tzv. invarianty. Vlastnosti, která v průběhu našeho procesu (obecněji algoritmu)
# bude vždy platit.

### Cvičení z Programování I ###

# Jak získat zápočet
#
# * Docházka je doporučená, ale není povinná
#   - 1 extra bod za každé cvičení, na které přijdete
# * Domácí úlohy
#   - Nová úloha každý týden, první zadám na dalším cvičení
#   - Celkem bude k dispozici 100 bodů (9-10 úloh, ještě řeknu)
#   - 70% bodů (tj. 70 bodů) pro získání zápočtu
#   - Úlohy se odevzdávají přes ReCodEx
#     * Přečtěte si README v repozitáři, jsou tam linky na návody
#   - Pokud se na něčem zasknete, tak vám můžu dát nápovědu
# * Test
#   - Na konci semestru (poslední cvičení) bude zápočtový test
#   - Další termíny budou k dispozici během zkouškového období
#   - Na test máte celkem 3 pokusy
#   - Zapisování přes SIS (včetně prvního termínu na cvičení)
#   - Pokud se na první termín (tj. poslední cvičení) nezapíšete na SISu
#     a nepřijdete, tak vám termín *nepropadne*
# * Zápočtový program
#   - Vyberete si a vyřešíte nějaký zajímavý problém
#   - Implementace algoritmu, jednoduchá hra, command line tool, atp.
#   - Než na programu začnete pracovat, tak sepište a pošlete specifikaci
#     * Popis problému a jak tento problém hodláte řešit
#     * Nemusí to být nic dlouhého/formálního; mělo by to ale být dost specifické
#       na to, aby se podle toho váš program dal hodnotit
#     * V ReCodExu na specifikace vytvořím speciální úlohu, odevzdejte jako
#       .txt, .md, .pdf (prosím ne .doc nebo .docx)
#     * Jakmile vám specifikaci odsouhlasím, tak na tom můžete začít pracovat
#   - Pro samotný projekt použijte git repozitář (bude na přednášce) a na
#     univerzitní mail mi pošlete link; v repozitáři by mělo být:
#     * Zdroják
#     * Uživatelská dokumentace (co jste to vlastně naprogramovali, jak se to ovládá, jak vypadá vstup, atp.)
#     * Programátorské dokumentace (jak váš program funguje, stačí formou dokumentačních komentářů)
#     * Testovací data (pokud má váš program nějaké netriviální vstupy, tak mi dejte nějaké příklady na vyzkoušení)
#   - Součástí je také prezentace vašeho programu (může být i online)
#   - Deadline do konce semestru

# Studijní materiály
#
# * GitHub repozitář
# * Discord server (nepovinný)

# Použití AI
#
# Dnešní LLMka vám často budou rovnou cpát kód. To je fajn, pokud
# už jste ostřílený programátor, ale pokud nejste, tak se z toho většina studentů
# prakticky nic nenaučí.
#
# Pokud narazíte na problém, tak se klidně LLMka zeptejte -- ale specificky modelu
# dejte vědět, že nechcete zdroják/chcete problému porozumět. Na zápočtovým testu to
# na konci semestru jde celkem poznat.

## Python ##

# Nejnovější verzi Pythonu si můžete stáhnout zde: https://www.python.org/downloads/
# Na cvičení budu používat VS Code, ale klidně použijte jakékoli IDE, se kterým umíte pracovat.

# Python je interpretovaný jazyk. Python vezme váš kód a rovnou ho vyhodnotí.

# Existují také kompilované jazyky (například C), které nejprve převedou (zkompilují) kód do
# instrukcí, kterým rozumí procesor. Po kompilaci nepotřebujete k puštění kódu žádný další program
# Existují také hybridní jazyky (které používají hybridní přístup, např. JIT).

# Interpret Pythonu je interaktivní (tzv. REPL). Můžete psát příkazy a
# interpret je interaktivně vyhodnocuje. Tímto způsobem si můžeme průběžně zkoušet části programu.

# Python má několik základních datových typů. Existují dva číselné typy: int (celá čísla) a
# float (čísla s plovoucí desetinnou čárkou).

# >>> type(5)
# >>> type(1.0)

# Celá čísla mají neomezenou přesnost. Čísla s plovoucí desetinnou čárkou mají velkou, ale konečnou přesnost.
# Můžeme vyjádřit čísla v rozsahu cca 1e-324 až 1e308 (kladná i záporná) a několik speciálních hodnot (nula, nekonečno).
# Poznámka k zápisu: 1e308 znamená 1 * 10^308.

# Při používání čísel s plovoucí desetinnou čárkou buďte opatrní, jejich konečná přesnost může vést k neočekávaným výsledkům:

# >>> 0.3 == 3 * 0.1

# Máme také některé aritmetické operace: +, -, *, /, **, //, %
# (sčítání, odčítání, násobení, dělení s plovoucí desetinnou čárkou, umocňování, celočíselné dělení, modulo)
# Všimněte si, že ^ NENÍ umocňování. Je to bitová operace, o které si povíme později.

# Dalším datovým typem je boolean. Booleany jsou logické hodnoty. Máme konstanty True a False a operace:
# <, <=, >, >=, ==, !=, and, or, not
# (menší než, menší nebo rovno, větší než, větší nebo rovno, rovno, nerovná se, konjunkce, disjunkce, negace)

# >>> not True

# Řetězce jsou posloupnosti znaků. Jsou uzavřeny v uvozovkách (") nebo apostrofech (').
# Pokud potřebujeme do řetězce napsat apostrof nebo uvozovku, můžeme použít zpětné lomítko:

# >>> "that's nice"
# >>> "that's \"nice\""

# Zpětným lomítkem můžeme vyjádřit i další speciální znaky, například znak nového řádku (\n) nebo tabulátor (\t).
# Pokud potřebujeme do řetězce vložit zpětné lomítko, jednoduše ho zdvojnásobíme:

# >>> 'The newline character is \\n'

# Řetězce lze sčítat, násobit (číslem) a porovnávat.

# Často budeme muset mezi těmito datovými typy převádět. Pokud například požádáme uživatele, aby zapsal číslo,
# Python přečte odpověď jako řetězec a my ho nejprve musíme převést na číslo, než s ním budeme moci použít aritmetické
# operace. K tomu máme následující 4 operace: int(...), float(...), str(...), bool(...)

# >>> int('5') == 5
# >>> str(True) == 'True'

# Program vygeneruje výjimku (bude později), pokud konverzi nelze provést.

# >>> int('hello')

# Prozatím budeme psát konzolové aplikace. Jak název napovídá, tyto aplikace jsou určeny k
# používání z konzole (terminálu). Konzolové aplikace mají STANDARDNÍ VSTUP (stdin) a STANDARDNÍ VÝSTUP (stdout).
# Pokud stdin a stdout nikdo nezmění (například přesměrováním), to, co uživatel zapíše do konzole, je
# vstup a to, co program zapíše do konzole, je výstup. Standardní vstup můžeme číst
# pomocí vestavěné funkce input(...) a zapisovat do standardního výstupu pomocí vestavěné funkce print(...)

name = input("What's your name?\n")
print('Nice to meet you', name)

# Pokud použijeme input(...) s řetězcem, nejprve se řetězec zapíše do stdout a poté se přečte řádek ze stdin.
# Mějte to na paměti při odesílání programů do ReCodEx, který porovnává celý stdout (tj. včetně řádků zapsaných fcí input).

# Python má také větve (if, elif, else) a smyčky (while, for).

for i in range(10):
    print(i)

for c in name:
    print(c)

## ReCodEx ##

# Domácí úkoly jsou automaticky hodnoceny ReCodExem. Vytvořte si účet a připojte se ke skupinám pro obě cvičení
# podle příručky pro nové uživatele: http://www.ms.mff.cuni.cz/ReCodEx/NewUserDocEng.pdf
# Studentská příručka pak vysvětlí, jak ReCodEx používat: http://www.ms.mff.cuni.cz/ReCodEx/StudentDocEng.pdf

# Když odevzdáte program, ReCodEx automaticky spustí váš kód na sadě testovacích případů a ohodnotí vás na základě počtu
# úspěšně dokončených případů. Testovací případ může selhat z mnoha důvodů: špatný výsledek, program příliš dlouho běžel,
# program spotřeboval příliš mnoho paměti, program spadnul, atp.

# Pokud si nejste jisti, proč něco nefunguje, tak mi klidně pošlete na Discordu DM nebo mi napište mail.

# Někdy mohou mít úkoly další požadavky, které ReCodEx neumí zkontrolovat.
# V těchto případech zkontroluju vaše řešení já a ručně upravím skóre, pokud jsou požadavky špatně.

# ReCodEx funguje zhruba takto: každý testovací případ má dva soubory: test.in a test.out.
# test.in je soubor obsahující vstupní data testovacího případu, test.out je správný výstup. ReCodEx poté spustí:

# $ python student_code.py < test.in > student.out

# A nakonec porovná soubory test.out a student.out. Pokud jsou stejné, test projde.
# Ve skutečnosti je to trochu složitější (existují časová omezení a omezení paměti, aby se zajistilo,
# že vaše programy nemohou způsobit problémy na serveru).

# Jednoduchá hra na hádání čísla.

import random

rnd = random.randint(1, 100)

while True:
    guess = int(input('Enter a guess: '))
    if guess < rnd:
        print('Too low, try again.')
    elif guess > rnd:
        print('Too high, try again.')
    else:
        print('You got it!')
        break

## Project Euler 2 ##

# https://projecteuler.net/
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
for n in range(1000): # 1000 není součástí rozsahu
    if n % 3 == 0 or n % 5 == 0:
        total = total + n
print(total)
