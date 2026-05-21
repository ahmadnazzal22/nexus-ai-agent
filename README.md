# 🤖 NEXUS — Multi-Tool AI Agent

> An intelligent AI assistant that automatically selects the right tool based on the user’s request.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square\&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square\&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

* 🔍 **Web Search** — Retrieves detailed information from Wikipedia (English & Arabic)
* 🧮 **Smart Calculator** — Understands math operations written in natural language
* 🌤️ **Live Weather** — Displays temperature and humidity for any city
* 🎯 **Automatic Tool Selection** — The AI agent decides which tool to use automatically
* 🌐 **Bilingual Support** — Communicates in both English and Arabic
* 🎨 **Professional Dark UI** — Modern interface with smooth visual effects

---

## 🛠️ Tech Stack

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python 3.10+         | Core programming language |
| Flask                | Backend web server        |
| Groq API (LLaMA 3.3) | AI language model         |
| Wikipedia API        | Knowledge source          |
| wttr.in              | Free weather data         |
| HTML / CSS / JS      | Frontend interface        |

---

## 📁 Project Structure

```bash
nexus-ai-agent/
│
├── app.py              # Flask entry point
├── agent.py            # Agent logic & tool routing
├── tools/
│   ├── __init__.py
│   ├── search.py       # Wikipedia search tool
│   ├── calculator.py   # Calculator tool
│   └── weather.py      # Weather tool using wttr.in
├── templates/
│   └── index.html      # Frontend UI
├── .env                # API keys (not uploaded)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/nexus-ai-agent.git
cd nexus-ai-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Your Groq API Key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key from:

[Groq Console](https://console.groq.com?utm_source=chatgpt.com)

---

### 5. Run the Application

```bash
python app.py
```

Open your browser at:

```bash
http://127.0.0.1:5000
```

---

## 🧪 Example Queries

| User Question                   | Tool Used     |
| ------------------------------- | ------------- |
| Weather in Amman                | 🌤️ Weather   |
| What is 1500 * 12               | 🧮 Calculator |
| Who is Ibn Khaldun              | 🔍 Search     |
| What is artificial intelligence | 🔍 Search     |
| 25% of 800                      | 🧮 Calculator |
| Weather in London               | 🌤️ Weather   |

---

## 🧠 How the Agent Works

```text
User submits a question
        ↓
LLaMA 3.3 analyzes the request
        ↓
Selects the appropriate tool
(search / calculator / weather)
        ↓
Executes the tool and retrieves data
        ↓
LLaMA 3.3 formats a natural response
        ↓
Displays the result in the UI
```

---

## 📦 requirements.txt

```txt
flask
groq
requests
python-dotenv
```

---

## 👨‍💻 Developer

**AHMAD NAZZAL** — Python & AI Developer

GitHub:

[GitHub Profile](https://github.com/your-username?utm_source=chatgpt.com)

---

## 📄 License

MIT License — Free to use, modify, and distribute.
