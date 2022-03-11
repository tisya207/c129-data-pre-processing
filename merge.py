import csv

dataset1=[]
dataset2=[]

with open("dataset1.csv","r") as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("dataset2.csv","r") as f:
    csv_reader= csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

header1= dataset1[0]
planet_data1= dataset1[1:]

header2= dataset1[0]
planet_data2= dataset1[1:]

headers= header1 + header2
all_planet_data=[]
for index, data_row in enumerate(planet_data1):
    all_planet_data.append(planet_data1[index]+ planet_data2[index])

with open("merged.csv","a+") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(all_planet_data)