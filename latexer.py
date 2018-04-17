#!/usr/bin/python3
import csv, os
f1 = open('fakt.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))

f2 = open('insider.tex', 'w', encoding="utf-8")
lista = ["00054", "00058", "00107", "00106", "00108", "00112", "00122", "00204", "00208", "00221", "00234", "00257", "00259", "00359", "00752", "00845", "00855", "00911", "01084", "01296", "01310", "01365", "01587", "01588", "01697", "01815", "02013", "02073", "02154", "02236", "02702", "02921", "02973", "03002", "03007", "0272", "03008","02841", "02922", "03105", "03106", "03123", "03115", "03056", "03183", "03405", "03726", "03464", "03735", "03772", "04032", "04037", "04056", "04069", "04089", "04202", "0412", "04207", "04206", "04250", "04274", "04305", "04377", "04392", "04410", "04343", "04508", "04540", "05004", "05016", "05017", "05065", "05071", "05072", "05136", "05150", "05167", "05219", "05240", "05296", "05327", "05328", "05299", "05329", "05330", "05332", "05333", "05318", "05328", "05336", "05340", "05342", "05345", "05309", "05347", "05350", "05351", "05355", "05360", "05376", "05391", "05393", "05400", "05400","00002"]

def funkc(a):
    if(os.path.isfile(''.join(["/home/dearn/zdjecia/",i['ID'],".jpg"]))):
        # print(''.join([i['ID'], " ", i['Nazwa'], i['Cena']]))
        f2.write(''.join(["\n\\pbox{0.5\\textwidth}\n{Index: \\textbf{", i['ID'], "}\\\\\n", i['Nazwa'],"\\\\\nCena: ", i['Cena'],"\\\\\n  \\includegraphics[height=150px,width=250px]{/home/dearn/zdjecia/", i['ID'], ".jpg}}\\newline\n\\newline\n"]))

def funkb(a):
    for j in lista:
        nazwa = i['Nazwa']
        if(len(nazwa)) > 25:
           nazwa = ''.join([nazwa[:25], ' ...'])
        if(j == i['ID'] and os.path.isfile(''.join(["/home/dearn/zdjecia/",i['ID'],".jpg"]))):
                    f2.write(''.join(["\n\\pbox{0.5\\textwidth}\n{Index: \\textbf{", i['ID'], "}\\\\\n", nazwa,"\\\\\nCena: ", i['CenaN']," netto / ", i['Cena'], " brutto\\\\\n  \\includegraphics[height=150px]{/home/dearn/zdjecia/", i['ID'], ".jpg}}\\newline\\newline\n"]))
        
        
for i in c1:
 # if(os.path.isfile('/home/dearn/zdjecia'.join([i['ID'],".jpg"]))):
    # print(''.join([i['ID'], " duzo kosztuje czyli ", i['Cena']]))
    funkb(c1)
              


f2.close()
