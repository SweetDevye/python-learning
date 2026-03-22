# 🚀 AI Learning Journey（我的AI学习之路）

## 👩‍💻 About Me
网络工程大二在读  
正在从零开始系统学习 AI / Python / 大语言模型  

目标：
- 提升代码能力
- 掌握AI应用开发（Agent方向）
- 找到实习 / 考研提升

---

## 📚 学习记录

### ✅ Day1 - 基础任务
- Python基础语法
- 列表操作

### ✅ Day2 - 函数 & 任务管理
- 函数定义
- 简单任务管理系统

### ✅ Day3 - 字典
- 字典基本用法

### ✅ Day4 - 任务管理系统（升级版）
- 使用函数封装代码
- 提升代码结构

### ✅ Day5 - 任务系统（交互版）
- while循环
- 用户输入
- 添加/删除任务

### 🔥 Day6 - 第一个AI程序
- 使用 transformers
- 调用 GPT2 模型
- 实现文本生成

---

## 🤖 AI项目

### 🧠 文本生成（GPT2）
```python
from transformers import pipeline

chat = pipeline("text-generation", model="gpt2")

result = chat("我今天很开心，因为", max_new_tokens=50)

print(result[0]["generated_text"])
