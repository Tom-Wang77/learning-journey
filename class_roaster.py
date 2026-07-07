classmate=["TOM", "JERRY", "MIKE", "LISA"]
print("=" * 30)
print(f"There are {len(classmate)} classmates in the class")
print("=" * 30)
for name in classmate:
    print(f"Hi, {name},welcome to the class!")
new_name=input("The new classmate's name: ")
classmate.append(new_name)
print(f"New classmate {new_name} has been added to the class,now there are {len(classmate)} students in the class")
print("=" * 30)
print("new classmate list:")
for i, name in enumerate(classmate,1):
    print(f"{i}.{name}")
numbers=[1,2,3,4,5,6,7,8,9,10]
total=0
for num in numbers:
 total=total+int(num)
print(f"the total of numbers from 1 to 10 is {total}")

