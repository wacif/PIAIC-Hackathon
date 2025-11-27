# 🚀 Quick Start Guide

## ⚡ Get Started in 5 Minutes

### Step 1: Review What's Been Done ✅

Everything is ready! Check these files:
- ✅ `README.md` - Full documentation
- ✅ `PROJECT_SUMMARY.md` - What's complete
- ✅ `DEPLOYMENT_GUIDE.md` - How to deploy
- ✅ `ARCHITECTURE.md` - System design

### Step 2: Set Up API Environment 🔧

```bash
# Navigate to API directory
cd /home/wasi/Desktop/PIAIC-Hackathon/chatbot-api

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies (fast - no PyTorch!)
pip install -r requirements.txt
```

### Step 3: Configure API Keys 🔑

```bash
# Create .env file
cat > .env << 'ENVEOF'
QDRANT_URL=https://5a552254-4803-497a-878d-712f2a402cf4.eu-central-1-0.aws.cloud.qdrant.io
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzY1OTA2MTE1fQ.r-Jj2l1fUt4LKXS93rkI0N0Kc1_ytoG7SleGZIANtOM
OPENAI_API_KEY=your_openai_key_here
ENVEOF

# Edit to add your OpenAI key
nano .env
```

### Step 4: Test the System 🧪

```bash
# Terminal 1: Start API
cd /home/wasi/Desktop/PIAIC-Hackathon/chatbot-api
source venv/bin/activate
uvicorn main:app --reload

# Terminal 2: Test Docusaurus
cd /home/wasi/Desktop/PIAIC-Hackathon/my-book
npm start

# Terminal 3: Run ingestion
cd /home/wasi/Desktop/PIAIC-Hackathon/chatbot-api
source venv/bin/activate
python ingestion.py
```

### Step 5: Deploy to GitHub Pages 🌐

```bash
cd /home/wasi/Desktop/PIAIC-Hackathon

# Stage all changes
git add .

# Commit
git commit -m "feat: Complete Docusaurus and RAG chatbot setup

- Created fresh Docusaurus project with TypeScript
- Implemented FastAPI backend with RAG endpoints
- Integrated Qdrant Cloud with FastEmbed
- Added comprehensive documentation
- Optimized dependencies (removed PyTorch)"

# Push to GitHub
git push origin rag-chatbot-development
```

### Step 6: Enable GitHub Pages 📄

1. Go to: https://github.com/wacif/PIAIC-Hackathon/settings/pages
2. Under **Source**, select **GitHub Actions**
3. Save and wait for deployment
4. Visit: https://wacif.github.io/PIAIC-Hackathon/

---

## 🎯 What to Do After Topic Announcement

### 1. Create Book Content
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon/my-book/docs

# Create your book chapters
nano chapter1.md
nano chapter2.md
# etc...
```

### 2. Re-ingest Content
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon/chatbot-api
source venv/bin/activate
python ingestion.py
```

### 3. Test Chatbot
```bash
# Visit http://localhost:8000/docs
# Try the /query endpoint with your content
```

### 4. Build Frontend Component
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon/my-book/src/components
mkdir Chatbot
# Create React component for chat UI
```

---

## 📊 System Status Check

### Check API Health
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "qdrant": "connected",
  "collection_exists": true,
  "openai_configured": true
}
```

### Check Docusaurus Build
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon/my-book
npm run build
```

Expected: Build completes in ~45 seconds

### Check Qdrant Connection
```bash
curl http://localhost:8000/collections
```

Expected:
```json
{
  "collections": ["book_content"]
}
```

---

## 🆘 Troubleshooting

### API won't start
```bash
# Check if port is in use
lsof -i :8000

# Try different port
uvicorn main:app --reload --port 8001
```

### Ingestion fails
```bash
# Check paths
ls ../my-book/docs
ls ../my-book/blog

# Check .env file
cat .env
```

### Build fails
```bash
# Clear cache
cd my-book
rm -rf .docusaurus build
npm run build
```

---

## 📞 Quick Links

- **API Docs**: http://localhost:8000/docs
- **Docusaurus**: http://localhost:3000
- **GitHub Repo**: https://github.com/wacif/PIAIC-Hackathon
- **Deployed Site**: https://wacif.github.io/PIAIC-Hackathon/

---

## ✅ Pre-Deployment Checklist

- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] .env file configured with OpenAI key
- [ ] API starts without errors
- [ ] Docusaurus builds successfully
- [ ] Ingestion runs successfully
- [ ] All changes committed
- [ ] Pushed to GitHub
- [ ] GitHub Pages enabled

---

**You're all set! Time to create amazing content! 🎉**
