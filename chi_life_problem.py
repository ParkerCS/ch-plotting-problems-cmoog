#1 Import csv, numpy, and matplotlib.plot
import csv
import numpy as np
import matplotlib.pyplot as plt

#2 Open the chi_life_expectancy.txt file

file = open("chi_life_expectancy.txt", 'r')

#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
chi_data = []

reader = csv.reader(file, delimiter='\t')

for line in reader:
    chi_data.append(line)


#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
life_expectancy_2010_list = []
for i in range(1,len(chi_data)):
    life_expectancy_2010_list.append(float(chi_data[i][8]))
community_list = []
for k in range(1,len(chi_data)):
    community_list.append(chi_data[k][1])

plt.bar(np.arange(len(life_expectancy_2010_list)), life_expectancy_2010_list, .8)
plt.xticks(np.arange(len(life_expectancy_2010_list)), community_list, rotation=90)


#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities

#ax = plt.gca()
#ax.set_xticklabels(community_list, rotation=60)


#6  Set an appropriate plt.ylim([min,max])
plt.ylim([65, 86])
plt.xlim([0,len(community_list)/2])

#7  Label your axes
plt.xlabel("Community Names")
plt.ylabel("2010 Life Expectancy")

#8  Add a title
plt.title("2010 Life Expectancy by Community")


#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.
plt.show()
# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.



