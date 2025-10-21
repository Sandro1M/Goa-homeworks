students = ["მარიამი", "გიორგი","ანა" , "ნიკა", "ანა"]

# აფფენდით ვამატებთ სიაში რამე ახალ სტრინგს
students.append("სანდრო")
print("appended:", students)

# პოპ ით ბოლოს ვიღებთ სიიდან
removed = students.pop()
print("with-out pop:", students)
print("poped:", removed)

# qaunts aketebs anu itvlis siashi arsebul elementebs
print("caunted:", len(students))


# anas edzebs tu ramdenia da caunts uketebs
count_ana = students.count("ანა")
print("'ანა' caunt:", count_ana)

# maris adgilivipove tu sadaa 
idk = students.index("მარიამი")
print("მარიამი ინდექსზეა:", idk)

# CW-2

fruits = {"ვაშლი", "ბანანი", "მსხალი", "ატამი"}

print("საწყისი სეტი:", fruits)

fruits.add("მარწყვი")
print("add() შემდეგ:", fruits)


removed = fruits.pop()
print("pop() შემდეგ:", fruits)
print("ამოღებული ელემენტი იყო:", removed)

fruits.remove("ბანანი")   
print("remove() შემდეგ:", fruits)

fruits.clear()
print("clear() შემდეგ:", fruits)