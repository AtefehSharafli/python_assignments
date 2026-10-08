class Product:
    def __init__(self):
        self.code=None
        self.name =None
        self.price=None
        print("کالا ایجاد شد")

    def save(self):
        print(f"save:{self.name} {self.code} {self.price}")

    def edit(self):
        print(f"edit:{self.name} {self.code} {self.price}")

    def remove(self):
        return f"{self.name} {self.code} {self.price}"

    def __repr__(self):
        return f"{self.name} {self.code} {self.price}"

class Electric (Product):
    def __init__(self):
        super().__init__()
        self.voltage=None

class Nonelectric(Product):
    def __init__(self):
        super().__init__()
        self.weight=None

class Laptop(Electric):
    def __init__(self):
        super().__init__()
        self.ram=None
        self.model=None

class Mobile(Electric):
    def __init__(self):
        super().__init__()
        self.screen_size=None

class Iphone(Mobile):
    def __init__(self):
        super().__init__()
        self.model=None

class Samsung(Mobile):
    def __init__(self):
        super().__init__()
        self.model=None

class Furniture(Nonelectric):
    def __init__(self):
        super().__init__()
        self.model=None
        self.color=None