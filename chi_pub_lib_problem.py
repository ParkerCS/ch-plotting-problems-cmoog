
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

file = open("chilib_visitors_2016")
reader = csv.reader(file, delimiter='\t')
plt.figure(figsize=(10,7))
lib_data = []
locations = []
for line in reader:
    lib_data.append(line)

headers = lib_data[0][1:]
lib_data = lib_data[1:]
for t in range(len(lib_data)):
    locations.append(lib_data[t][0])

for j in range(len(lib_data)):
    lib_data[j].remove(lib_data[j][0])

month_totals = []
for month in range(len(lib_data[0])):
    total = 0
    for location in range(len(lib_data)):
        total += int(lib_data[location][month])
    month_totals.append(total)

month_totals.remove(month_totals[12])

'''Which are the three most visited??'''
top_three = []  #will first be two dimensional [location index, location_total]
for l in range(len(lib_data)):  #locaiton
    total = 0
    for g in range(len(lib_data[l]) - 1):  #month
        total += int(lib_data[l][g])
    if len(top_three) != 3:
        top_three.append([l,total])
    elif total > top_three[0][1]:
        top_three.remove(top_three[0])
        top_three.append([l, total])
    elif total > top_three[1][1]:
        top_three.remove(top_three[1])
        top_three.append([l, total])
    elif total > top_three[2][1]:
        top_three.pop(top_three[2])
        top_three.append([l, total])

top_three = [top_three[0][0], top_three[1][0], top_three[2][0]]
top_three_index = top_three
top_three = [lib_data[top_three[0]], lib_data[top_three[1]], lib_data[top_three[2]]]


ax = plt.gca()
plt.xticks(np.arange(len(month_totals)), headers, rotation=20)

total_line = plt.plot(month_totals, label="total")

top_three_line1 = plt.plot(top_three[0][:12], label="line1")
top_three_line2 = plt.plot(top_three[1][:12])
top_three_line3 = plt.plot(top_three[2][:12])

plt.xlabel("Months of 2016")
plt.ylabel("Monthly Visitors")
plt.title("Chicago Public Library Visitors by Month")

plt.legend([total_line, top_three_line1])

plt.ylim([0, 870000])
plt.show()
