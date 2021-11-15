from pandas import DataFrame
import os
from os.path import exists
from datetime import date

# Variables
today = date.today()
path = "./slips"
x = {"Date": [],
     "Category": [],
     "Price": [],
     "Details": []
     }
date = f'./{today.strftime("%d-%b-%Y")}.csv'

# Folder
if not exists('./slips'):
    os.mkdir('./slips')
print('Place the receipt in the "slips" Folder. It was created')
print()
input('Press Enter to continue')
print()

# Capturing slips
filenames = os.listdir(path)
for filename in filenames:
    names = filename[:-4].split()
    if len(names) >= 4 or len(names) <= 2:
        print(f'Note that there is an abnormal amount of words/number sets for slip  ({filename})')
        print('It will not be recorded')
        print()
        input('Press Enter to continue')
        print()
    else:
        x['Date'].append(names[0])
        x['Category'].append(names[1])
        price = names[2]
        if price[-1] == ')':
            x['Price'].append(price[:-3])
            x['Details'].append(price[-3:])
        else:
            x['Price'].append(price)
            x['Details'].append('')

# Load slips to a CSV file
if x['Details'] != '':
    df = DataFrame(x, columns=["Date", "Category", "Price", "Details"])
else:
    df = DataFrame(x, columns=["Date", "Category", "Price"])
df.to_csv(date)
