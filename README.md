# Hasanah Mart AI Assistant

Production-oriented multilingual RAG-powered AI assistant built with FastAPI, OpenAI, FAISS, PostgreSQL, WhatsApp Cloud API, and Streamlit.

This project was built to explore real-world AI engineering workflows by creating an end-to-end conversational commerce system around an actual business use case.

---

# Live Demo

🌐 Streamlit Frontend
https://hasanah-mart-streamlit.onrender.com

📦 GitHub Repository
https://github.com/mridul162/RAG-System-for-Hasanah-Mart

---

# Core Features

✅ Retrieval-Augmented Generation (RAG) pipeline
✅ Semantic search using FAISS vector database
✅ OpenAI embedding integration
✅ Multilingual conversational support
✅ Bengali + English + Banglish query handling
✅ WhatsApp Cloud API integration
✅ Real-time AI-powered customer interaction
✅ PostgreSQL conversation persistence
✅ Dashboard analytics APIs
✅ Streamlit testing frontend
✅ FastAPI backend architecture
✅ Dockerized deployment workflow
✅ Structured logging and monitoring foundations

---

# System Architecture

```text
User Query (WhatsApp / Streamlit)
    ↓
FastAPI Endpoint (/chat/ask or Webhook)
    ↓
Pydantic Request Validation
    ↓
Dependency Injection
    ↓
RAG Service Layer
    ↓
Query Embedding Generation
    ↓
FAISS Semantic Retrieval
    ↓
Relevant Chunk Selection
    ↓
Prompt Construction
    ↓
OpenAI Response Generation
    ↓
Structured API Response
    ↓
WhatsApp / Streamlit Response Delivery
    ↓
Conversation Persistence (PostgreSQL)
    ↓
Dashboard Analytics APIs
    ↓
Logging + Latency Tracking
    ↓
Dockerized Cloud Deployment
```

---

# Tech Stack

| Layer      | Technologies           |
| ---------- | ---------------------- |
| Backend    | FastAPI, Python        |
| AI/LLM     | OpenAI API             |
| Retrieval  | FAISS                  |
| Embeddings | text-embedding-3-small |
| Database   | PostgreSQL             |
| ORM        | SQLAlchemy             |
| Frontend   | Streamlit              |
| Messaging  | WhatsApp Cloud API     |
| Deployment | Docker, Render         |
| Validation | Pydantic               |
| Logging    | Python Logging         |

---

# Project Structure

```text
RAG-System-for-Hasanah-Mart/
│
├── api/
│   ├── core/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── db/
│   └── dependencies/
│
├── data/
│
├── frontend/
│
├── notebooks/
│
├── vector_db/
│
├── logs/
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Chat Endpoint

```text
POST /chat/ask
```

Used for:

* Streamlit frontend
* direct API interaction

---

## WhatsApp Webhook

```text
GET /webhooks/whatsapp
POST /webhooks/whatsapp
```

Used for:

* webhook verification
* incoming WhatsApp messages

---

## Dashboard APIs

```text
GET /dashboard/conversations
GET /dashboard/conversations/{id}
GET /dashboard/analytics
```

Used for:

* monitoring
* analytics
* conversation inspection

---

# Installation

## Clone Repository

```bash
git clone https://github.com/mridul162/RAG-System-for-Hasanah-Mart.git

cd RAG-System-for-Hasanah-Mart
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key

WHATSAPP_VERIFY_TOKEN=your_verify_token

WHATSAPP_ACCESS_TOKEN=your_whatsapp_access_token

WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id

DATABASE_URL=your_postgresql_database_url
```

---

# Running Backend

```bash
uvicorn api.app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# Docker Deployment

## Build Image

```bash
docker build -t hasanah-mart-ai .
```

---

## Run Container

```bash
docker run -p 8000:8000 hasanah-mart-ai
```

---

# Completed Architecture

✅ Modular RAG pipeline
✅ Structured knowledge base
✅ Document loading system
✅ Text chunking pipeline
✅ OpenAI embedding integration
✅ FAISS vector database
✅ Semantic retrieval system
✅ Prompt builder
✅ LLM response generation
✅ Multilingual query handling
✅ WhatsApp Cloud API integration
✅ Webhook event handling
✅ Streamlit testing frontend
✅ PostgreSQL conversation persistence
✅ Dashboard analytics APIs
✅ FastAPI backend
✅ Schema validation
✅ Dependency injection
✅ Lifecycle-managed services
✅ Centralized configuration
✅ Structured logging
✅ Rotating log persistence
✅ Dockerized deployment workflow
✅ Production-oriented backend architecture
✅ Internal production testing pipeline

