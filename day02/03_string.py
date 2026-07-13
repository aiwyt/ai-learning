name = "小米"
score = 100

print(f"{name} 的分数是 {score}") # f-string
print(f"{name} 的分数是 {score:.1f}") #小米 的分数是 100.0
print(f"1 + 1 = {1 + 1}") # 1 + 1 = 2
print(f"平均分:{(90 + 100) / 2 :.2f}") # 平均分:95.00


s = "  Hello, Python World  "
#strip()：去掉两端空白（用户处理输入必备）
print(s.strip()) # Hello, Python World


#split(): 切分成列表（解析数据必用）
print("a,b,c".split(",")) #['a', 'b', 'c']
print("a b c".split()) #['a', 'b', 'c'] —— 不传参按空白切
print("2026-7-12".split("-")) #['2026', '7', '12']


#join(): 列表拼接成字符串（split 的逆操作）
print("-".join(["2024", "07", "12"])) # "2024-07-12"
print("-".join([])) # "" —— 空列表拼接成空字符串
print("".join(["a","b","c"])) # "abc"

#replace(): 替换
print("hello world".replace("o","t")) # hellt world


#大小写
print("Hello".upper())  # "HELLO"
print("HELLO".lower())  # "hello"



#判断
print("hello.py".startswith("hello")) # True
print("hello.py".endswith(".py")) # True
print("py" in "hello.py") # True


#查找与统计
print("hello".find("l")) # 2 —— 找到第一个 l 的索引
print("hello".count("l")) # 2 —— l 出现的次数
print(len("hello")) # 5 —— 字符串长度


s = "hello"
s2 = s.replace("h", "H555")
print(s)
print(s2) # hello H555llo —— replace 不改变原字符串，返回新字符串


#and 左边为假，右边不执行
#or 左边为真，右边不执行

name = ""
display = name or "游客"
print(display) # 游客