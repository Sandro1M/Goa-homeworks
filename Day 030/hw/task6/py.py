students_ids = [101, 202, 303, 404, 202]

unique_ids = set(students_ids)

if len(students_ids) != len(unique_ids):
    print("მოიძებნა ერთიდაიგივე id-ები!")
else:
    print("ყველა id უნიკალურია.")