#2003년부터 2025년까지, 서울의 최고 기온이 섭씨 35도 이상이었던 날은 총 며칠이고, 해당일의 기온 평균치, 해당일의 체감 기온 평균치는 몇 도일까요?
#과정1. 수집 기온 데이터 파일 가져오기
#과정2. 서울의 기온 읽어오기
#과정3. 서울의 최고 기온 저장
#과정4. 서울의 최고 기온이 섭씨 35도 이상이었던 날을 셈
#과정5. 서울의 최고 기온이 섭씨 35도보다 높은 날의 일수를 출력, 해당일의 기온 평균치, 해당일의 체감 기온 평균치 구하기

#체감 기온은 풍속과 온도에 영향을 받음 -> 서울_풍속.csv 파일에서 해당일의 풍속을 긁어와 공식에 대입, 해당일의 체감 기온을 구한다.
#간소화 된 체감 기온 공식 : T_체감 = 13.1 + 0.6  *T - 11 * (V^0.2) + 0.4 * T * (V^0.2)

import csv
import numpy

f1 = open('서울.csv', 'r', encoding='cp949')
f2 = open('서울_풍속.csv', 'r', encoding='cp949')

data1 = csv.reader(f1)
data2 = csv.reader(f2)
header1 = next(data1)
header2 = next(data2)

temps_list = []
velos_list = []

for row in data1:
    temps_list.append(row[-1])

for row in data2:
    velos_list.append(row[-1])

appt_temp_list = []
std_temp = 35
stf_date_temp = []
stf_date_count = 0 

for t, v in zip(temps_list, velos_list):
    if t == '':
        t = -999
    
    if v == '':
        v = -999

    t = float(t)
    v = float(v)
    
    if t >= std_temp and v != -999:
        stf_date_count = stf_date_count + 1
        stf_date_temp.append(t)

        T_체감 = 13.1 + (0.6 * t) - 11 * (v**0.2) + 0.4 * t * (v**0.2)
        appt_temp_list.append(T_체감)

        
mean_stf_temp = numpy.mean(stf_date_temp)
mean_appt_temp = numpy.mean(appt_temp_list)

f1.close()
f2.close()

print(stf_date_count, mean_stf_temp, round(mean_appt_temp, 1))

