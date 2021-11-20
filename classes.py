class parent:
  def func(self):
    print('one')
  
class parent2:
  def func2(self):
    print('two')


class child(parent, parent2):
  def func3(self):
    print("three")

ob = child()
ob.func3()