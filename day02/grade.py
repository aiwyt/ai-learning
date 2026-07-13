"""
•循环让用户输入学生姓名和成绩,输入空名字结束
•全部输入完后,打印:最高分、最低分、平均分(保留 2 位小数)
•打印每人的等第:90+ 优秀 / 80+ 良好 / 60+ 及格 / 其余不及格
"""

scores = []

while True:
    name = input("请输入姓名(直接回车结束):")
    if not name:
        break

    score_str = input("请输入成绩:")
    if not score_str.isdigit():
        print("成绩必须是数字,请重新输入这位同学")
        continue

    score = int(score_str)

    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"

    print(f"{name} 的等级是 {grade}")
    scores.append(score)

if not scores:
    print("没有输入任何成绩")
else:
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    print(f"平均分: {sum(scores) / len(scores):.2f}")