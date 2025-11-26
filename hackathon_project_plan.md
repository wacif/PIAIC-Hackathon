**Hackathon Project Plan: AI/Spec-Driven Book with Integrated RAG Chatbot**

**1. Project Setup and Initial Book Creation (Docusaurus)**
    *   **Goal**: Establish the basic Docusaurus project structure and get a minimal book deployed.
    *   **Steps**:
        1.  **Initialize Docusaurus Project**: Create a new Docusaurus site.
        2.  **Configure Docusaurus**: Set up basic navigation, sidebar, and general site metadata.
        3.  **Create Placeholder Content**: Add a few markdown files for initial book content (since the actual title and content will be provided later).
        4.  **Local Development**: Verify Docusaurus runs correctly locally.
        5.  **GitHub Repository Setup**: Initialize a Git repository and push the Docusaurus project to GitHub.
        6.  **GitHub Pages Deployment**: Configure GitHub Pages for automatic deployment of the Docusaurus site.

**2. RAG Chatbot Core Development**
    *   **Goal**: Develop the backend for the RAG chatbot using FastAPI and Qdrant, and integrate with OpenAI Agents/ChatKit.
    *   **Steps**:
        1.  **FastAPI Project Setup**: Create a new FastAPI application.
        2.  **Qdrant Cloud Setup**: Obtain a free-tier account for Qdrant Cloud and set up a new collection for vector storage.
        3.  **Data Ingestion (Book Content)**:
            *   Develop a script to parse the Docusaurus markdown files.
            *   Split the book content into smaller, manageable chunks.
            *   Generate embeddings for these chunks using an appropriate embedding model.
            *   Store the chunks and their embeddings in the Qdrant vector database.
        4.  **OpenAI Agents/ChatKit Integration**:
            *   Set up the OpenAI Agents/ChatKit SDK within the FastAPI application.
            *   Define tools for the agent to interact with the Qdrant database (e.g., a retrieval tool to search for relevant book content).
        5.  **RAG Logic Implementation**:
            *   Implement the core RAG flow:
                *   Receive user query.
                *   Generate embedding for the query.
                *   Perform a similarity search in Qdrant to retrieve relevant book content.
                *   Pass the retrieved context along with the user query to the OpenAI agent for generating a response.
        6.  **API Endpoints**: Create FastAPI endpoints for:
            *   Receiving user questions.
            *   Handling text selection from the book (to answer questions based only on selected text).

**3. Integrating Chatbot into Docusaurus Book**
    *   **Goal**: Embed the developed RAG chatbot seamlessly into the Docusaurus site.
    *   **Steps**:
        1.  **Frontend Component Development**: Create a React component (or similar) within Docusaurus to serve as the chatbot UI.
        2.  **API Integration**: The frontend component will interact with the FastAPI backend to send questions and receive responses.
        3.  **Text Selection Feature**: Implement functionality to allow users to select text within the Docusaurus book and send it to the chatbot as context for their questions.
        4.  **Styling and Responsiveness**: Ensure the chatbot UI is well-integrated visually and responsive.

**4. Bonus: Claude Code Subagents and Agent Skills**
    *   **Goal**: Explore and implement reusable intelligence for potential bonus marks.
    *   **Steps**:
        1.  **Research Claude Code Subagents/Skills**: Understand how to define and utilize subagents and skills within the Claude Code environment.
        2.  **Identify Potential Use Cases**: Based on the book content (once known) and chatbot development, identify areas where a subagent or skill could streamline future tasks (e.g., a skill to generate new book sections, or a subagent to help with chatbot debugging).
        *   **Implementation (if time permits)**: Develop a simple subagent or skill.

**5. Testing and Refinement**
    *   **Goal**: Ensure all components are working correctly and the project meets requirements.
    *   **Steps**:
        1.  **Unit and Integration Tests**: Write tests for the FastAPI backend and Docusaurus components.
        2.  **End-to-End Testing**: Test the entire flow from book content to chatbot interaction.
        3.  **Deployment Verification**: Ensure the deployed book and chatbot are accessible and functional on GitHub Pages.
        4.  **Refinement**: Address any bugs, improve performance, and enhance user experience.
