name = input("Enter your name: ")

# "Giorgi"


for i in name:
    if i.isupper():
        print(name.lower())
        break
else:
    print(name.capitalize())
# hw1

dog_names = ["Max","Rex","Drogo","zeus"]



for i in dog_names:
    
    if len(i) < 5 and i[0].isupper():
        print(i[:3])
    else:
        print(i, "does not meet conditions")
# hw2


names = ["giorgi","sandro","luka","goga"]

for i in names:
    print(i.upper())
# hw3

l = ["Ohioo",5,5.5,True,"Sandrik"]


for i in l:
    if type(i) == str:
        i = i.upper()
        print(i[-3:])
        