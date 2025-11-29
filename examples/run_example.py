from orchestrator.orchestrator import Orchestrator

def demo():
    orch = Orchestrator()
    queries = [
       "Explain the Binomial Theorem",                   
        "Give me a quiz on Chemical Bonding",            
        "Track my progress for today",
        "Recommend what I should study next",
        "Give me resources for Thermodynamics"
    ]
    for q in queries:
        print("User:", q)
        print("Response:", orch.handle_request(q))
        print("-" * 60)

if __name__ == "__main__":
    demo()
