# برنامه ای که از عدد 1تا 100، اعداد زوج بخش پذیر بر 7را به صورت لیست چاپ کند.

numbers=[]

for i in range(1 , 101):
    if i % 2 == 0 and i % 7 == 0 :
        numbers.append(i)

print(numbers)
