# 📘 Docu-Mentor Backend

This is the backend service for **Docu-Mentor**, powered by **FastAPI**, **LangChain**, and **HuggingFace models**.  
It provides a Retrieval-Augmented Generation (RAG) pipeline where questions are answered based on a local knowledge base (`knowledge.txt`).  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/docu-mentor.git
cd docu-mentor/backend
```

### 2️⃣ Create and configure `.env`
Inside `backend/.env` add:
```env
HUGGINGFACEHUB_API_TOKEN=your_hf_api_token_here
```

👉 Get a free token from [HuggingFace](https://huggingface.co/settings/tokens).

---

## 🚀 Run the Project

### ▶️ Run with Docker Compose
Build and start the container:
```bash
docker-compose up --build
```

Stop the container:
```bash
docker-compose down
```

### ▶️ Run Locally (without Docker)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
uvicorn src.server:app --reload
```

---

## 📡 API Endpoints

### 1️⃣ Health Check
```http
GET /ping
```
**Response:**
```json
{ "status": "ok" }
```

### 2️⃣ Ask Question
```http
POST /ask
```
**Body:**
```json
{
  "question": "What is Innovatech?"
}
```

**Response:**
```json
{
  "answer": "Innovatech is ..."
}
```

---

## 🛠️ Tech Stack
- **FastAPI** - API framework  
- **LangChain** - RAG pipeline  
- **HuggingFace** - Models & embeddings  
- **FAISS** - Vector storage  
- **Docker** - Containerization  

---
