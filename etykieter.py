#!/usr/bin/python3
import csv, os
f1 = open('fakt.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))

f2 = open('insider.tex', 'w', encoding="utf-8")
def funkc(a):
    nazwa = "" #i['Nazwa']
    cena = i['Detal [brutto] [PLN]']
    ID = i['Kod']
    if(len(nazwa)) > 20:
        nazwa = nazwa[:20]
    if ID[0] == "7":

         f2.write(''.join([" {\\renewcommand{\\arraystretch}{2.5}% \n\\begin{tabular}{ |L{3.3cm} |C{2.5cm}| } \n\\hline \n\\footnotesize\\nolinebreak{{",nazwa, "}} & \\textbf{\\LARGE{",ID,"}}\\\\\\cline{2-2} \n\\multicolumn{2}{|c|}{\\textbf{\\Large{", cena," zł} - \\small{cena ostateczna}}}  \\\ \n\\hline\n \\end{tabular}}\n    "]))
    else:
        f2.write(''.join([" {\\renewcommand{\\arraystretch}{2.5}% \n\\begin{tabular}{ |L{3.3cm} |C{2.5cm}| } \n\\hline \n\\footnotesize\\nolinebreak{{",nazwa, "}} & \\textbf{\\LARGE{",ID,"}}\\\\\\cline{2-2} \n\\multicolumn{2}{|c|}{\\textbf{\\Large{", cena," zł}}}  \\\ \n\\hline\n \\end{tabular}}\n    "]))

def funk():
    
    for i in c1:
        nazwa = i['Nazwa']
        cena = i['Detal [brutto] [PLN]']
        ID = i['Kod']
        f2.write(''.join([nazwa," & \\textbf{\\LARGE{",ID,"}} &     ",nazwa," & \\textbf{\\LARGE{",ID,"}}   &   ",nazwa,"  & \\textbf{\LARGE{",ID,"}} \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",cena," zł}}}  &     \\multicolumn{2}{c|}{\\textbf{\\Large{",cena," zł}} }    &     \\multicolumn{2}{c|}{\\textbf{\\Large{", cena, " zł}}}   \\\\  \\hline \n"]))
        

funk()
# for i in c1:
#     funkc(c1)
#     f2.close()
