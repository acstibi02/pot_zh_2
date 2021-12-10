class Jarmu:


    def ido(self,lista1:list):
        lista2 = []
        for i in range(len(lista1)):
            seged = lista1[i][0:8]
            lista2.append(seged)

    def rendszam(self,lista1:list):
        rendszam_lista = []
        for i in range(len(lista1)):
            rendszam_seged = lista1[i][9:17]
            rendszam_lista.append(rendszam_seged)

    def tipus(self,lista1:list):
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
        print("3. feladat: Elhaladt járművek mennyisége típusonként:\nautóbusz:", B_darab, "\nkamion:", K_darad,
              "\nmotor:", M_darab, "\nszemelygépkocsi:", SZ_darab)




