Detailed explanation of **data types in Python** along with **advanced examples and operations** for each type. 

---

### 1️⃣ **Numeric Data Types**
#### 📘 **int, float, complex**
- **int**: Integer numbers (e.g., 5, -10, 0)
- **float**: Decimal numbers (e.g., 3.14, -7.5)
- **complex**: Numbers with a real and imaginary part (e.g., 2 + 3j)

#### **Example**
```python
# Integer
num_int = 100
print(f"Integer: {num_int}, Type: {type(num_int)}")  # Type: int

# Float
num_float = 12.34
print(f"Float: {num_float}, Type: {type(num_float)}")  # Type: float

# Complex
num_complex = 4 + 5j
print(f"Complex: {num_complex}, Real Part: {num_complex.real}, Imaginary Part: {num_complex.imag}")  # Complex number operations

# Operations
sum_nums = num_int + num_float  # Addition of int and float
complex_multiply = num_complex * (2 + 3j)  # Multiplying two complex numbers
print(f"Sum of int and float: {sum_nums}, Multiplication of complex: {complex_multiply}")
```

---

### 2️⃣ **Text Data Type**
#### 📘 **str (String)**
- Strings are a sequence of characters, enclosed in single, double, or triple quotes.

#### **Example**
```python
# String
greeting = "Hello, Sachin!"
multi_line = """This is 
a multi-line 
string."""
print(f"Greeting: {greeting}, Type: {type(greeting)}")

# Operations
upper_case = greeting.upper()  # Converts to uppercase
split_text = greeting.split(",")  # Splits on the comma
concat = greeting + " How are you?"  # Concatenation
print(f"Uppercase: {upper_case}, Split: {split_text}, Concatenated: {concat}")
```

---

### 3️⃣ **Sequence Data Types**
#### 📘 **list, tuple, range**
1. **list**: Mutable, allows duplicates, heterogeneous elements.
2. **tuple**: Immutable, allows duplicates, heterogeneous elements.
3. **range**: Immutable, generates a sequence of numbers.

#### **Example**
```python
# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item to list
fruits.remove("banana")  # Remove item from list
print(f"List after operations: {fruits}")

# Tuple
coordinates = (10, 20, 30)  # Immutable
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")

# Range
range_seq = list(range(1, 11, 2))  # Generates numbers from 1 to 10 with step of 2
print(f"Range as List: {range_seq}")
```

---

### 4️⃣ **Mapping Data Type**
#### 📘 **dict (Dictionary)**
- Collection of key-value pairs. Keys must be unique and immutable.

#### **Example**
```python
# Dictionary
student = {"name": "Sachin", "age": 21, "skills": ["Python", "React"]}
student["age"] = 22  # Update age
student["location"] = "Raipur"  # Add new key-value pair
print(f"Student Dictionary: {student}")

# Operations
keys = student.keys()  # Get all keys
values = student.values()  # Get all values
name = student.get("name")  # Access value using key
print(f"Keys: {keys}, Values: {values}, Name: {name}")
```

---

### 5️⃣ **Set Data Type**
#### 📘 **set, frozenset**
- **set**: Unordered, no duplicates, mutable.
- **frozenset**: Immutable version of a set.

#### **Example**
```python
# Set
unique_numbers = {1, 2, 3, 4, 4, 5}  # Duplicate '4' will be removed
unique_numbers.add(6)  # Add new element
unique_numbers.discard(2)  # Remove element
print(f"Set: {unique_numbers}")

# Frozen Set
immutable_set = frozenset([1, 2, 3, 4])
# immutable_set.add(5)  # ❌ Will raise AttributeError (immutable)
print(f"Frozen Set: {immutable_set}")
```

---

### 6️⃣ **Boolean Data Type**
#### 📘 **bool**
- **True** or **False** values used in logical operations.

#### **Example**
```python
# Boolean
is_student = True
is_graduated = False
result = is_student and not is_graduated  # Logical operation
print(f"Boolean result: {result}, Type: {type(result)}")
```

---

### 7️⃣ **Binary Data Types**
#### 📘 **bytes, bytearray, memoryview**
- **bytes**: Immutable sequence of bytes.
- **bytearray**: Mutable sequence of bytes.
- **memoryview**: View of memory buffer.

#### **Example**
```python
# Bytes
byte_data = bytes([65, 66, 67])  # ASCII values for A, B, C
print(f"Bytes: {byte_data}, Decoded: {byte_data.decode('utf-8')}")

# Bytearray
byte_array = bytearray([68, 69, 70])  # ASCII values for D, E, F
byte_array[0] = 90  # Change first element
print(f"Bytearray: {byte_array}, Decoded: {byte_array.decode('utf-8')}")

# Memoryview
mem_view = memoryview(byte_data)
print(f"Memory View of Bytes: {mem_view[0]}")
```

---

### 8️⃣ **None Data Type**
#### 📘 **NoneType**
- Represents a **null** or **no value**. It is used to define a variable with no initial value.

#### **Example**
```python
# NoneType
value = None
if value is None:
    print("The value is None")
```

---

### 🔥 **Summary of Data Types and Their Usage**
| **Data Type**    | **Example**                | **Mutability** | **Operations**                              |
|-----------------|--------------------------|-----------------|-------------------------------------------|
| **int, float, complex** | `num = 10`, `pi = 3.14`, `c = 2+3j` | Immutable   | Arithmetic (`+`, `-`, `*`, `/`, `%`, `**`) |
| **str**          | `'Hello'`                 | Immutable     | Slicing, Concatenation, `.upper()`, `.split()` |
| **list**         | `[1, 2, 3]`               | Mutable       | Append, Remove, Index, Sort, Reverse       |
| **tuple**        | `(1, 2, 3)`               | Immutable     | Index, Slicing                            |
| **dict**         | `{"name": "Sachin"}`      | Mutable       | Access, Update, `.keys()`, `.values()`     |
| **set**          | `{1, 2, 3}`               | Mutable       | Add, Remove, Union, Intersection          |
| **frozenset**    | `frozenset([1, 2, 3])`    | Immutable     | Union, Intersection (No Add/Remove)       |
| **bool**         | `True`, `False`           | Immutable     | Logical (`and`, `or`, `not`)              |
| **bytes**        | `bytes([65, 66, 67])`     | Immutable     | Slicing, Decoding                         |
| **bytearray**    | `bytearray([68, 69, 70])` | Mutable       | Slicing, Decoding, Modification           |
| **memoryview**   | `memoryview(bytes(5))`    | Immutable     | View of data buffer                       |
| **NoneType**     | `None`                    | Immutable     | Used for placeholder or null check       |

---

### 🚀 **Practice Questions**
1. Write a program to input a **list** of numbers and remove **duplicates**.
2. Create a **dictionary** of students with names as keys and marks as values. Print the student with the highest marks.
3. Write a Python program to check if a given **string** is a **palindrome**.
4. Write a Python program to **swap two numbers** without using a third variable.
5. Convert a **list of tuples** into a **dictionary** using a Python function.

---

With this, you now have a **solid understanding of Python data types** with **advanced examples, operations, and practice problems**. Let me know if you'd like to explore any part of this in more depth! 😊