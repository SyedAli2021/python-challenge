#Importing the data 
import os
import csv
from pprint import pprint

#Creating the file path
file_path = os.path.join( 'Resources', 'election_data.csv')
print(file_path)

#opening the file and creating sepeart lists
with open(file_path) as csv_file:
    row = csv_file.read().splitlines() 

e_id = []
county = []
name = []
for line in row:
    data = line.split(',')
    e_id.append(data[0])
    county.append(data[1])
    name.append(data[2])

#counting the total number of votes
total_votes = len(name)

#Pulling the names of the candidates
names = list(set(name))
del names[2]
print (names)

#counting the total number of votes per person
counts = [name.count(x) for x in names]
print(counts)

#calculating the total percent of the votes
percent = []
for x in counts:
    y = (x/total_votes)*100
    z = round(y,3)
    percent.append(z)
    
print(percent)

#Printing the output
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
y=0
for x in percent:
    print(f"{names[y]}: {x}% ({counts[y]})")
    y+=1
