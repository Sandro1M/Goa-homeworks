# 1


word = input("შემოიტანე სიტყვა: ")

print("პატარა ასოებით:", word.lower())
print("დიდი ასოებით:", word.upper())
print("პირველი ასო დიდი, დანარჩენი პატარა:", word.capitalize())
# dzivs avamusave 

# 2 mas vxvdebi magram miwirs dzalian su secdomebi maqvsxolme
sentence1 = input("შემოიტანე პირველი წინადადება: ")  # lower() - პატარა ასოები
sentence2 = input("შემოიტანე მეორე წინადადება: ")   # upper() - დიდი ასოები
sentence3 = input("შემოიტანე მესამე წინადადება: ")  # capitalize() - პირველი დიდი, სხვა პატარა

print("პატარა ასოებით:", sentence1.lower())
print("დიდი ასოებით:", sentence2.upper())
print("პირველი დიდი, დანარჩენი პატარა:", sentence3.capitalize())

my_name = "sandro"  # შენს სახელს შეგიძლია შეცვლა

user_name = input("ჩაწერე შენი სახელi: ")

# ორივე lowercase-ში გადაყვანით ვადარებთ სწორად
if my_name,lower() == user_name.lower():
    print("names are similar!")
else:
    print("different names...")

# ????

# 3

# vermivxvdi ...

# 4

# .lower() — ყველა ასოს გადაყვანა პატარა ასოდ
# მაგ: "HI".lower() => "hi"

# .upper() — ყველა ასოს გადაყვანა დიდ ასოდ
# მაგ: "hi".upper() => "HI"

# .capitalize() — მხოლოდ პირველი ასო დიდი, დანარჩენი პატარა
# მაგ: "hI".capitalize() => "Hi"


# .replace(old, new) — ტექსტში რაიმეს ჩანაცვლება
# მაგ: "hello world".replace("world", "Georgia") => "hello Georgia"

# დანარჩენივერმივხვდი ბოდიშით  და ერთგან რაღაც არმუშაობს
