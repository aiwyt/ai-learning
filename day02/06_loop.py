#遍历字符串
for ch in "abc":
    print(ch)


#遍历列表
for fruit in ["苹果", "香蕉", "橘子"]:
    print(fruit)

#range() 0 - n-1 之间的整数序列
for i in range(5):
    print(i,end=" ")
print()


for i in range(1,6):
    print(i,end=" ")
print()

for i in range(0,10,2): # 0 - 9 之间的偶数
    print(i,end=" ")
print()


for i in range(5,0,-1):
    print(i,end=" ")
print()



#while
count = 0
while count < 5:
    print(count,end = " ")
    count += 1
print()

#break
for i in range(10):
    if i == 5:
        break
    print(i,end=" ")
print()



for i in range(10):
    if i == 2:
        continue
    print(i,end=" ")
print()


#for-else
for i in range(5):
    if i == 300:
        print("i等于3")
        break
else:
    print("没有找到i等于3")
print()



for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i*j}",end="\t")
    print()
    