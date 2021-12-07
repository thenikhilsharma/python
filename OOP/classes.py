class emp:
  empcount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    emp.empcount += 1

  def displaycount(self):
    print("totla employee %d" %emp.empcount)
  
  def displayemp(self):
    print("name : ",self.name,"salary : ", self.salary)

emp1 = emp("nick", 150000)
emp2 = emp("sick", 200)
emp1.displayemp()
emp2.displayemp()