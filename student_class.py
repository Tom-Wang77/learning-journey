class Student:
    def __init__(self,name,age,goal):
        self.name=name
        self.age=age
        self.goal=goal
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        print(f"I'm {self.age} years old")
        print(f"My goal is to {self.goal}")
    def is_adult(self):
        return self.age >= 18
Tom = Student("Tom",20,"AI engineer")
Jerry = Student("Jerry",15,"Web developer")
students=[Tom,Jerry]
print("="*30)
Tom.introduce()
print("=*30")
if Tom.is_adult():
    print(f"{Tom.name} is an adult")
else:
    print(f"{Tom.name} is a child")
print("="*30)
print("Class introduce")
for student in students:
    student.introduce()
    print("-"*20)