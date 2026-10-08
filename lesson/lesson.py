class Lesson:

    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None

        print("درس جدید ایجاد شد")

    def save(self):
        print(f"save:{self.name} {self.code} {self.teacher}")

    def edit(self):
        print(f"edit:{self.name} {self.code} {self.teacher}")

    def __repr__(self):
        return f"{self.name} {self.code} {self.teacher}"
