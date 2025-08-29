# Multi-Role AI Assistant

This project is a **multi-role AI assistant** that generates responses from different personas such as **Analyst**, **CEO**, **Engineer**, **Designer**, and **Marketing Specialist**.  
It is built using **FastAPI** with async OpenAI API calls.

---

## 🚀 Features
1. Role-specific responses (Analyst, CEO, Engineer, Designer, Marketing).
2. Asynchronous API calls for better performance.
3. Built with **FastAPI** for high-speed API interaction.
4. Easily extendable to include more roles.

---

## 📂 Project Structure
````text
    .
    ├── backend
    ├── frontend
    ├── requirements.txt # Python dependencies
    └── README.md # Documentation
````
---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-role-ai-assistant.git
cd multi-role-ai-assistant
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
````bash
pip install -r requirements.txt
````

### 4. Set Environment Variables

Create a .env file and add your OpenAI API key:
````bash
OPENAI_API_KEY=your_api_key_here
````

### ▶️ Running the Application

Start the FastAPI server:
````bash
uvicorn app:app --reload
````
API will be available at:
````bash
http://127.0.0.1:8000
````