from product import Laptop, Iphone


#تست لب تاپ

laptop1=Laptop()
laptop1.code=101
laptop1.name="Asus"
laptop1.price=45000000
laptop1.ram="16GB"
laptop1.cpu="Core i7"

laptop1.save()

#تست آیفون
phone2=Iphone()
phone2.code=102
phone2.name="iphone 13"
phone2.price=550000000
phone2.screen_size='601"'

phone2.save()

print(laptop1)
print(phone2)