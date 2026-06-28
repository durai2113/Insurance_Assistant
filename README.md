# 🛡️ Insurance Assistant (RAG Pipeline)

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Insurance Assistant is a full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload PDF insurance policies and interactively chat with an AI assistant to extract specific information, clauses, and summaries from the document.

The application uses **FastAPI** for a high-performance backend, **PostgreSQL** for storing chat histories, **FAISS** for local vector retrieval, and **Groq** for blazing-fast LLM inference. The frontend is a modern, responsive **React + Vite** application featuring a premium "Glassmorphism" UI with a beautiful Rose/Crimson color palette.

---

## 🚀 Features

- **PDF Ingestion & Processing**: Upload large insurance policies. The backend extracts text, splits it into semantic chunks, and calculates vector embeddings.
- **Pre-loaded ML Models**: The backend pre-loads HuggingFace embedding and reranking models at startup, ensuring instant, zero-delay document processing.
- **RAG Chat Interface**: Ask complex questions about the uploaded policy.
- **Hybrid Retrieval**: Uses local FAISS vector search combined with Cross-Encoder reranking for highly accurate context retrieval.
- **Modern Premium UI**: Built with pure Vanilla CSS, utilizing glassmorphism, dynamic gradients, and smooth micro-animations.

---

## 🛠️ Technology Stack

### Frontend
- **Framework**: React + Vite
- **Styling**: Vanilla CSS (Custom tokens, variables, and responsive design)
- **Icons**: Lucide React

### Backend Python Dependencies (`requirements.txt`)
The backend is highly optimized and stripped of unused bloat. Below are the core Python packages utilized:
- **`fastapi`**: The core web framework used to build the high-performance APIs.
- **`uvicorn`**: An ASGI web server implementation used to run the FastAPI application.
- **`sqlalchemy`**: The SQL toolkit and Object-Relational Mapper (ORM) used to interact with the PostgreSQL database.
- **`psycopg2-binary`**: The PostgreSQL database adapter for Python.
- **`python-dotenv`**: Used to load environment variables from the `.env` file.
- **`pymupdf` (`fitz`)**: A high-performance PDF processing library used to extract text from the uploaded insurance policies.
- **`langchain-text-splitters`**: Used to intelligently split extracted PDF text into overlapping semantic chunks.
- **`sentence-transformers`**: A HuggingFace library used to load the local ML embedding model and generate vector embeddings for chunks.
- **`faiss-cpu`**: Facebook AI Similarity Search, a library for efficient similarity search and clustering of dense vectors.
- **`python-multipart`**: Required by FastAPI to handle form data and parse file uploads (`UploadFile`).
- **`groq`**: The official Python client library for the Groq API, used to interface with the Llama 3 model at blazing speeds.

*(Note: Heavy ML dependencies like `torch` and `transformers` are handled implicitly by `sentence-transformers` to avoid version conflicts).*

---

## 📂 Project Architecture

```text
insurance_rag/
├── backend/
│   ├── app/
│   │   ├── api/            # API Routes: FastAPI controllers for file uploads and chat queries
│   │   ├── database/       # Database Layer: PostgreSQL connection, schemas, and SQLAlchemy ORM
│   │   ├── rag/            # AI Engine (RAG): Logic for chunking, HuggingFace embeddings, FAISS, and Llama 3
│   │   ├── services/       # Business Logic: Service layer orchestrating RAG and database operations
│   │   ├── utils/          # Utilities: Configuration management
│   │   └── main.py         # Backend Core: FastAPI entry point and dependencies
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/     # UI Components: Reusable React components for FileUpload and ChatBox
    │   ├── assets/         # Static Assets: Application images and graphics
    │   ├── App.jsx         # React App: Main application layout and state
    │   ├── index.css       # Styles: Global CSS tokens and premium Glassmorphism gradients
    │   └── main.jsx        # React App: DOM rendering entry point
    ├── package.json        # Frontend Core: Node dependencies
    └── vite.config.js      # Frontend Core: Vite bundler setup and backend API proxy routing
```

---

## ⚙️ Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL server running locally

### 1. Database Setup
Ensure you have a PostgreSQL database created. By default, the application looks for:
- Database Name: `insurance_db`
- User: `postgres`
- Password: `*******` *(replace in your local .env)*
- Port: `5432`

### 2. Backend Setup
Navigate to the backend directory:
```bash
cd backend
```

Create a virtual environment and activate it:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\Activate.ps1
# On Mac/Linux:
source .venv/bin/activate
```

Install the Python dependencies:
```bash
pip install -r requirements.txt
```

Ensure your `.env` file is properly configured with your keys:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/insurance_db 
GROQ_MODEL=llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CROSS_ENCODER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
```

Start the FastAPI backend server:
```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup
Open a new terminal window and navigate to the frontend directory:
```bash
cd frontend
```

Install the Node dependencies:
```bash
npm install
```

Start the Vite development server:
```bash
npm run dev
```

### 4. Usage
- Open your browser and navigate to `http://localhost:5173`.
- Upload a valid PDF document.
- Once processed, type your question in the chatbox to query the AI about the document's contents!
