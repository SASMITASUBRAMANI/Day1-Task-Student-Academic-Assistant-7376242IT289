# Day 1 Task — Student Academic Assistant

This is the **Day 1 assessment project**, separate from the earlier course-fee practice project.

## Scenario
A private student academic assistant that answers attendance and assignment questions.

## Systems
1. Plain chatbot
2. Rule-based workflow
3. AI agent (LLM + Tools + Loop)

## Required submission files
- Complete Python code
- `Output/` folder with screenshots of all three systems
- `analysis.md`

## Setup
Copy `.env.example` to `.env`, add your Groq API key, and install requirements.

```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python check_setup.py
python chatbot.py
python workflow.py
python agent.py
```

Do not commit `.env`.
