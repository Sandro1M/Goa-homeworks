# 1) მომხმარებელს შემოატანინეთ სიტყვა. ტერმინალში კი დაბეჭდეთ ეს სიტყვა ისე რომ იყოს:

# 1. ყველა პატარა ასო;
# 2. ყველა დიდი ასო;
# 3. პირველი ასო დიდი, ხოლო ყველა დანარჩენი პატარა.
nam = input("Paste your name:")

print(nam.lower())

print(nam.upper())

print(nam.capitalize())

# 2) მომხმარებელს შემოატანინეთ სამი წინადადება და თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი:
# პირველ წინადადებაზე — .lower()
# მეორე წინადადებაზე — .upper()
# მესამე წინადადებაზე — .capitalize()

word = input("Enter any word:")

print(word.lower())
print(word.upper())
print(word.capitalize())

# 3) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა დაბეჭდეთ
#  "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names". გაითვალისწინეთ, რომ მომხმარებელმა შეიძლება
#  თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა შრიფტის ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება
#  არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)

my_name = "Sandro"

your_name = input("Enter your name:")

if your_name == my_name:
    print("we have same names! :D ")

else:
    print("we have difrent names... ! :C ")

# 4) ცვლადში შეინახე წინადადება, დაწერე ისეთი პროგრამა რომ მხოლოდ წინადადების პირველი სიტყვა იყოს დიდი ასოთი, დანარჩენი კი იყოს პატარა.   -_o ez?
# 4

randomwerb = "Hello"

print(randomwerb.capitalize())

# 5) კომენტარის სახით ჩამოწერეთ ყველა სტრინგის მეთოდი, რომელიც ისწავლეთ.
#  თითოეულს მიუწერეთ დეტალური განმარტება და მათზე მოიყვანეთ თითო-თითო მაგალითი.

# capitalize - sandro | Sandro
name = "sandro"
print(name.capitalize())

# lower - Sandro = sandro (magalitad moviyvane es)
name2 = "vlado"
print(name2.lower())

# upper - Sandro = SANDRO
name3 = "gela"
print(name3.upper())