# Insurance Assistant (RAG Pipeline)

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

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Vector Store**: FAISS (Local)
- **AI / LLM**: Groq API (Llama-3 model)
- **Embeddings**: HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
- **Reranker**: HuggingFace `cross-encoder/ms-marco-MiniLM-L-6-v2`
- **PDF Extraction**: PyMuPDF (`fitz`)

### Frontend
- **Framework**: React + Vite
- **Styling**: Vanilla CSS (Custom tokens, variables, and responsive design)
- **Icons**: Lucide React

### Python Dependencies (`requirements.txt`)
Below is the list of Python packages installed in the backend and their definitions:
- **`fastapi`**: The core web framework used to build the high-performance APIs.
- **`uvicorn`**: An ASGI web server implementation used to run the FastAPI application.
- **`sqlalchemy`**: The SQL toolkit and Object-Relational Mapper (ORM) used to interact with the PostgreSQL database.
- **`alembic`**: A lightweight database migration tool for use with SQLAlchemy.
- **`psycopg2-binary`**: The PostgreSQL database adapter for Python.
- **`python-dotenv`**: Used to load environment variables from the `.env` file.
- **`pymupdf` (`fitz`)**: A high-performance PDF processing library used to extract text from the uploaded insurance policies.
- **`langchain`**: A framework for developing applications powered by language models (used here for general RAG utilities).
- **`langchain-text-splitters`**: Used to intelligently split extracted PDF text into overlapping semantic chunks.
- **`sentence-transformers`**: A HuggingFace library used to load the local ML embedding model and generate vector embeddings for chunks.
- **`faiss-cpu`**: Facebook AI Similarity Search, a library for efficient similarity search and clustering of dense vectors.
- **`transformers`**: HuggingFace library providing state-of-the-art machine learning models (used here as a dependency for the reranker).
- **`torch`**: PyTorch, the underlying deep learning tensor library required by HuggingFace models.
- **`python-multipart`**: Required by FastAPI to handle form data and parse file uploads (`UploadFile`).
- **`pydantic-settings`**: Used by FastAPI/Pydantic for robust environment and settings management.
- **`accelerate`**: A HuggingFace library that enables PyTorch models to run faster and with a smaller memory footprint.
- **`groq`**: The official Python client library for the Groq API, used to interface with the Llama 3 model at blazing speeds.

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
- Password: `*******`
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
*********
```

Start the FastAPI backend server:
```bash
uvicorn app.main:app --reload
```
*(Note: The first startup may take a few seconds as it downloads and caches the HuggingFace models into memory).*

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

---

## 📂 Project Structure

```text
insurance_rag/
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI route controllers (upload, chat)
│   │   ├── database/       # SQLAlchemy models, schemas, and CRUD operations
│   │   ├── rag/            # AI logic: chunking, embedding, FAISS, reranking, LLM
│   │   ├── services/       # Core business logic connecting API to DB and RAG
│   │   └── main.py         # FastAPI application entry point
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/     # React components (FileUpload, ChatBox)
    │   ├── App.jsx         # Main application layout
    │   ├── index.css       # Global design tokens and gradients
    │   └── main.jsx        # React DOM entry point
    ├── package.json        # Node dependencies and scripts
    └── vite.config.js      # Vite configuration and backend proxy setup
```
