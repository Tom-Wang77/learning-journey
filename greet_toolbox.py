def say_hello():
    print("=" * 30)
    print("Hello! Welcome to the greet toolbox")
    print("=" * 30)
say_hello()
say_hello()
def greet(name,mood):
    print(f"Hi,{name}!")
    print(f"I heard you are feeling {mood} today, hope you will have a great day!")
greet("Tom","Happy")
greet("Jerry","Sad")
def calc_sum(a,b):
    total = a + b
    return total
result = calc_sum(10,20)
print(f"10+20={result}")
def smart_greet():
    name=input("What's your name?")
    mood=input("How's going today?")
    print(f"Hi,{name}!")
    print(f"Are you feeling {mood} today? Let me be with you today!")
smart_greet()
print("=" * 30)
print("AI toolbox - choose the fuction you want to use")
print("1. Simple greeting")
print("2. Smart greeting")
choice= input("Pls choose 1/2.")
if choice=="1":
    say_hello()
elif choice=="2":
    smart_greet()
else:
    print("Invalid choice, please choose 1 or 2.")