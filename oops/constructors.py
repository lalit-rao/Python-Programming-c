class Person:
    def __init__(self, name, occupation):
        print("Hey I am a person")
        self.name = name
        self.occ = occupation

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Divya", "HR")
b = Person("Shubham", "Software Developer")
c = Person("Nitika", "Accountant")

a.info()
b.info()
c.info()
