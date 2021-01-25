#PYBANK

#Importing the data 
import os
import csv
from pprint import pprint

#Creating the file path
file_path = os.path.join( 'Resources', 'budget_data.csv')
print(file_path)

#.readlines() and .split(',') found here:
#https://www.summet.com/dmsi/html/CSVdataFiles.html#:~:text=When%20reading%20CSV%20files%2C%20we,use%20readline%20or%20readlines().&text=readlines()%20%2D%20This%20function%20will,it%20returns%20into%20a%20list.

with open(file_path) as csv_file:
    row = csv_file.read().splitlines() 

date = []
pl = []
for line in row:
    data = line.split(',')
    date.append(data[0])
    pl.append(data[1])


# removing first element of both lists
del date[0]
del pl[0]

# using list comprehension to perform conversion from str to int
pl_int = [int(i) for i in pl] 
print(pl_int)

#counting the rows 
num_rows= len(pl_int)

#https://www.kite.com/python/answers/how-to-subtract-two-lists-in-python#:~:text=Use%20zip()%20to%20subtract,the%20result%20in%20a%20list.
# creating the list with off set pairs
list2 = list(zip(pl_int, pl_int[1:]))

#subracting the pairs using list comprehension
dif= [x-y for x, y in list2]   

#calculating the average change 
avg_change = round(sum(dif)/len(dif),2)

# use zip function to combine both lists
list3 = list(zip(date, pl_int))

#Sorting the lists for most and least values
#https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
bottom_value = sorted(list3, key = lambda x: x[1])
top_value = sorted(list3, key = lambda x: x[1],reverse=True)

#Displaying Analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months : {num_rows}")
print(f"Total Profit/Loss : {total_pl}")
print(f"Average  Change: $-{avg_change}")
print(f"Greatest Increase in Profits: {top_value[0]}")
print(f"Greatest decrease in Profits: {bottom_value[0]}")

with open('Resources', 'Output:-PyBnk', "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Months : {num_rows}", file=text_file)
    print(f"Total Profit/Loss : {total_pl}", file=text_file)
    print(f"Average  Change: $-{avg_change}", file=text_file)
    print(f"Greatest Increase in Profits: {top_value[0]}", file=text_file)
    print(f"Greatest decrease in Profits: {bottom_value[0]}", file=text_file)
    text_file.close()
