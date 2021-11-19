from pandas import DataFrame
import os
from os.path import exists
from datetime import date

# Variables
today = date.today()
path = "./slips"
x = {"Date": [],
     "Details": [],
     "Category": [],
     "Price": [],
     "Duplicate": []
     }
date = f'./{today.strftime("%d-%b-%Y")}.csv'


def match_len(num):
    if len(names[num]) != 12:
        add_to = 12 - len(names[num])
        if len(names[num]) != 12:
            names[num].ljust(len(names[num]) + add_to)


# Folder
if not exists('./slips'):
    os.mkdir('./slips')
print('Place the receipts in the "slips" Folder. It was created')
print()
input('Press Enter to continue')
print()

# Capturing slips
filenames = os.listdir(path)
for filename in filenames:
    names = filename[:-4].split()
    if len(names) >= 6 or len(names) <= 2:
        print()
        print(f'Note that there is an abnormal amount of words/number sets for slip  ({filename})')
        print('It will not be recorded')
        print()
        input('Press Enter to continue')
        print()
    else:
        x['Date'].append(names[0])
        match_len(1)
        x['Details'].append(names[1])
        if names[2] == 'O':
            match_len(2)
            x['Category'].append('Other')
        elif names[2] == 'A':
            names[2] = 'Accommodation'
            match_len(2)
        elif names[2] == 'C':
            names[2] = 'Consumables'
            match_len(2)
        elif names[2] == 'E':
            names[2] = 'Equipment'
            match_len(2)
        elif names[2] == 'T':
            names[2] = 'Toll'
            match_len(2)
        elif names[2] == 'F':
            names[2] = 'Food'
            match_len(2)
        elif names[2] == 'S':
            names[2] = 'Stationery'
            match_len(2)
        else:
            print(f"Failed to determine the Category's Full name of {names[2]}")
            print()
            full_name = input('Full name:')
            names[2] = full_name
            match_len(2)
        x['Category'].append(names[2])
        x['Price'].append(names[3])
        if len(names) == 5:
            x['Duplicate'].append(names[4])
        else:
            x['Duplicate'].append('')


# Load slips to a CSV file
if x['Details'] != '':
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price", "Duplicate"])
else:
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price"])
df.to_csv(date)
