'''import csv

verb = 'servir'
finder = list()
finder.append(verb)

print(finder)

with open('Lista_Irregulares.csv',newline='') as f:
    reader = csv.reader(f)
    irregulars = list(reader)

print(irregulars)

print(len(irregulars))


if finder in irregulars:
    print("É irregular!")
else:
    print("Não é irregular!")
'''
import pandas as pd

verb = 'ter'

irregulars_pd = pd.read_excel('Lista_Irregulares.xlsx')
irregular_list = list(irregulars_pd.Verbos)
irregular_list

print(irregular_list)

if verb in irregular_list:
    print("É irregular!")
else:
    print("Não é irregular!")
