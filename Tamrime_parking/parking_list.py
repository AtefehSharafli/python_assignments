parking_list = []

def show_menu():
    print("1) enter to parking")
    print("2) parking list")
    print("3) search car by plate number")
    print("0) exit to parking")
    return int(input("Enter your choice: "))

def get_car_information():
    name= input("Enter your name: ")
    color= input("Enter your color: ")
    plate= input("Enter your plate number: ")
    enter_time= input("Enter your enter time: ")

    return {"name":name,"color":color,"plate":plate,"enter_time":enter_time}

def print_parking_list(parking_list):
    print("parking list")
    for car in parking_list:
        print(car['name'],['color'],["plate"],['enter_time'])

def find_car_by_plate_number(parking_list,plate_number):
    for car in parking_list:
        if car['plate'] == plate_number:
            return car
    return None