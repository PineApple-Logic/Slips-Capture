from pandas import DataFrame
import pandas as pd
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
        x['Details'].append(names[1])
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

