# Set
unique_numbers = {1, 2, 3, 4, 4, 5}  # Duplicate '4' will be removed
unique_numbers.add(6)  # Add new element
unique_numbers.discard(2)  # Remove element
print(f"Set: {unique_numbers}")

# Frozen Set
immutable_set = frozenset([1, 2, 3, 4])
# immutable_set.add(5)  # ❌ Will raise AttributeError (immutable)
print(f"Frozen Set: {immutable_set}")
