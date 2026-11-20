# Local AI Chatbot – Qwen 2.5 (1.5B)

A lightweight local AI chatbot powered by **Qwen2.5-1.5B-Instruct**, running entirely on a local machine using `llama.cpp` through the `llama-cpp-python` library.

## Project Overview

This project demonstrates how to run a Large Language Model (LLM) locally without relying on cloud-based AI APIs.

The model contains **1.5 billion parameters** and uses the GGUF Q3_K_M quantized format to reduce memory requirements.

## Technologies Used

- Python 3.10
- Qwen2.5-1.5B-Instruct
- llama.cpp
- llama-cpp-python
- GGUF Quantization

## Project Structure

```text
Local-AI/
│
├── models/
│   └── qwen2.5-1.5b-instruct-q3_k_m.gguf
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone or download this repository.

2. Create and activate a virtual environment:

```bash
python -m venv cpu_env
```

3. Install the required package:

```bash
pip install llama-cpp-python
```

For Windows CPU installations, use:

```bash
python -m pip install --only-binary=:all: llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

4. Download the Qwen2.5-1.5B-Instruct GGUF model and place it inside the `models` folder.

## Run the Project

```bash
python main.py
```

After loading, you can enter questions and receive AI-generated responses directly in the terminal.

Type `exit` to close the chatbot.

## Features

- Runs locally on CPU
- Supports Persian conversations
- No cloud API required
- Uses a 1.5-billion-parameter language model
- Reduced memory usage through quantization
- Maintains conversation history during the session

## Hardware

Designed to run on CPU-based systems. Performance depends on available RAM and processor speed.

## Future Improvements

- Develop a graphical user interface
- Add a web-based chat interface
- Improve conversation memory
- Optimize CPU performance

## License

This project uses the Qwen2.5 model. Please refer to the original model license and terms of use.

---

**Developed as a Local AI Model Project.**
