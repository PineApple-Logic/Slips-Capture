from pandas import DataFrame
import os
from os.path import exists
from datetime import date

# Variables
today = date.today()
path = "./slips/"
x = {"Date": [],
     "Details": [],
     "Category": [],
     "Price": [],
     "Duplicate": []
     }
date = f'./{today.strftime("%d-%b-%Y")}.csv'


def logged(file):
    with open('files.txt', 'w') as f:
        f.write(file)
        f.write('/n')


def match_len(name):
    if len(name) != 12:
        add_to = 12 - len(name)
        name.ljust(len(name) + add_to)


# Checks the file name
def check(filename):
    logged(filename)
    print('-------------------------------------------------------------------------------')
    print(f'Note that there is an abnormal amount of words/number sets for slip:')
    print(f'{filename[:-4]}')
    print()
    print('Please provide a new file name. The old file name will be replaced.')
    newname = input('New file name:')
    os.rename(path + filename, path + newname + filename[-4:])
    print('-------------------------------------------------------------------------------')
    capture(newname + filename[-4:])


# Capturing slips
def capture(filename):
    detail = filename[filename.find('(') + 1: filename.find(')')]
    details = detail
    file = filename.replace(filename[filename.find('('): filename.find(')') + 1], '')
    names = file[:-4].split()
    print(filename[:-4])
    if len(names) > 5 or len(names) < 3:
        check(filename)
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
            names[1] = 'Fuel'
            match_len(names[1])
        else:
            logged(filename)
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


# Check if folder slips exits
if not exists('./slips'):
    os.mkdir('./slips')
print('Place the receipts in the "slips" Folder. It was created')
print()
input('Press Enter to continue')
print()


# Load slips and place them into CSV file
filenames = os.listdir(path)
print('Scanned:')
for files in filenames:
    capture(files)
if x['Details'] != '':
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price", "Duplicate"])
else:
    df = DataFrame(x, columns=["Date", "Details", "Category", "Price"])
df.to_csv(date)
