# RAG-System-for-Hasanah-Mart
# Hasanah Mart AI Assistant — Project Flow

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

# Phase 2 — Knowledge Base Structuring

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

# Phase 3 — Core RAG Backend Development

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

# Phase 4 — Frontend Experimentation

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

# Phase 5 — Production Deployment

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

# Phase 6 — WhatsApp Integration

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

# Phase 7 — Multilingual Conversational Testing

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

# Phase 8 — Persistence & Analytics Layer

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

# Phase 9 — Internal Production Validation

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

# Phase 10 — Reverse Engineering & Optimization Phase (Current Phase)

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
“building with AI assistance”
to
“deeply understanding and engineering production-grade AI systems.”