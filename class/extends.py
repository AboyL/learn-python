from dataclasses import dataclass

@dataclass
class Animal:
  name:str
  def speak(self):
      print("动物发出声音")

class Dog(Animal):
    pass

# 创建子类实例
dog = Dog("小狗")
dog.speak()  # 输出: 动物发出声音