# AI 应用开发学习记录

从零开始学习 AI 应用开发的过程记录,包含每日学习笔记与练习代码。

## 学习目标

系统掌握 AI 应用开发所需的核心技能,产出可展示的项目作品。

- Python 基础与工程化
- SQL 与数据处理
- FastAPI 后端开发
- LLM 应用开发(Prompt 工程、RAG、Agent)

## 进度

- [x] **Day 1** — 开发环境搭建:venv / VS Code / Git / .env 管理
- [x] **Day 2** — Python 基础:变量、类型转换、字符串、条件、循环、字典
- [ ] **Day 3** — 待补充

## 目录结构

```
ai-learning/
├── day02/
│   ├── 01_basic.py       # 变量与数据类型
│   ├── 02_convert.py     # 类型转换
│   ├── 03_string.py      # 字符串操作
│   ├── 04_if.py          # 条件判断
│   ├── 05_if.py          # 条件判断进阶
│   ├── 06_loop.py        # for / while 循环
│   ├── guess.py          # 练习:猜数字游戏
│   ├── count_word.py     # 练习:词频统计
│   └── grade.py          # 练习:学生成绩管理
├── .env.example          # 环境变量模板
├── .gitignore
├── requirements.txt
└── README.md
```

## 练习说明

| 文件 | 说明 | 涉及知识点 |
|---|---|---|
| `guess.py` | 1–100 猜数字游戏,支持退出与非法输入处理 | while 循环、break、类型转换 |
| `count_word.py` | 统计文本词频并按出现次数降序输出 | 字典、sorted、lambda |
| `grade.py` | 录入学生成绩,输出等第与最高/最低/平均分 | 列表、条件分支、格式化输出 |

## 环境

- Python 3.12
- Windows + PowerShell
- 依赖管理:`venv` + `requirements.txt`

## 快速开始

```bash
# 克隆项目
git clone https://github.com/aiwyt/ai-learning.git
cd ai-learning

# 创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
```