import jarmu
import ido
import ellenorzes

lista1 = []
forrásfájl = open('jarmu.txt')
for sor in forrásfájl:
    lista1.append(sor.strip())
forrásfájl.close()
print("1. feladat: A jarmu.txt beolvasása.")


x = ido.Ido()
x.ora(lista1)
x.perc(lista1)
x.masodperc(lista1)

y = jarmu.Jarmu()
y.ido(lista1)
y.rendszam(lista1)
y.tipus(lista1)

z = ellenorzes.Ellenorzes()
z.kereses(lista1)
z.muszaki_ellenorzes(lista1)

