age_str = input ("How old are you?")
age = int(age_str)
name = input("Whats your name?")
print (f"Hi, {name}")
print (f"The type of your age is {type(age)}")
is_adult = age >= 18
is_young = age <= 30
is_middle_aged = age > 30 and age < 60
print (f"{name} is an adult or not? {is_adult}")
print (f"{name} is young or not? {is_young}")
print (f"{name} is middle or not? {is_middle_aged}")
print (f"The age which you entered is {age} and the type of your age is {type(age)}")