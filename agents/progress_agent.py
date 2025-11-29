class ProgressAgent:
    def __init__(self, memory):
        self.memory = memory

    def track_progress(self, user_input: str) -> str:
        self.memory.record_event({"type": "query", "text": user_input})
        return f"Progress summary: {self.memory.summary()}"
