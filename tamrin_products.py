order_list=[
    {"name":"moBile","quantity":2,"price":700},
    {"name":"laPtop","quantity":4,"price":6000},
    {"name":"sPeaker","quantity":6,"price":400},
]


#اسم کالاها به حروف کوچک
def text_to_lower(order):
     order["name"]=order["name"].lower()
     return order
result=list(map(text_to_lower,order_list))
print(result)

#اضافه شدن total به هر کالا
def add_total(product):
    product["total"]=product["quantity"]*product["price"]
    return product
result=list(map(add_total,result))
print(result)

#کالاهای بیش از 1000 را نشان بده
def check_price(order):
    return order ["price"]>1000
result_filtered=list(filter(check_price,result))
print(result_filtered)

#جمع کل سفارش ها
def get_total_price(product):
    return product["total"]

total_list=list(map(get_total_price,result))
print(total_list)
print("sum total:",sum(total_list))


#مرتب سازی بر اساس قیمت
def chek_expected_price(product):
    return product["price"]>1000
result_sorted=list(filter(chek_expected_price,result))
print(result_sorted)



