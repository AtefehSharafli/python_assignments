from parking_list import *

while True:
    option=show_menu()
    if option==1:
        car=get_car_information()
        parking_list.append_car(car)
        print("car added successfully")

    elif option==2:
        print_parking_list(parking_list)

    elif option==3:
        plate=input("enter plate number to search:")
        result=find_car_by_plate_number(parking_list,plate)
        if result:
            print("found:",result)
        else:
            print("not found")

    elif option==0:
        break


