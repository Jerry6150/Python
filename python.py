
#name = input("올해 년도를 입력해주세요.")
#x = int(name)-1
#print("작년은 ", x ,"년입니다.")

#A = int(input("숫자 1을 입력해주세요."))
#B = int(input("숫자 2를 입력해주세요."))
#print(A!=B)
#print(B//A)
#print(A**B>=B)
#print(not A!=B)

import math
#x = float(input("숫자를 입력해주세요."))
#print(math.sqrt(x))

#파이썬 멘토링 2주차

#name = input("이름을 입력해주세요.")
#for i in name:
#    print(i)

#season = ["봄", "여름", "가을", "겨울"]
#for i in season:
#    print(i)

#x = float(input("점수를 입력하세요."))
#if 90<=x<=100:
#    print('"A"')
#elif 80<=x<90:
#    print('"B"')
#elif 70<=x<80:
#    print('"C"')
#elif 60<=x<70:
#    print('"D"')
#elif 0<=x<60:
#    print('"E"')
#else:
#    print('"ERROR"')

#x = float(input("점수를 입력하세요."))
#if x>100 or x<0:
#    print('"ERROR"')
#elif x>=90:
#    print('"A"')
#elif x>=80:
#    print('"B"')
#elif x>=70:
#    print('"C"')
#elif x>=60:
#    print('"D"')
#else:
#    print('"E"')

#season=['봄', '여름', '가을']
#print(season[0])
#print(season[1])
#print(season[:])
#print(season[0:3:2])
#season.append('겨울')
#print(season[0:])
#seasons = season[1:]
#seasons.append('훈영씨')
#print(seasons)


#natural = ['1', '2', '3', '4', '5', '6', '7','8', '9', '10']
#print(natural[0:9:2])


import random
import math
x = int(input("원하는 정수1을 입력하세요."))
y = int(input("원하는 정수2를 입력하세요."))
A = int(((x+y)/2)-(abs((x-y)/2)))
B = int(((x+y)/2)+(abs((x-y)/2)))
randomness = []
for k in range(10):
    i = random.randint(A, B)
    randomness.append(i)

for p, q in enumerate(randomness):
    if q>=3:
        print(q, p)

