import streamlit as st
import requests
import uuid

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Local AI Chatbot", layout="centered")
st.title("Local AI Chatbot")

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "selected_model" not in st.session_state:
    st.session_state["selected_model"] = None

# --- API Client Functions ---

def get_models():
    try:
        response = requests.get(f"{BACKEND_URL}/models")
        response.raise_for_status()
        return response.json().get("models", [])
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend. Please ensure FastAPI backend is running.")
        return []
    except Exception as e:
        st.error(f"Error fetching models: {e}")
        return []

def send_message(model: str, message_content: str, session_id: str):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message_content}],
        "session_id": session_id
    }
    try:
        response = requests.post(f"{BACKEND_URL}/chat", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend. Please ensure FastAPI backend is running.")
        return None
    except Exception as e:
        st.error(f"Error sending message: {e}")
        return None

# --- Model Selector Component ---

models = get_models()
model_names = [model["name"] for model in models]

if not model_names:
    st.warning("No Ollama models found. Please ensure Ollama is running and models are pulled (e.g., 'ollama pull llama2').")
else:
    selected_model_name = st.sidebar.selectbox(
        "Select an Ollama Model",
        model_names,
        index=0 if st.session_state["selected_model"] is None else model_names.index(st.session_state["selected_model"])
    )
    if selected_model_name:
        st.session_state["selected_model"] = selected_model_name

# --- Chat Interface Component ---

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    if st.session_state["selected_model"]:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Thinking..."):
            response_data = send_message(
                st.session_state["selected_model"],
                prompt,
                st.session_state["session_id"]
            )

            if response_data and "response" in response_data:
                ai_response = response_data["response"]
                st.session_state["messages"].append({"role": "assistant", "content": ai_response})
                with st.chat_message("assistant"):
                    st.markdown(ai_response)
            else:
                st.error("Failed to get a response from the AI.")
    else:
        st.warning("Please select an Ollama model first.")

# Clear Chat History Button
if st.sidebar.button("Clear Chat History"):
    try:
        requests.delete(f"{BACKEND_URL}/sessions/{st.session_state["session_id"]}")
        st.session_state["messages"] = []
        st.session_state["session_id"] = str(uuid.uuid4()) # Generate new session ID
        st.rerun()
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend to clear session. Please ensure FastAPI backend is running.")
    except Exception as e:
        st.error(f"Error clearing session: {e}") 