class RecommendationAgent:
    def __init__(self, memory, llm=None):
        self.memory = memory
        self.llm = llm

    def generate_recommendations(self, user_input: str) -> str:
        summary = self.memory.summary()
        prompt = f"Based on: {summary}, recommend 2 short next steps for: {user_input}"
        if self.llm:
            return self.llm(prompt)
        return "RecommendationAgent (mock): 1) Review basics. 2) Try 3 practice questions."
