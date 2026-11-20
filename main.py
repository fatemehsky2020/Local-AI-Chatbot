
from llama_cpp import Llama

model = Llama(
    model_path="./models/qwen2.5-1.5b-instruct-q3_k_m.gguf",
    n_ctx=1024,
    n_threads=2,
    verbose=False
)

print("Local AI 1.5B is ready!")
print("Type exit to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = model.create_chat_completion(
        messages=[
            {"role": "user", "content": question}
        ],
        max_tokens=150,
        temperature=0.7
    )

    print("\nAI:", response["choices"][0]["message"]["content"])
