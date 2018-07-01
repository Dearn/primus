#!/usr/bin/env python
import csv
import locale

f1 = open('real.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))
f2 = open('fakt.csv', 'r', encoding="utf-8")
c2 = list(csv.DictReader(f2, delimiter=';'))

f3 = open('test.csv', 'w',encoding="utf-8")
filewriter = csv.writer(f3, delimiter=';', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

# filewriter.writerow(['Kod', 'Nazwa', 'Cena Na Test', 'Cena na Fakturowym'])
lista = []


# class Baza(object):
#     filename = None
#     cvs = None
#     def __init__(self, nazwapliku):
        



# def roznicaStr(a, b):
#     return ""


for i in range(len(c1) - 1):
    #        print("Nie znaleziono ",c1[i-1]['ID'])
    for j in range(len(c2) - 1):
        if(c1[i]['Kod'] == c2[j]['Kod'] and c1[i]['Kod'] != "00000"):

            # if( float(str(c1[i]['Detal [brutto] [PLN]']).replace(',','.')) != float(str(c2[j]['Detal [brutto] [PLN]']).replace(',','.'))):
            if(c1[i]['Detal [brutto] [PLN]'] != c2[j]['Detal [brutto] [PLN]']):
                print([c1[i]['Kod'], c1[i]['Nazwa'], c1[i]['Detal [brutto] [PLN]'], c2[j]['Detal [brutto] [PLN]']])
                znaleziono = 1

f3.close()
