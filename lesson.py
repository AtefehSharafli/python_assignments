lessons=[
    {"name":"java","unit":5,"teacher":"mohammadi"},
    {"name":"python","unit":4,"teacher":"mirzaei"},
    {"name":"c++","unit":3,"teacher":"alipur"},
]


student_1={"name":"java","unit":5,"teacher":"sharafli"}
student_2={"name":"python","unit":4,"teacher":"hasani"}
student_3={"name":"c++","unit":3,"teacher":"alipur"}

student_list=[student_1,student_2,student_3]

#اسم استاد و تعداد واحد با لیست ارائه شده یکی است

def check_lesson(student_lesson):
    return student_lesson in lessons
result=list(filter(check_lesson, student_list))
print(result)
#اسم درس ها به ترتیب حروف الفبا
def sort_by_name(lesson):
    return lesson["name"]
result=sorted(student_list,key=sort_by_name)
print(result)

#اضافه شدن مبلغ
def add_total(lesson):
    lesson["total"]=lesson["unit"]*1000000
    return lesson
student_list=list(map(add_total, student_list))
print(student_list)


#مبلغ کل به حروف نمایش داده شود
def get_total(lesson):
    return lesson["total"]

total_list =list(map(get_total, student_list))
print(total_list)
print("sum total:",sum(total_list))
