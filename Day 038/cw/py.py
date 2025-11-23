# 1)შექმენით dictionary სადაც შენახული იქნება შენი სახელი, ასაკი და ქალაქი.

# შემდეგ ამოიღეთ კონკრეტული მნიშვნელობა და შეინახე ცვლადში.

# ასევე შეცვალეთ რომელიმე მნიშვნელობა რაც გექნება dictionary ში.

# წაშალე ერთი ელემენტი.

# for ციკლის მეშვეობით გამოიტანე თითოეული key და value (არ ამიხსნია ჯერ და მაინტერესებს თუ იზამთ :)) )


# ასევე გამოიტანეთ მხოლოდ value ები

# 1
person = {
    "name": "სანდრო",
    "age": 15,
    "city": "თბილისი"
}

print(person.values())

user_add = person.get("ლუკა")
person["name"] = "nika"

city = person["city"]
print("ჩემი ქალაქია:", city)

person["age"] = 16

removed_value = person.pop("age")
print(person)