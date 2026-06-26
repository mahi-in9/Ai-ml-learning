student = {
    "name": "Mahi",
    "age": 21,
    "grade": "A",
    "subjects": ["Math", "Physics", "English"]
}

student["city"] = "Bangalore"

student["age"] = 22;

del student["grade"];

if "name" in student:
    print("Name found:", student["name"])

grade = student.get("grade", "Not Found");
print(grade);

print(student);

for key, value in student.items():
    print(f"{key} -> {value}");
