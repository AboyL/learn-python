from dataclasses import dataclass
# class 的继承 实现 静态类

@dataclass
class Father:
  name:str='father'
  age:int=30
  def run(self):
    print(f"我是{self.name},年龄{self.age}")
  @classmethod
  def see(cls):
    print('我是不需要实例化就可以调用的方法')
  @staticmethod
  def see2():
    print('我是不需要实例化就可以调用的方法2')
  def play2(self):
    print('打游戏')

class Play:
  def play(self):
    print('打游戏2')

class Child(Father, Play):
  def __init__(self,name,age,sex='男'):
    super().__init__(name, age)
    self.sex=sex
  def run(self):
    print(f"i am {self.name},my name {self.age}, sex is {self.sex}")
  @property
  def gage(self):
    return self.age+1
  @gage.setter
  def gage(self, varValue=1):
    self.age = self.age+varValue

f1=Father()
f1.run()
c1=Child(name='kid',age=20,sex='男')
c1.run()
c1.play2()
c1.play()
Child.see()
Child.see2()
print(c1.gage)
c1.gage=1
print(c1.gage)
