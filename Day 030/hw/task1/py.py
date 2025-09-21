students = {
    "ნიკა": 98,
    "გიო": 78,
    "სანდრო": 91,
    "ლუკა": 66,
}

best_student = max(students, key=students.get)
print("ყველაზე მაღალი ქულააქვს:", best_student, "-", students[best_student])