"""System 2: Rule-based workflow. No LLM is used."""
import re
from config import ATTENDANCE, ASSIGNMENTS, QUESTIONS


def workflow(question):
    text = question.lower()

    # Rule 1: compare attendance with 75%
    match = re.search(r"(dbms|ai|cn)", text)
    if match and ("above 75" in text or "75%" in text):
        subject = match.group(1).upper()
        percentage = ATTENDANCE[subject]
        difference = percentage - 75

        if difference >= 0:
            return f"{subject} is above 75% by {difference} percentage points."

        return f"{subject} is below 75% by {abs(difference)} percentage points."

    # Rule 2: direct attendance lookup
    for subject, percentage in ATTENDANCE.items():
        if subject.lower() in text and "attendance" in text:
            return f"{subject} attendance: {percentage}%."

    # Rule 3: pending assignments
    if "pending" in text and "assignment" in text:
        pending = [
            s for s, info in ASSIGNMENTS.items()
            if info["status"] == "pending"
        ]
        return "Pending assignments: " + ", ".join(pending) + "."

    return "Sorry, this question is outside my predefined rules."


if __name__ == "__main__":
    print("=== SYSTEM 2: RULE-BASED WORKFLOW ===")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)