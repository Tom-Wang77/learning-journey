student={"name":"Tom","age":25,"goal": "AI engineer","City":"Shanghai"}
print("=" * 30)
print(f"Student's file:{student}")
print("=" * 30)
print(f"student's name:{student['name']}")
print(f"student's age:{student['age']}")
print(f"student's goal:{student['goal']}")
print(f"student's location:{student['City']}")
student['age']=26
print(f"student's new age:{student['age']}")
student['hobby']="coding"
print(f"add stundent's hobby:{student['hobby']}")
class_dict={"Tom":{"age":26,"goal":"AI engineer"},"Jerry":{"age":25,"goal":"Data science"},"Mike":{"age":23,"goal":"Web developer"}}
print("=" * 30)
print(f"Classmate's file:")
for name, info in class_dict.items():
    print(f"{name}:{info}")
query=input(f"Who you wanna to search in this class")
if query in class_dict:
    print(f"{query}'s info:{class_dict[query]}")
else: print(f"{query} is not in this class")
