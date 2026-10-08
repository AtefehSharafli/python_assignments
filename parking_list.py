parking_list = []

def show_menu():
    print("1) enter to parking")
    print("2) parking list")
    print("3) search car by plate number")
    print("0) exit to parking")
    return int(input("Enter your choice: "))

def get_car_information():
    name = input("Enter your name: ")
    color = input("Enter your color: ")
    plate = input("Enter your plate number: ")
    enter_time = input("Enter your enter time: ")
    return{"name":name, "color":color, "plate":plate, "enter_time":enter_time}

#نمایش ماشین ها

def print_single_car(car):
    print(car['name'], car['color'],car['plate'],car['enter_time'])
    return car


def print_car_list(parking_list):
    print(parking_list)
    list(map(print_single_car, parking_list))
#جستجو ماشین
def find_car_by_plate_number (parking_list, plate_number):
    def check_plate(car):
        return car['plate']==plate_number

    found_cars = list(filter(check_plate, parking_list))
    if found_cars:
        return found_cars[0]
    return None


