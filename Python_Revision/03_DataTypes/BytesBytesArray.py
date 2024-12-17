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
