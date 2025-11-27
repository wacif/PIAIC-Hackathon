# 🚀 Deployment Guide

## Step-by-Step Deployment Instructions

### Part 1: Deploy Docusaurus to GitHub Pages

#### 1. Enable GitHub Pages
1. Go to https://github.com/wacif/PIAIC-Hackathon/settings/pages
2. Under **Source**, select **GitHub Actions**
3. Save the settings

#### 2. Commit and Push Your Changes
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon

# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "feat: Complete project setup with Docusaurus and RAG chatbot

- Created fresh Docusaurus project with TypeScript
- Configured GitHub Pages deployment
- Implemented FastAPI backend with RAG endpoints
- Integrated Qdrant Cloud with FastEmbed
- Added OpenAI integration for responses
- Optimized dependencies (removed heavy PyTorch)
- Created comprehensive documentation"

# Push to GitHub
git push origin rag-chatbot-development
```

#### 3. Monitor Deployment
1. Go to https://github.com/wacif/PIAIC-Hackathon/actions
2. Watch the deployment workflow run
3. Once complete, visit: **https://wacif.github.io/PIAIC-Hackathon/**

#### 4. Merge to Main (Optional)
```bash
# Switch to main branch
git checkout main

# Merge the development branch
git merge rag-chatbot-development

# Push to main
git push origin main
```

### Part 2: Test Chatbot API Locally

#### 1. Set Up Environment
```bash
cd /home/wasi/Desktop/PIAIC-Hackathon/chatbot-api

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Configure Environment Variables
```bash
# Create .env file
cat > .env << 'EOF'
QDRANT_URL=https://5a552254-4803-497a-878d-712f2a402cf4.eu-central-1-0.aws.cloud.qdrant.io
QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzY1OTA2MTE1fQ.r-Jj2l1fUt4LKXS93rkI0N0Kc1_ytoG7SleGZIANtOM
OPENAI_API_KEY=your_openai_api_key_here
EOF

# Edit the file to add your OpenAI API key
nano .env  # or use your preferred editor
```

#### 3. Ingest Book Content
```bash
# Make sure you're in chatbot-api directory with venv activated
python ingestion.py
```

Expected output:
```
Starting data ingestion...
Found X markdown files
Created Y chunks from documents
✅ Successfully ingested Y chunks into Qdrant collection 'book_content'
```

#### 4. Start the API Server
```bash
uvicorn main:app --reload
```

The API will be available at: **http://localhost:8000**

#### 5. Test the API

Open your browser and visit:
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

Or use curl:
```bash
# Health check
curl http://localhost:8000/health

# Test query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is this documentation about?",
    "max_results": 5
  }'
```

### Part 3: Deploy API to Production (Optional)

#### Option A: Deploy to Render (Recommended)

1. **Create account** at https://render.com
2. **Create new Web Service**:
   - Connect your GitHub repository
   - Select `chatbot-api` as root directory
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. **Add Environment Variables**:
   - `QDRANT_URL`
   - `QDRANT_API_KEY`
   - `OPENAI_API_KEY`
4. **Deploy**!

#### Option B: Deploy to Railway

1. **Create account** at https://railway.app
2. **New Project** → Deploy from GitHub
3. **Select** your repository
4. **Add Environment Variables**
5. **Deploy**!

#### Option C: Deploy to Fly.io

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Launch app
cd chatbot-api
flyctl launch

# Set secrets
flyctl secrets set QDRANT_URL="your_url"
flyctl secrets set QDRANT_API_KEY="your_key"
flyctl secrets set OPENAI_API_KEY="your_key"

# Deploy
flyctl deploy
```

### Part 4: Connect Frontend to Backend

Once your API is deployed, update the Docusaurus site to use it:

1. Create a chatbot component in `my-book/src/components/Chatbot/`
2. Use the deployed API URL
3. Implement the chat UI
4. Add to Docusaurus pages

Example API call from frontend:
```javascript
const response = await fetch('https://your-api-url.com/query', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    question: userQuestion,
    max_results: 5
  })
});

const data = await response.json();
console.log(data.answer);
```

## 🔍 Troubleshooting

### Issue: GitHub Pages not deploying
- Check Actions tab for errors
- Ensure Pages is set to "GitHub Actions" source
- Verify workflow file is in `.github/workflows/`

### Issue: API can't connect to Qdrant
- Verify Qdrant URL and API key in `.env`
- Check if Qdrant cluster is active
- Test connection: `curl -H "api-key: YOUR_KEY" https://your-qdrant-url/collections`

### Issue: OpenAI API errors
- Verify API key is correct
- Check you have credits in your OpenAI account
- Ensure you're using a valid model name (gpt-4o-mini)

### Issue: No documents found during ingestion
- Check that `my-book/docs/` and `my-book/blog/` exist
- Verify markdown files have `.md` or `.mdx` extension
- Check the path in ingestion.py is correct

## 📊 Monitoring

### Check API Health
```bash
curl https://your-api-url.com/health
```

### Check Qdrant Collections
```bash
curl https://your-api-url.com/collections
```

### View API Logs
- **Render**: Dashboard → Logs tab
- **Railway**: Dashboard → Deployments → Logs
- **Fly.io**: `flyctl logs`

## 🎯 Next Steps After Deployment

1. ✅ Verify Docusaurus site is live
2. ✅ Test API endpoints
3. ✅ Ingest initial content
4. ⏳ Wait for hackathon topic announcement
5. ⏳ Create book content
6. ⏳ Re-run ingestion
7. ⏳ Build chatbot UI component
8. ⏳ Deploy API to production
9. ⏳ Final testing and polish

## 📞 Support

If you encounter issues:
1. Check the logs
2. Review error messages
3. Consult the README.md
4. Check Docusaurus docs: https://docusaurus.io/docs
5. Check FastAPI docs: https://fastapi.tiangolo.com/

---

**Good luck with your deployment! 🚀**