---

# Project Flow & Learning Journey

## Phase 1 — Problem Identification & Goal Setting

### Objective

Build a real-world AI assistant around an actual business use case instead of staying inside tutorials and notebooks.

### Core Goals

* Learn production-oriented AI engineering
* Understand end-to-end RAG pipeline development
* Experiment with AI-assisted engineering workflows
* Build multilingual conversational commerce capability
* Deploy a working real-world system

---

## Phase 2 — Knowledge Base Structuring

### Tasks

* Organized Hasanah Mart product data
* Created structured markdown-based product knowledge base
* Defined product categories and information hierarchy
* Planned chunk-friendly documentation structure

### Learning Focus

* Data organization
* Knowledge representation
* RAG-friendly content structuring

---

## Phase 3 — Core RAG Backend Development

### Technologies

* FastAPI
* OpenAI API
* FAISS
* Python

### Tasks

* Built embedding pipeline
* Generated vector embeddings
* Created FAISS vector index
* Implemented semantic retrieval
* Built prompt construction pipeline
* Integrated OpenAI chat completion API
* Created `/chat/ask` endpoint

### Learning Focus

* Embeddings
* Vector similarity search
* Context injection
* Prompt engineering
* Backend API design

---

## Phase 4 — Frontend Experimentation

### Technology

* Streamlit

### Tasks

* Built basic testing interface
* Connected frontend to FastAPI backend
* Enabled multilingual query testing
* Tested Bengali, English, and Banglish interactions

### Learning Focus

* Frontend-backend communication
* API integration
* Rapid AI interface prototyping

---

## Phase 5 — Production Deployment

### Technologies

* Docker
* Render

### Tasks

* Dockerized backend service
* Configured environment variables
* Solved deployment and dependency issues
* Deployed FastAPI backend publicly
* Deployed Streamlit frontend separately

### Learning Focus

* Production deployment
* Environment management
* Dependency optimization
* Cloud hosting

---

## Phase 6 — WhatsApp Integration

### Technologies

* Meta Developer Platform
* WhatsApp Cloud API
* Webhooks

### Tasks

* Created Meta developer app
* Configured WhatsApp Cloud API
* Implemented webhook verification
* Built incoming message handler
* Implemented outgoing message delivery
* Connected WhatsApp flow with RAG backend

### Learning Focus

* Webhook architecture
* Real-time messaging systems
* External API integration
* Conversational orchestration

---

## Phase 7 — Multilingual Conversational Testing

### Tasks

* Tested Bengali interactions
* Tested Banglish interactions
* Tested product-related conversations
* Evaluated retrieval quality
* Verified contextual responses

### Learning Focus

* Multilingual retrieval behavior
* Context quality
* Conversational AI evaluation
* User-side testing

---

## Phase 8 — Persistence & Analytics Layer

### Technologies

* PostgreSQL
* SQLAlchemy

### Tasks

* Integrated PostgreSQL database
* Stored conversation history
* Created CRUD operations
* Built analytics endpoints
* Built dashboard APIs

### Learning Focus

* Database integration
* Operational AI systems
* Conversation persistence
* Observability foundations

---

## Phase 9 — Internal Production Validation

### Tasks

* Enabled real user testing
* Tested through WhatsApp interface
* Collected conversational logs
* Evaluated practical usability
* Monitored system stability

### Learning Focus

* Real-world testing
* Operational reliability
* User interaction flow
* Practical AI deployment

---

## Phase 10 — Reverse Engineering & Optimization Phase (Current Phase)

### Current Focus

Deeply understanding and optimizing the system instead of only extending features.

### Planned Areas

* RAG optimization
* Retrieval quality improvement
* Better chunking strategies
* Backend architecture refinement
* Observability and monitoring
* Scalability improvements
* Async processing
* AI system design understanding

### Long-Term Goal

Transition from:

```text
building with AI assistance
```

to:

```text
deeply understanding and engineering production-grade AI systems
```

---

# Future Improvements

* Hybrid retrieval
* pgvector integration
* Redis caching
* Async background workers
* Next.js dashboard frontend
* Human escalation system
* Conversation memory
* Retrieval observability
* Evaluation pipelines
* AI analytics dashboard
* Scalable queue-based processing

---

# Disclaimer

This project is currently in prototype and experimentation phase and is being used primarily as a learning platform for applied AI engineering and production-oriented RAG system development.

---

# License

MIT License