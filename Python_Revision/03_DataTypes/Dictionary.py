# Dictionary
student = {"name": "Sachin", "age": 21, "skills": ["Python", "React", "Java", "JavaScript", "C++"]}
student["age"] = 22  # Update age
student["location"] = "Raipur"  # Add new key-value pair
print(f"Student Dictionary: {student}")

# Operations
keys = student.keys()  # Get all keys
values = student.values()  # Get all values
name = student.get("name")  # Access value using key
print(f"Keys: {keys}, Values: {values}, Name: {name}")
