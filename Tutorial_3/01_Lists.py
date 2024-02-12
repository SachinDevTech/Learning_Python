"""Lists in Python"""
# A list in Python is an ordered collection of items, mutable and versatile for storing multiple values.
# Lists can store multiple kind of values like int, float, string etc.

# Creating a list
my_list = [1, 2, 3, 4, 5]
my_details = ["Sachin", 21, True, 99.80]

# Accessing elements in a list
print("First element:", my_list[0])  # Output: 1
print("Last element:", my_list[-1])  # Output: 5

# Slicing a list
print("Sliced list:", my_list[1:3])  # Output: [2, 3]

# Modifying elements in a list
my_list[0] = 0
print("Modified list:", my_list)  # Output: [0, 2, 3, 4, 5]

# Appending elements to a list
my_list.append(6)
print("Appended list:", my_list)  # Output: [0, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(3)
print("List after removing element:", my_list)  # Output: [0, 2, 4, 5, 6]

# Inserting elements into a list at a specific position
my_list.insert(2, 3) #insert(index, value)
print("List after inserting element:", my_list)  # Output: [0, 2, 3, 4, 5, 6]

# Extending a list with another list
my_list.extend([7, 8, 9])
print("Extended list:", my_list)  # Output: [0, 2, 3, 4, 5, 6, 7, 8, 9]

# Finding the index of an element in a list
index = my_list.index(5)
print("Index of element 5:", index)  # Output: 4

# Counting occurrences of an element in a list
count = my_list.count(3)
print("Number of occurrences of 3:", count)  # Output: 1

# Reversing a list
my_list.reverse()
print("Reversed list:", my_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 0]

# Sorting a list
my_list.sort() #will sort in ascending order 
print("Normal Sorted list:", my_list)  # Output: [0, 2, 3, 4, 5, 6, 7, 8, 9]

my_list.sort(reverse=True)
print("Reversed Sorted list:", my_list) 



"""List Methods"""

# Removing the last element from a list
last_element = my_list.pop()
print("Popped element:", last_element)  # Output: 9
print("List after popping:", my_list)  # Output: [0, 2, 3, 4, 5, 6, 7, 8]

# Clearing a list
my_list.clear()
print("Cleared list:", my_list)  # Output: []
