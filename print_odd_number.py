# برنامه ای که تا وقتی کاربر عدد 0 وارد نکرده عدد بگیرد و میانگین اعداد فرد دریافتی را چاپ کند.

sum_odd =0
count_odd =0

while True:
    number=int(input("  : یک عدد وارد کنید"))

    if number == 0:
        break

    if number % 2 !=0:
        sum_odd += number
        count_odd +=1

if count_odd > 0:
    average = sum_odd / count_odd
    print(" :  میانگین اعداد فرد")

else:
    print("عدد فرد وارد نشده")
