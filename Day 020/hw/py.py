# 1)შექმენით ცვლადი შეინახეთ მნიშვნელობად რაიმე სტრინგი,შენი დავალებაა შეამოწმო,თუ ცვლადში შენახული სტრინგის პირველი
#  ასო არის დიდი,მაგ შემთხვევაში დაუპრინტე ეს სიტყვა uppercase ში,სხვა შემთხვევაში კი დაუპრინტე ეს სიტყვა lowercase ში

string = "Sandro"
if string[0].isupper():
    print(string.upper())
else:
    print(string.lower())

# 2)მომხმარებელს შემოატანინე სახელი,თუ მომხმარებლის შემოტანილი სახელი შეიცავს ერთ uppercase ასოს მაინც(for loop გამოიყენეთ)მაშინ დაპრინტე
#  ეს სახელი მთლიანად lowercase ში,სხვა შემთხვევაში დაპრინტე ეს სახელი რომელიც იქნება capitalize
name = input("შემოიყვანეთ თქვენი სახელი:")
has_upper = False
for uppername in name:
    if uppername.isupper():
        has_upper = True
        break

if has_upper:
    print(name.lower())
else:
    print(name.capitalize())

#   3)შექმენი ცვლადი რომელსაც გადაეცემა პატარა ასოებით დაწერილი სტრინგი,შენი დავალებაა
#  დააბრუნო ეს სტრინგი ისე რომ პირველი ასო იყოს დიდი
string3 = "sandrovar"
print(string3.capitalize())

# 4)შექმენი სია სადაც გექნება მოთავსებული lowercase სახელები,შენი დავალებაა გადაიყვანო და გამოპრინტო ყველა მათგანი uppercase ში
namez = ["sandro", "gela", "tengiza", "vaxtanga", "malxaza"]
for uppernamez in namez:
    print(uppernamez.upper())

# 5)შექმენი სია სადაც გადაცემული გექნებათ სხვადასხვა მონაცემთა ტიპები,შენი დავალებაა შეამოწმო,თუ სიაში იმყოფება სტრინგ ტიპის მონაცემი,
# ეს სტრინგი უნდა გადააქციო uppercase ად და უნდა დააბრუნოთ ამ სტრინგიდან ბოლო 3 ასო გამოიყენეთ მინუს ინდექსები

random_list = [1,2,3,"sandro","gio"]

for i in random_list:
    if type(i) == str:
        print(random_list[-3:])