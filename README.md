# PIAIC Hackathon: AI-Powered Interactive Book with RAG Chatbot

An intelligent book platform built with Docusaurus and a RAG (Retrieval-Augmented Generation) chatbot powered by FastAPI, Qdrant, and OpenAI.

## 🚀 Project Overview

This project combines a beautiful documentation site with an AI-powered chatbot that can answer questions about the book content using RAG technology.

### Features

- 📚 **Interactive Book**: Built with Docusaurus for a modern reading experience
- 🤖 **RAG Chatbot**: AI assistant that answers questions based on book content
- 🔍 **Smart Search**: Vector-based semantic search using Qdrant
- 💬 **Context-Aware**: Ask questions about specific text selections
- ⚡ **Fast & Lightweight**: Uses Qdrant FastEmbed for efficient embeddings
- 🎨 **Beautiful UI**: Modern, responsive design with dark mode support

## 📁 Project Structure

```
PIAIC-Hackathon/
├── my-book/                    # Docusaurus source files
│   ├── docs/                   # Book content (markdown)
│   ├── blog/                   # Blog posts
│   ├── src/                    # Custom React components
│   └── docusaurus.config.ts   # Docusaurus configuration
├── chatbot-api/                # FastAPI backend
│   ├── main.py                 # API endpoints
│   ├── ingestion.py            # Data ingestion script
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # Environment variables (not in git)
└── .github/workflows/          # GitHub Actions for deployment
```

## 🛠️ Setup Instructions

### Prerequisites

- Node.js 20+ and npm
- Python 3.12+
- Qdrant Cloud account (free tier)
- OpenAI API key

### 1. Clone the Repository

```bash
git clone https://github.com/wacif/PIAIC-Hackathon.git
cd PIAIC-Hackathon
```

### 2. Setup Docusaurus Book

```bash
cd my-book
npm install
npm start  # Runs on http://localhost:3000
```

### 3. Setup Chatbot API

```bash
cd chatbot-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cat > .env << EOF
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
OPENAI_API_KEY=your_openai_api_key
EOF
```

### 4. Ingest Book Content

```bash
# Make sure you're in the chatbot-api directory with venv activated
python ingestion.py
```

### 5. Run the API

```bash
uvicorn main:app --reload  # Runs on http://localhost:8000
```

## 🌐 Deployment

### GitHub Pages (Docusaurus)

The book is automatically deployed to GitHub Pages when you push to the `main` or `rag-chatbot-development` branch.

**Live URL**: https://wacif.github.io/PIAIC-Hackathon/

### API Deployment

The FastAPI backend can be deployed to:
- **Render** (recommended for free tier)
- **Railway**
- **Fly.io**
- **AWS Lambda** (with Mangum)

## 📚 API Endpoints

### Health Check
```bash
GET /health
```

### Query Book Content
```bash
POST /query
Content-Type: application/json

{
  "question": "What is this book about?",
  "max_results": 5
}
```

### Query Selected Text
```bash
POST /query-selection
Content-Type: application/json

{
  "question": "Explain this concept",
  "selected_text": "The text user selected from the book"
}
```

### List Collections
```bash
GET /collections
```

## 🔧 Technology Stack

### Frontend (Book)
- **Docusaurus 3.9**: Modern static site generator
- **React**: UI components
- **TypeScript**: Type safety
- **MDX**: Enhanced markdown with React components

### Backend (Chatbot)
- **FastAPI**: Modern Python web framework
- **Qdrant**: Vector database for semantic search
- **FastEmbed**: Lightweight embedding model
- **OpenAI GPT-4**: Language model for responses
- **Pydantic**: Data validation

## 📝 Development Workflow

1. **Add Content**: Create/edit markdown files in `my-book/docs/` or `my-book/blog/`
2. **Test Locally**: Run `npm start` in `my-book/` directory
3. **Ingest Content**: Run `python ingestion.py` to update the vector database
4. **Test API**: Use the API endpoints to verify chatbot responses
5. **Deploy**: Push to GitHub for automatic deployment

## 🎯 Next Steps

- [ ] Add chatbot UI component to Docusaurus
- [ ] Implement text selection feature in frontend
- [ ] Add authentication for API
- [ ] Implement rate limiting
- [ ] Add analytics and monitoring
- [ ] Create custom book content based on hackathon topic

## 🤝 Contributing

This is a hackathon project. Feel free to fork and experiment!

## 📄 License

MIT License - feel free to use this project as a template for your own documentation sites with AI chatbots.

## 🙏 Acknowledgments

- PIAIC for organizing the hackathon
- Docusaurus team for the amazing documentation framework
- Qdrant for the vector database
- OpenAI for the language models

---

**Built with ❤️ for PIAIC Hackathon**

