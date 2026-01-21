# 1.

try:
    print(10 / 0)
except:
    print("this move isnot alowed")

# 2.

try:
    num1 = int("txt")
except :
    print("This isnt integer")

# 3

try:
    print("sandro" + 100)
except:
    print("error int+str :\ ")

# 4

try:
    list = [1, 22]
    print(list[2])
except:
    print("error :\ ")

# 5

try:
    age = int("5")
except:
    print("err")

# 6

try:
    x = int("gka")
except:
    print("err")

try:
    x = int("10.5") 
except:
    print("err")

try:
    names = ["gio", "sandro"]
    names.remove("gioo")
except:
    print("131313")

try:
    a, b = [1, 2, 3] 
except:
    print("err")

try:
    a, b = [1, 2, 3 ,4] 
except:
    print("err")

try:
    idk = 10 + "20"
except:
    print("err")

try:
    print(len(100)) 
except:
    print("err")

try:
    x = 555
    print(x[3])
except:
    print("1414141242")

try:
    res = "გამარჯობა" / 2
except:
    print("err")

try:
    for i in 10: 
        print(b)
except:
    print(";_;")

# 2.

# ნეიმ ერორი სახელის შეცვლა როცა რამე ცვლადს შექმნი და პრინტში სხვანაირად მიუთითებ ამის მაგალითი ეს შეიძლება ავიღოთ

# ინდექს ერორი როდესაც ის ინდექსი სიაში არ არსებობს და მაინც ვუთითებთ, ეგ არის ერორი 

# ვალუე ერორი როდესაც იღებს რაღაც ვალუეს კოდი მაგრამ არარის შესაბამისი კოდში რაც წერია იმის

# ტაიპ ერორის დროს მაგალითად შეიძლება ავიღოთ მათემატიკური პოერაციის სტრინგს მივუმატოთ ინტეჯერი "5" +5 ეს ვერ ხერხდება რის გამოც ერორია