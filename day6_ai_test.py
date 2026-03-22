from transformers import pipeline

chat = pipeline("text-generation", model="gpt2")

result = chat(
    "我今天很开心，因为",
    max_new_tokens=50
)

print(result[0]["generated_text"]) 