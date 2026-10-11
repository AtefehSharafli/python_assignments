# برنامه ای که تا وقتی کاربر عدد صفر وارد نکرده غدد بگیرد و اعداد زوج و فرد را در دو لیست جداگانه چاپ کند.

even_numbers=[]
odd_numbers=[]

while True:
  number=int(input(': لطفا یک عدد وارد کنید'))

  if number==0:
     break

  if number % 2 == 0:
     even_numbers.append (number)

  else:
     odd_numbers.append(number)

print("even_numbers :" , even_numbers)
print("odd_numbers :" ,odd_numbers )