#1.feladat
lista1 = []
forrásfájl = open('jarmu.txt')
for sor in forrásfájl:
    lista1.append(sor.strip())
forrásfájl.close()
print("1. feladat: A jarmu.txt beolvasása.")

#2.feladat
lista2 = []
for i in range(len(lista1)):
    seged = lista1[i][0:8]
    lista2.append(seged)

lista3 = []
for i in range(len(lista2)):
    seged2 = lista2[i][0:2]
    seged2 = int(seged2)
    lista3.append(seged2)

lista4 = []
for i in range(len(lista1)):
    seged4 = lista1[i][3:5]
    lista4.append(seged4)

lista5 = []
for i in range(len(lista1)):
    seged5 = lista1[i][6:8]
    lista5.append(seged5)

elso_ora = lista3[0]
for i in range(len(lista3)):
    utolso_ora = lista3[i]
munkaido = utolso_ora - elso_ora
print("2. feladat: Az ellenőrzést végzők legalább",munkaido,"órát dolgoztak.")

#3.feladat
rendszam_lista = []
for i in range(len(lista1)):
    rendszam_seged = lista1[i][9:17]
    rendszam_lista.append(rendszam_seged)


autobusz = "B"
B_darab = 0
kamion = "K"
K_darad = 0
motor = "M"
M_darab = 0
SZ_darab = 0
for i in range(len(rendszam_lista)):
    if rendszam_lista[i][0] == autobusz:
        B_darab += 1
    if rendszam_lista[i][0] == kamion:
        K_darad += 1
    if rendszam_lista[i][0] == motor:
        M_darab +=1
    else:
        SZ_darab += 1
print("3. feladat: Elhaladt járművek mennyisége típusonként:\nautóbusz:",B_darab,"\nkamion:",K_darad,"\nmotor:",M_darab,"\nszemelygépkocsi:",SZ_darab)

#5.feladat
bekert_rendszam = input("5. feladat: Adja meg a keresett rendszámot:")
rendszam_reszlet = ""

for i in range(len(bekert_rendszam)):
    if bekert_rendszam[i] != "*":
        rendszam_reszlet += bekert_rendszam[i]

logikai_valtozo = False
for i in range(len(rendszam_lista)):
    if rendszam_reszlet == "":
        break
    if rendszam_reszlet in rendszam_lista[i]:
        logikai_valtozo = True
        print(rendszam_lista[i])
if logikai_valtozo == False:
    print("Nem haladt el ilyen rendszámmal jármű.")

#6.feladat
ora_seged = 0
rendszam_seged = "a"
ellenorzes_txt_listaja = []
for i in range(len(lista1)):
    if ora_seged != lista1[i][0:3]:
        ora_seged = lista1[i][0:3]
        rendszam_seged = lista1[i][9:17]

        if ora_seged[0] == "0":
            formazas = ora_seged[1] + " óra: " + rendszam_seged
        else:
            formazas = ora_seged + "óra: " + rendszam_seged
        ellenorzes_txt_listaja.append(formazas)

