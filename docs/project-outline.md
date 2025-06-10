# Local AI Chatbot Development Prompt

## Project Overview
Create a complete local AI chatbot application using Python FastAPI as backend, Streamlit as frontend, and Ollama for local AI model inference. The system should provide a seamless chat experience with model selection capabilities and conversation context preservation.

## Core Requirements

### Technology Stack
- **Backend**: FastAPI with Python
- **Frontend**: Streamlit
- **AI Engine**: Ollama (local inference)
- **Session Management**: In-memory storage
- **Communication**: REST API

### Must-Have Features
1. **Dynamic Model Selection**: Dropdown menu populated with available Ollama models
2. **Conversation Context**: Preserve chat history during active session
3. **Real-time Chat Interface**: Responsive message exchange
4. **Session Management**: Handle multiple concurrent conversations
5. **Error Handling**: Graceful handling of API failures and model issues

## Development Tasks

### Phase 1: Backend Development (FastAPI)
**Create the following components:**

1. **Main FastAPI Application** (`backend/app/main.py`)
   - CORS configuration for Streamlit integration
   - API endpoints setup
   - Error handling middleware

2. **API Endpoints**
   - `GET /models` - Fetch available Ollama models
   - `POST /chat` - Process chat messages and return AI responses
   - `GET /sessions/{session_id}` - Retrieve conversation history
   - `DELETE /sessions/{session_id}` - Clear conversation history

3. **Ollama Service Integration** (`backend/app/services/ollama_service.py`)
   - Connect to local Ollama instance
   - Model availability checking
   - Message processing with context
   - Response streaming (optional)

4. **Data Models** (`backend/app/models/chat.py`)
   - Request/response Pydantic models
   - Message structure definition
   - Session data models

5. **Session Manager** (`backend/app/utils/session_manager.py`)
   - In-memory conversation storage
   - Session lifecycle management
   - Context preservation logic

### Phase 2: Frontend Development (Streamlit)
**Create the following components:**

1. **Main Streamlit App** (`frontend/streamlit_app.py`)
   - App layout and configuration
   - Session state initialization
   - Component integration

2. **Model Selector Component** (`frontend/components/model_selector.py`)
   - Dynamic dropdown population
   - Model switching functionality
   - API integration for model fetching

3. **Chat Interface Component** (`frontend/components/chat_interface.py`)
   - Message display area
   - Input handling
   - Chat history rendering
   - Loading states

4. **API Client Functions**
   - HTTP requests to FastAPI backend
   - Error handling and retries
   - Response processing

### Phase 3: Integration & Enhancement
1. **End-to-End Testing**
   - API connectivity verification
   - Chat flow testing
   - Model switching validation

2. **User Experience Improvements**
   - Loading indicators
   - Error messages
   - Chat clearing functionality
   - Responsive design

3. **Performance Optimization**
   - Session cleanup
   - Memory management
   - Response time optimization

## Technical Specifications

### Project Structure
```
local-ai-chatbot/
├── backend/
│   ├── main.py
│   ├── models/chat.py
│   ├── services/ollama_service.py
│   └── utils/session_manager.py
│   └── requirements.txt
├── frontend/
│   ├── streamlit_app.py
│   ├── components/
│   │   ├── chat_interface.py
│   │   └── model_selector.py
│   └── requirements.txt
└── README.md
```

### Key Dependencies
**Backend:**
- fastapi
- uvicorn
- ollama
- pydantic
- python-multipart

**Frontend:**
- streamlit
- requests
- streamlit-chat (optional for enhanced UI)

### Configuration Requirements
- Ollama running locally on default port (11434)
- At least one model pulled (e.g., `ollama pull llama2`)
- Python 3.8+ environment

## Implementation Guidelines

### Backend Best Practices
- Use async/await for API endpoints
- Implement proper error handling and logging
- Validate all inputs with Pydantic models
- Use dependency injection for services
- Include API documentation with FastAPI's automatic docs

### Frontend Best Practices
- Use Streamlit session state for persistence
- Implement loading states for better UX
- Handle API errors gracefully
- Organize code into reusable components
- Maintain clean and intuitive UI layout

### Session Management Strategy
- Generate unique session IDs for each user
- Store conversation history with timestamps
- Implement session timeout and cleanup
- Preserve context across model switches (optional)

## Development Workflow
1. **Setup**: Install Ollama, create virtual environments
2. **Backend First**: Develop and test API endpoints
3. **Frontend Integration**: Build Streamlit interface
4. **Testing**: End-to-end functionality verification
5. **Refinement**: UI/UX improvements and bug fixes

## Success Criteria
- [ ] User can select from available Ollama models
- [ ] Chat interface responds with AI-generated messages
- [ ] Conversation context is maintained during session
- [ ] Multiple sessions can run independently
- [ ] Application runs reliably on local machine
- [ ] Clean, intuitive user interface
- [ ] Proper error handling and user feedback

## Bonus Features to Consider
- Model switching mid-conversation
- Export chat history
- Custom model parameters (temperature, max tokens)
- Dark/light theme toggle
- Chat streaming for real-time responses
