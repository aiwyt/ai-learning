x = 10
print(type(x)) # <class 'int'>

x = "我现在是字符串"
print(type(x)) # <class 'str'>

#input()拿到的永远是字符串
age_str = input("你几岁：")
print(type(age_str)) # <class 'str'>

age_num = int(age_str)
print(age_num + 1)


int("20") # 20
int(3.9) # 3
float("3.14") # 3.14
str(100) # "100"
# bool()函数
a = bool("   ") # True
bool("hello") # True
bool("") # False
bool(" ") # True

print(a)