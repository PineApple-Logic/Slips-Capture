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


def match_len(name):
    if len(name) != 12:
        add_to = 12 - len(name)
        name.ljust(len(name) + add_to)


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
    details = filename[filename.find('(') + 1: filename.find(')')]
    file = filename.replace(filename[filename.find('('): filename.find(')') + 1], '')
    names = file[:-4].split()
    print(details)
    print(file)
    if len(names) >= 5 or len(names) <= 2:
        print()
        print(f'Note that there is an abnormal amount of words/number sets for slip  ({names})')
        print('It will not be recorded')
        print()
        input('Press Enter to continue')
        print()
    else:
        x['Date'].append(names[0])
        if len(details) != 20:
            add_to = 20 - len(details)
            details.ljust(len(details) + add_to)
        x['Details'].append(details)
        if names[1] == 'O':
            names[1] = 'Other'
            match_len(names[1])
        elif names[1] == 'A':
            names[1] = 'Accommodation'
            match_len(names[1])
        elif names[1] == 'C':
            names[1] = 'Consumables'
            match_len(names[1])
        elif names[1] == 'E':
            names[1] = 'Equipment'
            match_len(names[1])
        elif names[1] == 'T':
            names[1] = 'Toll'
            match_len(names[1])
        elif names[1] == 'F':
            names[1] = 'Food'
            match_len(names[1])
        elif names[1] == 'S':
            names[1] = 'Stationery'
            match_len(names[1])
        elif names[1] == 'D':
            names[1] = 'Diesel'
            match_len(names[1])
        elif names[1] == 'P':
            names[1] = 'Petrol'
            match_len(names[1])
        else:
            print(f"Failed to determine the Category's Full name of {names[1]}")
            print()
            full_name = input('Full name:')
            names[1] = full_name
            match_len(names[1])
        x['Category'].append(names[1])
        x['Price'].append(names[2])
        if len(names) == 4:
            x['Duplicate'].append(names[3])
        else:
            x['Duplicate'].append('')


# Load slips to a CSV file
if x['Details'] != '':
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price", "Duplicate"])
else:
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price"])
df.to_csv(date)
