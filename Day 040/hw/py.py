# 1) 1
numbers = range(1,11)
kvadrati = []
for x in numbers:
    kvadrati.append(x * x)
print(kvadrati)
# 2
nums = [1,2,3,4,5,6,7,8,9,10]
result1 = []
for i in nums:
    if i % 2 == 0:
        result1.append(i)
print(result1)
# 3
words = ["apple", "banana", "cherry", "date"]

u_w = []
for i in words:
    u_w.append(i.upper())
print(u_w)

# 4
animals = ["cat", "dog", "elephant", "mouse"]
a_l = []
for i in animals:
    a_l.append(len(i))
print(a_l)

# 5

nums2 = [5, 12, 8, 20, 3, 15]
morethen_10 = []

for i in nums2:
    if i > 10:
        morethen_10.append(i)
print(morethen_10)

# 6

nums3 = [1, 2, 3, 4]
result2 = []

for i in nums3:
    result2.append(i *5)
print(result2)

# 7
words2 = ["hello", "world", "python", "programming", "list"]

result3 = []

for i in words2:
    if i[0] == "p":
        result3.append(i)
print(result3)

#8
listof_2nums = range(1,10)

for i in listof_2nums:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

# 9

# 💖