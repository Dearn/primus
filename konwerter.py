#!/usr/bin/python3
import csv
f1 = open('real.csv', 'r')
c1 = list(csv.DictReader(f1, delimiter=';'))
f2 = open('fakt.csv', 'r')
c2 = list(csv.DictReader(f2, delimiter=';'))

def roznicaStr(a, b):
    return int(b) - int(a)

for i in range(500):
    #        print("Nie znaleziono ",c1[i-1]['ID'])
    for j in range(500):
        if( c1[i]['ID'] == c2[j]['ID']):
            print(c1[i]['ID'],c2[j]['ID'],c1[i]['Nazwa'],c1[i]['Ilosc'], c2[j]['Ilosc'], roznicaStr(c1[i]['Ilosc'],c2[j]['Ilosc']))
            znaleziono = 1
            break
        else:
            znaleziono = 0
    # if znaleziono == 0:
        # dziala ale wyciszyc
        # print("Nie znaleziono ",c1[i]['ID'])
        
            
