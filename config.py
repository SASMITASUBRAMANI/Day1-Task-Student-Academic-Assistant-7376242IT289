"""Shared configuration and private student data for the Day 1 task."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()
MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")

if PROVIDER != "groq":
    raise SystemExit("This project is configured for the Groq provider. Set PROVIDER=groq in .env.")

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise SystemExit("No GROQ_API_KEY found. Create a .env file from .env.example.")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY,
)

# Example private/local student data. Replace with your own data if required.
STUDENT = {
    "name": "Student A",
    "roll_no": "IT001",
    "semester": "S5",
}

ATTENDANCE = {
    "DBMS": 82,
    "AI": 91,
    "CN": 76,
}

ASSIGNMENTS = {
    "DBMS": {"status": "submitted", "due_days": 0},
    "AI": {"status": "pending", "due_days": 2},
    "CN": {"status": "pending", "due_days": 5},
}

QUESTIONS = [
    "What is my attendance in AI?",
    "Which subjects have pending assignments?",
    "Am I above 75% attendance in CN, and by how many percentage points?",
    "Give me a short reminder about my pending assignments.",
]
