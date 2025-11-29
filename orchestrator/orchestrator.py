import os
import google.generativeai as genai

from agents import TutorAgent, QuizAgent, ProgressAgent, RecommendationAgent, ResourceAgent
from memory.memory_manager import MemoryManager


def make_llm():
    """Creates a simple LLM call wrapper using Google Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None

    genai.configure(api_key=api_key)

    model_name = os.getenv("EDUMENTOR_MODEL", "models/gemini-1.5-flash")

    model = genai.GenerativeModel(model_name)

    def llm_call(prompt: str) -> str:
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"LLM Error: {str(e)}"

    return llm_call


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
