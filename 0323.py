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


#import csv
#import numpy
#f = open('훈영씨.csv', 'r', encoding='cp949')
#data = csv.reader(f, delimiter=',')
#header = next(data)

#max_avg_temp_range = 0
#max_avg_temp_range_date =''
#temp_ranges = [[], [], [], [], [], [], [], [], [], [], [], []]

#for row in data:
#    if row[-2] != '' and row[-1] != '':
#        temp_range = float(row[-1]) - float(row[-2])
#        temp_ranges[int(row[0].split('-')[1])-1].append(temp_range)

#f.close()

#for index, temp_range in enumerate(temp_ranges):
#    avg_temp_range = numpy.mean(temp_range)
#    if avg_temp_range > max_avg_temp_range:
#        max_avg_temp_range = avg_temp_range
#        max_avg_temp_range_date = index + 1

#max_avg_temp_range = round(max_avg_temp_range, 1)
#
#print(max_avg_temp_range_date, max_avg_temp_range)

#import csv
#import numpy

#f= open('훈영씨.csv', 'r', encoding='cp949')

#data = csv.reader(f)

#header = next(data)
##print(header)

#min_avg_min_temp = 999
#min_avg_min_temp_date = ''
#min_temps = [[], [], []]
#target_date = [12, 1, 2]

#for row in data:
#    if row[-2] != '':
#        month = int(row[0].split('-')[1])
#        if month in target_date:
#            min_temps[target_date.index(month)].append(float(row[-2]))

#f.close()

#for index, min_temp in enumerate(min_temps):
#    avg_min_temp = numpy.mean(min_temp)
#    if avg_min_temp < min_avg_min_temp:
#        min_avg_min_temp = avg_min_temp
#        min_avg_min_temp_date = target_date[index] #같게 설정해놨기 때문에 대입 가능함.

#min_avg_min_temp = round(min_avg_min_temp, 1)

#print(min_avg_min_temp, min_avg_min_temp_date)


import csv

f1= open('훈영씨.csv', 'r', encoding='cp949')
f2= open('헌충씨.csv', 'r', encoding='cp949')

data1 = csv.reader(f1)
data2 = csv.reader(f2)

header1 = next(data1)
header2 = next(data2)

dj_max_temps = []
dj_dates = []

dg_max_temps = []
dg_dates = []

count1 = 0
count2 = 0

for row1 in data1:
    dj_max_temps.append(row1[-1])
    dj_dates.append(row1[0])

for row2 in data2:
    dg_max_temps.append(row2[-1])
    dg_dates.append(row2[0])

f1.close()
f2.close()

if dj_dates == dg_dates:
    for index in range(len(dj_max_temps)):
        dj_max_temp = dj_max_temps[index]
        dg_max_temp = dg_max_temps[index]
        if dj_max_temp != '' and dg_max_temp != '':
            dj_max_temp = float(dj_max_temp)
            dg_max_temp = float(dg_max_temp)
            if dj_max_temp > dg_max_temp:
                count1 = count1 + 1
            #if dg_max_temp > dj_max_temp:
            #    count2 = count2 + 1

print(count1)
