"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

file = open("meantemp.txt", "r")
lines = file.readlines()
file.close()
hval = -40.0
hdate = ""
lval = 40.0
ldate = ""
for i in range(2,len(lines)):
    rn = lines[i]
    if rn.strip() != "":
        parts = rn.split()
        date = parts[0]
        value = float(parts[1])
        if value > hval:
            hval = value
            hdate = date

for i in range(2,len(lines)):
    rn = lines[i]
    if rn.strip() != "":
        parts = rn.split()
        date = parts[0]
        value = float(parts[1])
        if value < lval:
            lval = value
            ldate = date
total = 0
count = 0
for i in range(2,len(lines)):
    rn = lines[i]
    if rn.strip() != "":
        parts = rn.split()
        value = float(parts[1])
        total = total + value
        count = count + 1

average = total / count
print("highest temp: ", hval, " on", hdate)
print("lowest temp: ", lval, "on", ldate)
print("average temp: ", int(average))


