class Ellenorzes:

    def kereses(self,lista1:list):
        rendszam_lista = []
        for i in range(len(lista1)):
            rendszam_seged = lista1[i][9:17]
            rendszam_lista.append(rendszam_seged)

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

    def muszaki_ellenorzes(self,lista1:list):
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






