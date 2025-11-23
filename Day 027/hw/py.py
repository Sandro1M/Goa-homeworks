# 1) ცვლადში შეინახეთ ნებისმიერი სიტყვა, შემდეგ კი მომხმარებელსაც შემოატანინეთ რაიმე სიტყვა, თუ თქვენი სიტყვები ერთმანეთს დაემთხვევა
#  გამოუტანეთ "Our words are similar !", სხვა შემთხვევაში - "We have different words". hint: დაგჭირდებათ პირობითი განცხადებები და სტრინგის
#  მეთოდები. ეს შემოწმება უნდა იყოს case-insensitive

idk123 = "hello"

user = input("შემოიყვანეთ თქვენი რანდომ სიტყვა: ")

if idk123.capitalize() == user.capitalize():
    print("Our words are similar !")
else:
    print("We have different words")