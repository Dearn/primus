#!/usr/bin/python3
import csv, os
f1 = open('fakt.csv', 'r', encoding="utf-8")
c1 = list(csv.DictReader(f1, delimiter=';'))

f2 = open('insider.tex', 'w', encoding="utf-8")
# def funkc(a): # dzialajaca funkcja (kazda etykieta oddzielna tabelka)
#     nazwa = "" #i['Nazwa']
#     cena = i['Detal [brutto] [PLN]']
#     ID = i['Kod']
#     if(len(nazwa)) > 20:
#         nazwa = nazwa[:20]
#     if ID[0] == "7":

#          f2.write(''.join([" {\\renewcommand{\\arraystretch}{2.5}% \n\\begin{tabular}{ |L{3.3cm} |C{2.5cm}| } \n\\hline \n\\footnotesize\\nolinebreak{{",nazwa, "}} & \\textbf{\\LARGE{",ID,"}}\\\\\\cline{2-2} \n\\multicolumn{2}{|c|}{\\textbf{\\Large{", cena," zł} - \\small{cena ostateczna}}}  \\\ \n\\hline\n \\end{tabular}}\n    "]))
#     else:
#         f2.write(''.join([" {\\renewcommand{\\arraystretch}{2.5}% \n\\begin{tabular}{ |L{3.3cm} |C{2.5cm}| } \n\\hline \n\\footnotesize\\nolinebreak{{",nazwa, "}} & \\textbf{\\LARGE{",ID,"}}\\\\\\cline{2-2} \n\\multicolumn{2}{|c|}{\\textbf{\\Large{", cena," zł}}}  \\\ \n\\hline\n \\end{tabular}}\n    "]))

def funk():
    if len(c1)%3 == 0:
        for i  in range(0, len(c1), 3):
            f2.write(''.join(["\\mbox{",c1[i+0]['Nazwa'][:13],"} & \\textbf{\\LARGE{",c1[i+0]['Kod'],"}} &\\mbox{    ",c1[i+1]['Nazwa'][:15],"} &  \\textbf{\\LARGE{",c1[i+1]['Kod'],"}}   &\\mbox{  ",c1[i+2]['Nazwa'][:15],"}  & \\textbf{\LARGE{",c1[i+2]['Kod'],"}} \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",c1[i+0]['Detal [brutto] [PLN]']," zł}}}  &     \\multicolumn{2}{c|}{\\textbf{\\Large{",c1[i+1]['Detal [brutto] [PLN]']," zł}} }    &     \\multicolumn{2}{c|}{\\textbf{\\Large{", c1[i+2]['Detal [brutto] [PLN]'], " zł}}}   \\\\  \\hline \n"]))
    if len(c1)%3 == 1:
        for i  in range(0, len(c1)-1, 3):
            f2.write(''.join(["\\mbox{",c1[i+0]['Nazwa'][:13],"} & \\textbf{\\LARGE{",c1[i+0]['Kod'],"}} &\\mbox{    ",c1[i+1]['Nazwa'][:15],"} &  \\textbf{\\LARGE{",c1[i+1]['Kod'],"}}   &\\mbox{  ",c1[i+2]['Nazwa'][:15],"}  & \\textbf{\LARGE{",c1[i+2]['Kod'],"}} \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",c1[i+0]['Detal [brutto] [PLN]']," zł}}}  &     \\multicolumn{2}{c|}{\\textbf{\\Large{",c1[i+1]['Detal [brutto] [PLN]']," zł}} }    &     \\multicolumn{2}{c|}{\\textbf{\\Large{", c1[i+2]['Detal [brutto] [PLN]'], " zł}}}   \\\\  \\hline \n"]))
        f2.write(''.join(["\\mbox{",c1[i+3]['Nazwa'][:13],"} & \\textbf{\\LARGE{",c1[i+3]['Kod'],"}}   & & & &  \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",c1[i+3]['Detal [brutto] [PLN]']," zł}}} & &  \\hline"]))
            
            
    #         # print (i)
    #     print(tabelka[i+3], tabelka[i+4])

        # ponizej dzialajacy kod - bez i+ 1 / 2 /3
        # f2.write(''.join(["\\mbox{",c1[i+0]['Nazwa'][:13],"} & \\textbf{\\LARGE{",c1[i+0]['Kod'],"}} &\\mbox{    ",c1[i+1]['Nazwa'][:15],"} &  \\textbf{\\LARGE{",c1[i+1]['Kod'],"}}   &\\mbox{  ",c1[i+2]['Nazwa'][:15],"}  & \\textbf{\LARGE{",c1[i+2]['Kod'],"}} \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",c1[i+0]['Detal [brutto] [PLN]']," zł}}}  &     \\multicolumn{2}{c|}{\\textbf{\\Large{",c1[i+1]['Detal [brutto] [PLN]']," zł}} }    &     \\multicolumn{2}{c|}{\\textbf{\\Large{", c1[i+2]['Detal [brutto] [PLN]'], " zł}}}   \\\\  \\hline \n"]))

    #     f2.write(''.join(["\\mbox{",c1[i+0]['Nazwa'][:13],"} & \\textbf{\\LARGE{",c1[i+0]['Kod'],"}} &\\mbox{    ",c1[i+1]['Nazwa'][:15],"} &  \\textbf{\\LARGE{",c1[i+1]['Kod'],"}}   &\\mbox{  ",c1[i+2]['Nazwa'][:15],"}  & \\textbf{\LARGE{",c1[i+2]['Kod'],"}} \\\\ \\cline{2-2}\\cline{4-4}\\cline{6-6}  \\multicolumn{2}{|c|}{\\textbf{\\Large{",c1[i+0]['Detal [brutto] [PLN]']," zł}}}  &     \\multicolumn{2}{c|}{\\textbf{\\Large{",c1[i+1]['Detal [brutto] [PLN]']," zł}} }    &     \\multicolumn{2}{c|}{\\textbf{\\Large{", c1[i+2]['Detal [brutto] [PLN]'], " zł}}}   \\\\  \\hline \n"]))     
    # if len(c2)%3 == 1:
        

funk()
# for i in c1:
#     funkc(c1)
#     f2.close()
