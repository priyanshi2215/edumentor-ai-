# 🌟 EduMentor AI — Multi-Agent Personalized Learning System

EduMentor AI is an adaptive multi-agent learning companion designed to support every type of learner—especially those who struggle with traditional “one-size-fits-all” systems.  
It observes patterns, detects confusion, adapts difficulty, and guides students with personalized mentorship.

---

## 🎯 Problem Statement

Most education systems assume all students learn the same way.  
But learners differ in:

- pace  
- attention  
- reasoning style  
- memory  
- understanding patterns  

Neurodiverse learners (ADHD, dyslexia, slow processing) are affected most.  
Traditional tools only react when the student asks for help.

**EduMentor AI changes this.**  
It continuously:

- monitors learning patterns  
- detects hidden confusion  
- adapts explanations  
- generates personalized practice  
- guides next steps  

A system that behaves like a real mentor — consistent, attentive, supportive.

---

## 🤖 Why Agents?

Teaching requires many skills:

- explaining concepts  
- generating quizzes  
- tracking progress  
- identifying gaps  
- suggesting what to learn next  
- giving summaries or examples  

A single LLM becomes inconsistent if forced to do everything.

A **multi-agent system** solves this through specialization:

- **Tutor Agent** — explanations that adjust to difficulty  
- **Quiz Agent** — adaptive practice questions  
- **Progress Agent** — learns from patterns & mistakes  
- **Recommendation Agent** — next-step guidance  
- **Resource Agent** — summaries, notes, examples  

The **Orchestrator** coordinates all agents to make the experience feel unified.

---

## 🧠 System Architecture

```
edumentor-ai/
│
├── agents/
│   ├── tutor_agent.py
│   ├── quiz_agent.py
│   ├── progress_agent.py
│   ├── recommendation_agent.py
│   ├── resource_agent.py
│   └── __init__.py
│
├── orchestrator/
│   ├── orchestrator.py
│   └── __init__.py
│
├── memory/
│   ├── memory_store.json
│   └── memory_manager.py
│
├── examples/
│   ├── demo_run.ipynb
│   └── example_inputs.md
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How the System Works

### **1. Student Query Layer**
User sends messages like:

- "Explain the Binomial Theorem"
- "Give me a quiz on Chemical Bonding"
- "Track my progress for today"
- "Recommend what I should study next"
- "Give me resources for Thermodynamics"

A rule-based router detects intent.

---

### **2. Core Agents**

#### 📘 Tutor Agent
- Explains concepts at the right level  
- Simplifies when the student struggles  
- Deepens when mastery is detected  

#### 📝 Quiz Agent
- Generates MCQs and reasoning questions  
- Adapts difficulty based on performance  

#### 📊 Progress Agent
Stores learning patterns:

- strengths  
- weaknesses  
- repeated mistakes  
- pacing  
- preferred explanation style  

#### 🎯 Recommendation Agent
Decides:

- revise  
- practice  
- move ahead  
- increase difficulty  

#### 📚 Resource Agent
Generates:

- notes  
- formula sheets  
- examples  
- revision summaries  

---

### **3. Long-Term Memory System**
Keeps track of:

- topics learned  
- concepts mastered  
- quiz history  
- misconceptions  
- learning speed  

This prevents the system from “resetting” every session.

---

### **4. Orchestrator**
The system brain that:

- detects intent  
- selects the correct agent  
- pulls past memory  
- merges outputs into one response  

---

### **5. Output Layer**
Students receive:

- explanations  
- quizzes  
- progress updates  
- study plans  
- personalized resources  

---

## 🧪 Example Interaction

### **Student**  
“Explain Newton’s Third Law. I keep forgetting.”

### **System Behavior**
- Tutor Agent detects confusion → gives adapted explanation  
- Progress Agent logs weakness  
- Recommendation Agent suggests a short check  
- Quiz Agent provides 2 targeted questions  
- Resource Agent creates a simple summary  

---

## 🛠️ Technologies Used

- Multi-agent architecture  
- Python  
- Google Gemini API  
- Memory-augmented reasoning  
- Intent-based routing  
- Modular, scalable structure  


---

## 🌍 Impact

What makes EduMentor AI unique:

- continuous adaptation  
- memory-driven personalization  
- multi-agent specialization  
- support for neurodiverse learners  
- proactive detection of confusion  
- real-time difficulty adjustment  

EduMentor AI behaves like a mentor who remembers you.

---

## 📌 Running the Project (Kaggle Notebook)

1. Clone repo  
2. Install requirements  
3. Load API key using Kaggle Secrets  
4. Import orchestrator  
5. Run sample query  

---

## 👩‍💻 Author
Priyanshi



