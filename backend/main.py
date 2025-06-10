from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models.chat import ChatRequest, Message
from backend.services.ollama_service import OllamaService
from backend.utils.session_manager import SessionManager

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize services
ollama_service = OllamaService()
session_manager = SessionManager()

@app.get("/")
async def read_root():
    return {"message": "Local AI Chatbot Backend is running!"}

@app.get("/models")
async def get_models():
    models = ollama_service.get_available_models()
    return {"models": models}

@app.post("/chat")
async def chat_with_ollama(chat_request: ChatRequest):
    session_id = chat_request.session_id
    if not session_id:
        # If no session_id is provided, create a new one.
        session_id = session_manager.create_session()
    else:
        # If a session_id is provided, try to retrieve it.
        session = session_manager.get_session(session_id)
        # If the provided session_id does not exist, create a new session instead of raising 404.
        if not session:
            session_id = session_manager.create_session()

    # Always ensure session is valid and retrieved before proceeding
    session = session_manager.get_session(session_id)
    if not session:
        # This case should ideally not be reachable with the logic above,
        # but provides a fallback for unexpected issues.
        raise HTTPException(status_code=500, detail="Failed to establish or retrieve session unexpectedly.")

    # Append user message to history
    user_message = {"role": "user", "content": chat_request.messages[-1].content}
    session_manager.update_session_history(session_id, user_message)

    # Get conversation history for context
    messages_for_ollama = session["history"]

    try:
        response = ollama_service.chat_completion(
            model=chat_request.model,
            messages=messages_for_ollama,
            stream=chat_request.stream
        )

        # For non-streaming, append AI response to history
        if not chat_request.stream:
            ai_message = {"role": "assistant", "content": response["message"]["content"]}
            session_manager.update_session_history(session_id, ai_message)
            return {"response": response["message"]["content"], "session_id": session_id}
        else:
            # Handle streaming response (yield chunks)
            # This is a simplified example, actual streaming would require more complex handling
            # For now, we'll just return a placeholder for streaming
            full_response_content = ""
            for chunk in response:
                content = chunk["message"]["content"]
                full_response_content += content
                # In a real streaming scenario, you'd yield this chunk

            ai_message = {"role": "assistant", "content": full_response_content}
            session_manager.update_session_history(session_id, ai_message)
            return {"response": full_response_content, "session_id": session_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama chat error: {e}")

@app.get("/sessions/{session_id}")
async def get_session_history(session_id: str):
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"session_id": session_id, "history": session["history"]}

@app.delete("/sessions/{session_id}")
async def clear_session(session_id: str):
    session_manager.clear_session_history(session_id)
    return {"message": f"Session {session_id} history cleared."} 