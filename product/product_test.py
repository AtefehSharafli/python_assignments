from product import Samsung, Furniture, Mobile

#تست موبایل سامسونگ
phone1=Samsung()
phone1.code= "A21"
phone1.name= "Samsung"
phone1.screen_size='8" '
phone1.voltage=220
phone1.price=15000000

phone1.save()

#تست مبلمان
furniture1=Furniture()
furniture1.name="Furniture"
furniture1.capacity=7
furniture1.color="red"
furniture1.price=25000000

furniture1.save()

print(phone1)
print(furniture1)
