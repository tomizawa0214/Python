class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def hello(self):
    print('Hello,', str(self.name))
  def get_age(self):
    return self.age

kawasaki = Person('kawasaki', 250)
isshiki = Person('isshiki', 19)
# kawasaki.hello()
# print(isshiki.get_age())

# class Student(Person):
#   pass

# kawasaki = Person('kawasaki', 250)
# isshiki = Student('isshiki', 18)
# print(type(kawasaki))
# print(type(isshiki))
# isshiki.hello()

# class Student(Person):
#   def __init__(self, name, age, school):
#     self.name = name
#     self.age = age
#     self.school = school
#   def get_school(self):
#     return self.school

# class Student(Person):
#   def __init__(self, name, age, school):
#     super().__init__(name, age)
#     self.school = school
#   def get_school(self):
#     return self.school

# isshiki = Student('isshiki', 18, 'Imperial univ')
# isshiki.hello()
# print(isshiki.get_school())

class Student(Person):
  def __init__(self, name, age, school):
    super().__init__(name, age)
    self.school = school
  def get_school(self):
    return self.school
  def hello(self):
    super().hello()
    print('You are a student of', self.school)

# isshiki = Student('isshiki', 18, 'Imperial univ')
# isshiki.hello()

# 整数値「100」はfloat型のインスタンスか
print('isinstance(100, float):', isinstance(100, float))

# studentはPersonクラスのインスタンスか
student = Student('isshiki', 18, 'Imperial univ')
print('isinstance(student, Person):', isinstance(student, Person))

# StudentクラスはPersonクラスの派生クラスか
print('issubclass(Student, Person):', issubclass(Student, Person))

# PersonクラスはPersonクラスの派生クラスか
print('issubclass(Person, Person):', issubclass(Person, Person))

# 「100」はfloatクラスまたはstrクラスのインスタンスか
print('isinstance(100, (float, str)):', isinstance(100, (float, str)))

# StudentクラスはPersonクラスまたはStudentクラスの派生クラスか
print('issubclass(Student, (Person, Student)):', issubclass(Student, (Person, Student)))