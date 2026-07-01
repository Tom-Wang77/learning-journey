mood = input('Hows your feeling today?(happy/sad/tired)')
if mood == "happy":
    print(f"Good to hear that you are {mood} today!")
elif mood == "sad":
    print(f"Sry to hear that you are {mood} today. Hope you will be better soon!")
elif mood == "tired":
    print(f"Get some rest! Getting {mood} is fucked")
else:
    print(f"Fine, you are {mood} today, {mood} is normal and acceptable")
age_str = input("By the way, how old are you?")
age = int(age_str)
print(f"You are {age} years old")
if age < 18:
    print(f"You are a minor, pls take care of yourself")
elif age >= 18 and age <50:
    print(f"You are an adult, pls take your responsibility")
else:
    print(f"You are not young anymore, pls take care of yourself.")
