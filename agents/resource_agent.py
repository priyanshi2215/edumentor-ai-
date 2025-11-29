class ResourceAgent:
    def __init__(self, memory=None, llm=None):
        self.memory = memory
        self.llm = llm

    def provide_resources(self, user_input: str) -> str:
        prompt = f"Provide a short summary and 1-2 resources for: {user_input}"
        if self.llm:
            return self.llm(prompt)
        return "ResourceAgent (mock): Short summary + example link: https://example.com"
