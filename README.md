# Local AI Chatbot

## Project Overview
This project provides a complete local AI chatbot application. It utilizes Python FastAPI for the backend, Streamlit for the frontend, and Ollama for local AI model inference. The system is designed to offer a seamless chat experience, including dynamic model selection and the preservation of conversation context.

## Core Requirements

### Technology Stack
- **Backend**: FastAPI with Python
- **Frontend**: Streamlit
- **AI Engine**: Ollama (local inference)
- **Session Management**: In-memory storage
- **Communication**: REST API

### Must-Have Features
1.  **Dynamic Model Selection**: Dropdown menu populated with available Ollama models.
2.  **Conversation Context**: Preserves chat history during the active session.
3.  **Real-time Chat Interface**: Provides responsive message exchange.
4.  **Session Management**: Handles multiple concurrent conversations.
5.  **Error Handling**: Graceful handling of API failures and model issues.

## Project Structure
```
local-ai-chatbot/
├── backend/
│   ├── main.py
│   ├── models/chat.py
│   ├── services/ollama_service.py
│   └── utils/session_manager.py
├── frontend/
│   ├── streamlit_app.py
│   ├── components/
│   │   ├── chat_interface.py
│   │   └── model_selector.py
└── README.md
```

## Key Dependencies

### Backend:
-   `fastapi`
-   `uvicorn`
-   `ollama`
-   `pydantic`
-   `python-multipart`

### Frontend:
-   `streamlit`
-   `requests`
-   `streamlit-chat` (optional for enhanced UI)

## Configuration Requirements
-   Ollama running locally on default port (11434).
-   At least one model pulled (e.g., `ollama pull llama2`).
-   Python 3.12+ environment.

## Running with Docker

Alternatively, you can run the entire application using Docker. Ensure Docker Desktop is running on your machine and Ollama is accessible on your host machine.

### 1. Build the Docker Image
Navigate to the root directory of the project (where the `Dockerfile` is located) and build the Docker image:

```bash
docker build -t local-ai-chatbot-image .
```

### 2. Run the Docker Container
Run the Docker container, mapping the necessary ports and connecting to your host's Ollama instance. The `--name` flag is used to assign a memorable name to your container.

```bash
docker run --name local-ai-chatbot -p 8000:8000 -p 8501:8501 local-ai-chatbot-image
```

**Note**: The `Dockerfile` includes an `ENV OLLAMA_HOST=http://host.docker.internal:11434` variable. This special Docker hostname allows the container to connect to the Ollama service running on your host machine. If you are not using Docker Desktop (e.g., on Linux with a different Docker setup), you might need to adjust `host.docker.internal` to your host's actual IP address or configure Docker's network mode appropriately.

Once the container is running, the backend will be accessible at `http://localhost:8000` and the Streamlit frontend at `http://localhost:8501`.

## Getting Started

### 1. Setup
-   **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/local-ai-chatbot.git
    cd local-ai-chatbot
    ```
-   **Create a Python virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```
-   **Activate the virtual environment**:
    -   On Windows: `.\venv\Scripts\activate`
    -   On macOS/Linux: `source venv/bin/activate`

### 2. Install Dependencies
Install all required packages for both backend and frontend:
```bash
pip install fastapi uvicorn ollama pydantic python-multipart streamlit requests
```

### 3. Start the Backend
Navigate to the `backend` directory and run the FastAPI application:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The backend server will start on `http://localhost:8000`. Keep this terminal running.

### 4. Start the Frontend
Open a new terminal, navigate to the `frontend` directory, and run the Streamlit application:
```bash
cd frontend
streamlit run streamlit_app.py
```
This will open the Streamlit chatbot interface in your web browser.

## Usage
-   **Model Selection**: Choose an available Ollama model from the sidebar dropdown.
-   **Chat**: Type your messages in the input box and press Enter.
-   **Conversation Context**: Your chat history will be preserved within the active session.
-   **Clear Chat**: Use the "Clear Chat History" button in the sidebar to reset the current conversation.

