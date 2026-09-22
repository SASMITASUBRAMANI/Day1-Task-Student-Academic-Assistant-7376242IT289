"""System 1: Plain chatbot for a private student-data scenario."""
from config import client, MODEL, STUDENT, ATTENDANCE, ASSIGNMENTS, QUESTIONS

PRIVATE_CONTEXT = f"""
Student profile: {STUDENT}
Attendance: {ATTENDANCE}
Assignments: {ASSIGNMENTS}
"""

SYSTEM_PROMPT = (
    "You are a student academic assistant. Answer using only the private student "
    "data supplied in the conversation. Do not invent missing values. "
    "You are a plain chatbot: do not call tools."
)

def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PRIVATE_CONTEXT + "\nQuestion: " + question},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("=== SYSTEM 1: PLAIN CHATBOT ===")
    for question in QUESTIONS:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 70)
