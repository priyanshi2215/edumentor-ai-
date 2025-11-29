import json
from pathlib import Path

STORE_FILE = Path(__file__).parent / "memory_store.json"

class MemoryManager:
    def __init__(self):
        self._data = {"events": []}
        if STORE_FILE.exists():
            try:
                self._data = json.loads(STORE_FILE.read_text())
            except Exception:
                self._data = {"events": []}

    def record_event(self, event: dict):
        self._data.setdefault("events", []).append(event)
        self._save()

    def summary(self) -> str:
        n = len(self._data.get("events", []))
        return f"{n} events recorded."

    def get_context(self) -> str:
        events = self._data.get("events", [])
        last = events[-3:] if events else []
        return " | ".join(e.get("text", "") for e in last)

    def get_quiz_history(self) -> str:
        return ", ".join(e.get("text", "") for e in self._data.get("events", []) if e.get("type") == "quiz")

    def _save(self):
        try:
            STORE_FILE.write_text(json.dumps(self._data, indent=2))
        except Exception:
            pass
