from typing import Optional

class TutorAgent:
    def __init__(self, memory, llm=None):
        self.memory = memory
        self.llm = llm

    def explain_concept(self, user_input: str) -> str:
        context = self.memory.get_context() if self.memory else ""
        prompt = f"Explain clearly and simply: {user_input}\n\nContext: {context}\nKeep it short with one example."
        if self.llm:
            return self.llm(prompt)
        return "TutorAgent (mock): " + user_input
