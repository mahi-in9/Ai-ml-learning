Classroom = {
    "student1": {"name": "Mahi", "score": 95},
    "student2": {"name": "Jennie", "score": 100},
    "student3": {"name": "Aman", "score": 96}
}

print(Classroom["student1"]["score"])

for student_id, info in Classroom.items():
    print(f"{student_id}: {info["name"]} scored {info["score"]}");



