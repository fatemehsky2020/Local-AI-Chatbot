
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"

save_path = "./models/qwen"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print("Model downloaded successfully!")
