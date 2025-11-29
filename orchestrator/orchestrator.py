import os
from agents import TutorAgent, QuizAgent, ProgressAgent, RecommendationAgent, ResourceAgent
from memory.memory_manager import MemoryManager

def make_llm():
    try:
        import openai
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return None
        openai.api_key = api_key

        def llm_call(prompt: str) -> str:
            # Minimal chat call compatible with common OpenAI SDKs
            resp = openai.ChatCompletion.create(
                model=os.getenv("EDUMENTOR_MODEL", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.2
            )
            # safe extraction of response text
            try:
                return resp.choices[0].message.content.strip()
            except Exception:
                return resp.choices[0].text.strip() if hasattr(resp.choices[0], "text") else ""
        return llm_call
    except Exception:
        return None

class Orchestrator:
    def __init__(self):
        self.memory = MemoryManager()
        llm = make_llm()

        self.tutor = TutorAgent(self.memory, llm)
        self.quiz = QuizAgent(self.memory, llm)
        self.progress = ProgressAgent(self.memory)
        self.recommendation = RecommendationAgent(self.memory, llm)
        self.resource = ResourceAgent(self.memory, llm)

    def handle_request(self, user_input: str) -> str:
        text = (user_input or "").lower()
        if any(k in text for k in ["explain", "learn", "help me", "i don't understand", "i dont understand"]):
            return self.tutor.explain_concept(user_input)
        if any(k in text for k in ["quiz", "test me", "practice"]):
            return self.quiz.generate_quiz(user_input)
        if any(k in text for k in ["progress", "track", "how am i"]):
            return self.progress.track_progress(user_input)
        if any(k in text for k in ["recommend", "what should i", "next step"]):
            return self.recommendation.generate_recommendations(user_input)
        if any(k in text for k in ["resource", "material", "summary", "notes"]):
            return self.resource.provide_resources(user_input)
        return self.tutor.explain_concept(user_input)
