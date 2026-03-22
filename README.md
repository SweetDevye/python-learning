# 🚀 AI Learning Journey（我的AI学习之路）

## 👩‍💻 About Me
华南师范大学计算机学院大二在读  
正在从零开始系统学习 AI / Python / 大语言模型  

👉 当前重点：AI应用开发（Agent方向）

目标：
- 提升代码能力
- 掌握AI应用开发
- 找到实习 / 提升学历（考研）

---

## 🤖 核心项目（重点）

### 🧠 AI文本生成系统（基于GPT2）
- 使用 HuggingFace Transformers
- 本地加载并运行 GPT2 模型
- 实现中文输入 → 自动生成文本
- 完成从“环境搭建 → 模型调用 → 推理”的完整流程

📌 示例代码：
```python
from transformers import pipeline

chat = pipeline("text-generation", model="gpt2")

result = chat(
    "我今天很开心，因为",
    max_new_tokens=50
)

print(result[0]["generated_text"])
