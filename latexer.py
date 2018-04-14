#!/usr/bin/python3
import csv, os
f1 = open('fakt.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))

f2 = open('insider.tex', 'w', encoding="utf-8")
lista = []
def funkc(a):
    if(os.path.isfile(''.join(["/home/dearn/zdjecia/",i['ID'],".jpg"]))):
        # print(''.join([i['ID'], " ", i['Nazwa'], i['Cena']]))
        f2.write(''.join(["\centering{\n\\pbox{0.5\\textwidth}\n{Index: \\textbf{", i['ID'], "}\\\\\n", i['Nazwa'],"\\\\\nCena: ", i['Cena'],"\\\\\n  \\includegraphics[height=150px,width=250px]{/home/dearn/zdjecia/", i['ID'], ".jpg}}}\n"]))


for i in c1:
 # if(os.path.isfile('/home/dearn/zdjecia'.join([i['ID'],".jpg"]))):
    # print(''.join([i['ID'], " duzo kosztuje czyli ", i['Cena']]))
    funkc(i)

f2.close()
