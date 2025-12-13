# 🧠 Math Wisdom Bot — Math Solver + Wikipedia Search (Groq + LangChain)

**Math Wisdom Bot** is an intelligent Streamlit application that can:

✔ Solve **math problems step-by-step** using Groq's Llama 3.1 models  
✔ Perform **Wikipedia search & data lookup**  
✔ Chat with users while maintaining conversation history  
✔ Use modern LangChain components (LCEL, Tools, Prompts)

This bot is perfect for students, learners, and anyone who needs instant math help or factual data via Wikipedia.

---

## 🚀 Features

### 🔢 **Math Problem Solver**
- Uses LangChain prompt chaining (LCEL)
- Provides detailed step-by-step solutions
- Handles arithmetic, algebra, word problems, and logic questions

### 📚 **Wikipedia Search Mode**
- Uses LangChain’s modern `WikipediaQueryRun` tool  
- Fetches factual data instantly  
- Supports any topic: science, history, people, places, etc.

### 🤖 **Groq Llama-3 Backend**
- Powered by **Llama-3.1-8B-Instant**
- Fast reasoning & high-quality responses
- Uses Groq API for speed and efficiency

### 💬 **Chat Interface**
- Maintains session-based conversation history
- Built fully in Streamlit

---

## 📁 Project Structure

math-wisdom-bot/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

yaml
Copy code

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Shehjad2019/math-wisdom-bot.git
cd math-wisdom-bot
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add Groq API Key
Create .env file:

bash
Copy code
cp .env.example .env
Then open .env:

ini
Copy code
GROQ_API_KEY=your_groq_api_key_here
▶️ Run the App
bash
Copy code
streamlit run app.py
🧠 How It Works
Math Solver Mode
User enters a problem

Prompt instructs model: "Solve step-by-step with reasoning"

LLM processes via ChatGroq (Llama-3)

Output parsed using StrOutputParser

Returned in clean step-by-step explanation

Wikipedia Search Mode
Uses WikipediaQueryRun tool

Fetches relevant info using WikipediaAPIWrapper

Returns summarized results directly

🔑 Environment Variables
ini
Copy code
GROQ_API_KEY=your_groq_api_key_here
👤 Author
Shehjad Patel
GitHub: https://github.com/Shehjad2019

⭐ Support the Project
If you like this bot, please ⭐ the repo:
https://github.com/Shehjad2019/math-wisdom-bot