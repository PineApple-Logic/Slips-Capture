from pandas import DataFrame
import os
from datetime import date
from os.path import exists

# Variables
path = "./slips"
today = date.today()
x = {"Date": [],
     "Category": [],
     "Price": [],
     "Details": []
     }
date = f'{today.strftime("%d-%b-%Y")}.csv'

# Folder
if not exists('./slips'):
    os.mkdir('./slips')
print('Place the receipt in the Resets Folder. It was created')
print('(Click anything to continue)')
input()

# Capturing slips
filenames = os.listdir(path)
print(filenames)
for filename in filenames:
    names = filename[:-4].split()
    print(names)
    input()
    x['Date'].append(names[0])
    x['Category'].append(names[1])
    price = names[2]
    if price[-1] == ')':
        x['Price'].append(price[:-3])
        x['Details'].append(price[-3:])
    else:
        x['Price'].append(price)

# Load slips to a CSV file
if x['Details'] != '':
    df = DataFrame(x, columns=["Date", "Category", "Price", "Details"])
else:
    df = DataFrame(x, columns=["Date", "Category", "Price"])
print(df)
df.to_csv(date)
