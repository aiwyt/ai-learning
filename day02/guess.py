"""
•程序随机生成 1 ~ 100 的数
•用户循环输入猜测
•提示「太大了 / 太小了 / 猜对了」
•猜对后打印用了几次
•输入 q 可以退出
•用户输入非数字时不能崩溃
"""


import random

random_num = random.randint(1, 100)
count = 0

num = input("请输入数字(输入 q 退出):")

while num != 'q':
    if num.isdigit():
        guess = int(num)
        count += 1

        if guess > random_num:
            print("太大了")
        elif guess < random_num:
            print("太小了")
        else:
            print("猜对了!")
            print(f"您一共猜测了 {count} 次")
            break
    else:
        print("请输入有效数字")

    num = input("请输入数字(输入 q 退出):")