#import csv
#f = open('훈영씨.csv', 'r', encoding='cp949')
#data = csv.reader(f, delimiter=',')
#header = next(data)
#print(header)
#for row in data:
#    print(row)
#f.close()


#import csv
#f = open('훈영씨.csv', 'r', encoding='cp949')
#data = csv.reader(f, delimiter=',')
#header = next(data)
#print(header)
#max_temp = -999
#max_date = ''
#for row in data:
#    if row[-1]=='':
#        row[-1]=-999
#    row[-1]=float(row[-1])
#    if max_temp < row[-1]:
#        max_temp = row[-1]
#        max_date = row[0]
#f.close()
#print(max_temp, max_date)


import csv
import numpy
f = open('훈영씨.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)

max_avg_temp_range = 0
max_avg_temp_range_date =''
temp_ranges = [[], [], [], [], [], [], [], [], [], [], [], []]

for row in data:
    if row[-2] != '' and row[-1] != '':
        temp_range = float(row[-1]) - float(row[-2])
        temp_ranges[int(row[0].split('-')[1])-1].append(temp_range)

f.close()

for index, temp_range in enumerate(temp_ranges):
    avg_temp_range = numpy.mean(temp_range)
    if avg_temp_range > max_avg_temp_range:
        max_avg_temp_range = avg_temp_range
        max_avg_temp_range_date = index + 1

max_avg_temp_range = round(max_avg_temp_range, 1)

print(max_avg_temp_range_date, max_avg_temp_range)