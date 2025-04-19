age = int(input("Enter Age: "))

if age < 13:
    print("You are a kid")
elif age >= 13 and age < 19:  # Corrected the condition for 'teen'
    print("You are a teen")
elif age >= 19 and age < 60:  # Corrected the condition for 'adult'
    print("You are an adult")
else:
    print("You are a senior")
