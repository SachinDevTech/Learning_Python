# A dictionary is a collection of key-value pairs.
# It is unordered (Python < 3.7), mutable (can be changed), and indexed by keys.

# Example:
person = {
    "name": "Sachin",
    "age": 22,
    "is_student": True
}

"""🔧 Operations on Dictionaries"""

# 1. Accessing values
print(person["name"])         # Output: Sachin
print(person.get("age"))      # Output: 22

# 2. Adding new key-value pair
person["email"] = "sachin@example.com"

# 3. Updating a value
person["age"] = 23

# 4. Deleting a key
del person["is_student"]      # removes the key 'is_student'

# 5. Checking existence of key
print("name" in person)       # Output: True


"""🧰 Useful Dictionary Functions/Methods"""

# keys(), values(), items()
print(person.keys())          # dict_keys(['name', 'age', 'email'])
print(person.values())        # dict_values(['Sachin', 23, 'sachin@example.com'])
print(person.items())         # dict_items([('name', 'Sachin'), ('age', 23), ('email', 'sachin@example.com')])

# get() with default
print(person.get("gender", "Not specified"))  # Output: Not specified

# update() to merge another dictionary
person.update({"gender": "Male", "country": "India"})

# pop() to remove a key and get its value
email = person.pop("email")   # removes and returns 'email'



"""🔁 Looping through a Dictionary"""


# Loop through keys
for key in person:
    print(key, person[key])

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")



"""📦 Use Cases of Dictionaries"""

# Storing related data:

user = {"username": "sachin123", "password": "abc@123"}
# Word frequency counter:

text = "apple banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'apple': 2, 'banana': 1}


# Representing JSON data (from APIs):

# JSON response from API is often converted into a Python dictionary
response = {"status": "success", "data": {"id": 1, "value": "abc"}}


# Switch/Case alternative:

def switch_demo(day):
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday"
    }.get(day, "Invalid day")

print(switch_demo(2))  # Output: Tuesday