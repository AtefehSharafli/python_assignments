from lesson.lesson import Lesson

lesson1 = Lesson()
lesson1.code=101
lesson1.name ="برنامه نویسی"
lesson1.teacher="استاد پریور"

lesson1.save()

lesson2 = Lesson()
lesson2.code=101
lesson2.name ="الگوریتم"
lesson2.teacher="استاد رضایی"

print(lesson1)
print(lesson2)