class QuizAgent:
    def __init__(self, memory=None, llm=None):
        self.memory = memory
        self.llm = llm

    def generate_quiz(self, user_input: str, n_questions: int = 3) -> str:
        history = self.memory.get_quiz_history() if self.memory else ""
        prompt = f"Create {n_questions} short quiz questions about: {user_input}. Context: {history}"
        if self.llm:
            return self.llm(prompt)
        return "\n".join([f"Q{i+1}: (sample) {user_input}?" for i in range(n_questions)])
