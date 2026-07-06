total = int(input("How many people are in the roll call?"))
count = 0
print("=" * 30)
print("Begin counting")
print("=" * 30)
while count < total:
    count = count + 1
    print(f"There are {count} people in the roll call")
print("=" * 30)
print("Line the odd numbers and even numbers under 10:")
num = 1
while num<= 10:
    if num % 2 ==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
    num = num + 1
    
