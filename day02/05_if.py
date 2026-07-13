#三元表达式
score = 80
result = "及格" if score >= 60 else "不及格"

print(result) # 及格


#利用真假值判断
name = input("请输入你的名字：")

if name:
    print(f"你好，{name}")
else:
    print("你好，游客")


item = []
if not item: ## 等价于 if len(item) == 0
    print("购物车为空")
