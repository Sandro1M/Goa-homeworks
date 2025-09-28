# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი და უნდა 
# ჩამოაშორო ბოლო და პირველი ასოები შემდეგ კი დააბრუნოთ

# def remove_first_and_last_char(s):
#  return s[1:-1]

# print(remove_first_and_last_char("სალამი"))
# print(remove_first_and_last_char("ნახვამდის"))
    
# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სია, თუ 
# სია სიგრძე აღემატება 4 ელემენტს დააბრუნეთ რომ  სია ძალიან დიდია,
#  სხვა შემთხვევაში დააბრუნეთ ეს გადმოცემული სია

def check_list_size(lst):
    if len(lst) > 4:
        return "სია ძალიან დიდია"
    else:
        return lst

print(check_list_size(1, 2, 3))       
print(check_list_size([1, 2, 3, 4, 5]))  