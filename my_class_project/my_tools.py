from persian_tools import national_id,phone_number,bank

#کد ملی را بررسی کردم

def check_national_id(code):
     if national_id.is_valid(code):
         print("national id is valid")
         prov_city =national_id.get_place_by_code(code)
         if prov_city:
              print(f" :شهر/استان صادر کنند{prov_city['city']['title']}({prov_city['province']['title']})")
     else:
         print("national id is not valid")


def check_phone_number(number):
    if phone_number.is_valid(number):
        print("phone number is valid")
        operator=phone_number._get_operator(number)
        print(f":اپراتور {operator}")
    else:
        print("phone number is not valid")


def check_car_plate(code):
    plate=input("Enter your plate number:")
    if len(plate)==8:
        print("plate number is valid")
    else:
        print("plate number is not valid")

def check_bill_id(code):
    bill_id=input("Enter your bill_id:")
    if not bill_id.isdigit() or len(bill_id)>= 4:
        print("bill_id is valid")
    else:
        print("bill_id is not valid")
        return
def check_card_number(number):
    card=input("Enter your card number:")
    if bank.check_card_number(number,card):
        print("card number is valid")
        bank_name=bank.get_bank_name(card)
        if bank_name:
            print(f"  :بانک صادرکنند{bank_name}" )
    else:
        print("card number is not valid")


def check_card_number(number):
    return None