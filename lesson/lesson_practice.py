from lesson.lesson import Lesson

my_lesson=Lesson()
my_lesson.code=201
my_lesson.name="الگوریتم"
my_lesson.teacher="استاد پریور"

my_lesson.save()

print(my_lesson)