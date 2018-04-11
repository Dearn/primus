#!/usr/bin/python3
import csv, os
f1 = open('test.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))

lista = []


for i in c1:
    if(os.path.isfile(''.join([i['ID'],".txt"]))):
        print(''.join([i['ID'], " duzo kosztuje czyli ", i['Cena']]))
