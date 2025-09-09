num = 1
while num <= 20:
    print(num)
    num += 1

correct_pin = "1234"
user_pin = input("შეიყვანე პინ კოდი: ")

while user_pin != correct_pin:
    print("არასწორი პინ კოდი, სცადე ისევ.")
    user_pin = input("შეიყვანე პინ კოდი: ")

print("პინ კოდი სწორია!")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
for i in range(1, 31):
    if i % 2 != 0:
        print(i)

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1