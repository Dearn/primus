#!/usr/bin/python3
import csv
f1 = open('real.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))
f2 = open('fakt.csv', 'r', encoding="utf-8")
c2 = list(csv.DictReader(f2, delimiter=';'))

f3 = open('wynik.csv', 'w', encoding="utf-8")
filewriter = csv.writer(f3, delimiter=';', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

filewriter.writerow(['ID', 'Nazwa', 'Ilosc Real', 'Ilosc Fakt', 'Roznica Fakt Norm'])
lista = []


class Baza(object):
    filename = None
    csv = None
    def __init__(self, nazwapliku):
        self.filename = open(nazwapliku, 'r', encoding='utf-8')
        self.csv = list(csv.DictReader(self.filename, delimiter=';'))
    
t1 = Baza('real.csv')      

# print (t1.csv[2]['Kod'])

# def roznicaStr(a, b):
#     return ""


for i in range(len(c1) - 1):
    #        print("Nie znaleziono ",c1[i-1]['Kod'])
    for j in range(len(c2) - 1):
        if(c1[i]['Kod'] == c2[j]['Kod'] and c1[i]['Kod'] != "00000"):
            # print(c1[i]['Kod'], c2[j]['Kod'], c1[i]['Nazwa'][:8], "\t", c1[i]
            #       ['Ilość'], c2[j]['Ilość'], roznicaStr(c1[i]['Ilość'], c2[j]['Ilość']))
            filewriter.writerow([c1[i]['Kod'], c1[i]['Nazwa'], c1[i]['Ilość'], c2[j]['Ilość']]) #( float(c2[j]['Ilość'].replace(",",".")) - float(c1[i]['Ilość'].replace(",",".")))])

            znaleziono = 1
            break
        else:
            znaleziono = 0
            # print(c1[i]['Kod'],c2[j]['Kod'],c1[i]['Nazwa'][:25],"\t",c1[i]['Ilość'], c2[j]['Ilość'], roznicaStr(c1[i]['Ilość'],c2[j]['Ilość']))
    if(znaleziono == 0 and c1[i]['Kod'] != "00000"):
        # dziala ale wyciszyc
        # print("Nie znaleziono ", c1[i]['Kod'])
        lista.append([c1[i]['Kod'], c1[i]['Nazwa'],
                      c1[i]['Ilość']])
# for row in lista:
#     filewriter.writerow(row)
f3.close()
