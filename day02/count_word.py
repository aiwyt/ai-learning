#统计每个单词出现的次数,按次数从高到低打印。

text = "python is great python is easy python is powerful"
words = text.split()


count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

result = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word,num in result:
    print(f"{word}:{num}")