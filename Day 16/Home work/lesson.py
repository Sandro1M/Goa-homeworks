# 1) შემოყვანილი რიცხვის ლუწ/კენტობა
number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("even")  # ლუწია
else:
    print("odd")   # კენტია

# 2
my_name = "გიორგი"
user_name = input("შეიყვანეთ თქვენი სახელი: ")
if user_name == my_name:
    print("Hello")
else:
    print("Bye")

# 3)
score = int(input("შეიყვანეთ თქვენი ქულა: "))
if score > 90:
    print("A")
elif score > 70:
    print("B")
elif score > 50:
    print("C")
else:
    print("D")

# 4) 1-დან 100-მდე რიცხვების ლუწ/კენტობა while ციკლით (უიმე {}):

i = 1
while i <= 100: input
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")
    i += 1
    print(i-=1)