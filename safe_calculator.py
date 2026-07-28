def get_number(prompt):
    while True:
        user_input=input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Wrong number. Please type a number.")
def safe_divide(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print("Can't divided")
        return None
def safe_get(d,key):
    try:
        return d[key]
    except KeyError:
        print(f"Can't find:{key}")
        return None
print("="*30)
print("Strong Calculator")
print("="*30)
num1=get_number("The first number:")
num2=get_number("The second number:")
result=safe_divide(num1,num2)
if result is not None:
    print(f"{num1}/{num2}={result}")
student={"name":"Tom","age":25}
name=safe_get(student,"name")
age=safe_get(student,"age")
grade=safe_get(student,"grade")
print(f"name:{name}")
print(f"grade:{grade}")
