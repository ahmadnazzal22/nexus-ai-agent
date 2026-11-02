# 🤖 NEXUS — Multi-Tool AI Agent

An AI-powered assistant that understands user requests and automatically selects the appropriate tool to provide useful responses.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- 🔍 **Wikipedia Search** — Retrieves information from Wikipedia in English and Arabic.
- 🧮 **Natural Language Calculator** — Handles mathematical requests expressed in natural language.
- 🌤️ **Weather Information** — Retrieves weather information, including temperature and humidity, for a requested city.
- 🎯 **Automatic Tool Selection** — Determines which tool is appropriate for each user request.
- 🌐 **Bilingual Interaction** — Supports communication in English and Arabic.
- 🎨 **Dark User Interface** — Provides a modern dark-themed web interface.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Flask | Web application backend |
| Groq API (LLaMA 3.3) | Language model and request analysis |
| Wikipedia API | Information retrieval |
| wttr.in | Weather information |
| HTML, CSS, JavaScript | Frontend interface |

---

## 📁 Project Structure

```text
nexus-ai-agent/
│
├── app.py
├── agent.py
│
├── tools/
│   ├── __init__.py
│   ├── search.py
│   ├── calculator.py
│   └── weather.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── .gitignore
└── .env.example
```

> Make sure this structure matches the actual files in the repository before publishing it. Do not upload your real `.env` file or API keys.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadnazzal22/nexus-ai-agent.git
cd nexus-ai-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Keep your API key private. Never commit your `.env` file to GitHub.

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧪 Example Queries

| Example Request | Expected Tool |
|---|---|
| Weather in Amman | 🌤️ Weather |
| What is 1500 × 12? | 🧮 Calculator |
| Who is Ibn Khaldun? | 🔍 Wikipedia Search |
| What is artificial intelligence? | 🔍 Wikipedia Search |
| What is 25% of 800? | 🧮 Calculator |
| Weather in London | 🌤️ Weather |

---

## 🧠 How It Works

```text
User submits a question
          ↓
LLaMA 3.3 analyzes the request
          ↓
The agent selects the appropriate tool
          ↓
Search / Calculator / Weather
          ↓
The selected tool processes the request
          ↓
The AI generates a natural language response
          ↓
The result is displayed in the web interface
```

---

## 📦 Dependencies

The project dependencies are listed in `requirements.txt`.

Main packages:

```text
flask
groq
requests
python-dotenv
```

---

## 👨‍💻 Developer

**Ahmad Nazzal**

Python Developer | Exploring AI & Automation

- GitHub: [ahmadnazzal22](https://github.com/ahmadnazzal22)
- Project: [NEXUS AI Agent](https://github.com/ahmadnazzal22/nexus-ai-agent)

---

## 📄 License

This project is licensed under the MIT License.
