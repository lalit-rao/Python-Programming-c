class Person:
  # name = "Harry"
  # occupation = "Software Developer"
  # networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
    print(f"{self.name} has a salary of {self.networth}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"
a.networth = 100000

b.name = "Nitika"
b.occupation = "HR"
b.networth = 1000000

c.name = "Rahul"
c.occupation = "Manager"
c.networth = 10000000

# print(a.name, a.occupation)
a.info()
b.info()
c.info()