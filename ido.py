class Ido:


    def ora(self,lista1:list):
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
        print(lista5)

        elso_ora = lista3[0]
        for i in range(len(lista3)):
            utolso_ora = lista3[i]
        munkaido = utolso_ora - elso_ora
        print("2. feladat: Az ellenőrzést végzők legalább", munkaido, "órát dolgoztak.")



    def perc(self,lista1:list):
        lista4 = []
        for i in range(len(lista1)):
            seged4 = lista1[i][3:5]
            lista4.append(seged4)

    def masodperc(self,lista1:list):
        lista5 = []
        for i in range(len(lista1)):
            seged5 = lista1[i][6:8]
            lista5.append(seged5)


