from typing import Dict, List, Any, Optional
import uuid
import datetime

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self) -> str:
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "history": [],
            "last_active": datetime.datetime.now()
        }
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        session = self.sessions.get(session_id)
        if session:
            session["last_active"] = datetime.datetime.now()
        return session

    def update_session_history(self, session_id: str, message: Dict):
        if session_id in self.sessions:
            self.sessions[session_id]["history"].append(message)
            self.sessions[session_id]["last_active"] = datetime.datetime.now()

    def clear_session_history(self, session_id: str):
        if session_id in self.sessions:
            self.sessions[session_id]["history"] = []
            self.sessions[session_id]["last_active"] = datetime.datetime.now()

    def delete_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def cleanup_old_sessions(self, timeout_minutes: int = 60):
        cutoff_time = datetime.datetime.now() - datetime.timedelta(minutes=timeout_minutes)
        sessions_to_delete = [
            session_id for session_id, data in self.sessions.items()
            if data["last_active"] < cutoff_time
        ]
        for session_id in sessions_to_delete:
            self.delete_session(session_id) 