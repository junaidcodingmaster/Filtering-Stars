import os
import csv
import pandas as pd

# Clearing the screen.
if os.name == "nt":
    os.system("cls")
else:
    # for mac and linux(here, os.name is 'posix')
    os.system("clear")

# Getting the terminal size and adding divider for any screen.
sp = "-" * os.get_terminal_size().columns

# Getting data for CSV file.
## Reading Data using the pandas method.
df = pd.read_csv(".\gravity.csv")

## Reading Data using CSV methods.
rows = []
with open(".\gravity.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        rows.append(i)
    filename = f.name

# Printing divider and some data.
print("\nGiven Data", sp)
print(df.head())
print(sp, "\nFiltering Data...\n")

# Generating Data.
headers = rows[0]
star_data = rows[1:]

final_list = []
for star in star_data:
    if float(star[1]) < 100:
        if float(star[4]) > 150 and float(star[4]) < 350:
            final_list.append(star)

# Storing Data.
names = []
distance = []
mass = []
radius = []
gravity = []

for i in final_list:
    names.append(i[0])
    distance.append(i[1])
    mass.append(i[2])
    radius.append(i[3])
    gravity.append(i[4])

# Creating Data Frame to make a CSV file.
df = pd.DataFrame(
    list(zip(names, distance, mass, radius, gravity)),
    columns=["Star_name", "Distance", "Mass", "Radius", "Gravity"],
)

# Printing divider and some result data.
print("Filtered Data", sp)
print(df.head())
print(sp, "\n")

# Creating CSV file.
df.to_csv("filtered_data.csv", index=False)

# Printing the location of filtered data.
print(
    "Your Filtered data is saved ->",
    str(os.path.join(os.getcwd(), "filtered_data.csv")) + "\n",
)
