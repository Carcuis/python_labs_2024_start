import json

# Step 1: Open and read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Step 2: Process the JSON data
for student in data["students"]:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()  # Print a newline for better readability