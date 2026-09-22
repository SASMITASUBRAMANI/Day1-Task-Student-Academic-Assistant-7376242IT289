"""Day 2 Task: Compare Direct Prompting and Chain-of-Thought."""

from config import client, MODEL


QUESTIONS = [
    (
        "What is the attendance percentage for AI?"
    ),

    (
        "A student has 82% attendance in DBMS, 91% in AI, "
        "and 76% in CN. What is the average attendance percentage?"
    ),

    (
        "A student has 82% attendance in DBMS and 76% in CN. "
        "If the student attends 10 more classes in each subject "
        "without missing any, what will the new attendance "
        "percentage be if the current total classes are 100 "
        "for each subject?"
    ),

    (
        "Which subject has the highest attendance: DBMS, AI, or CN?"
    ),
]


DIRECT_PROMPT = """
You are a Student Academic Assistant.

Answer the question directly.

Give only the final answer.
Do not explain your reasoning.
Do not use tools.
"""


COT_PROMPT = """
You are a Student Academic Assistant.

Solve the problem step by step.

Number each step clearly.
Show calculations when required.

Do not use external tools.

After the steps, write:

Final Answer: <answer>
"""


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    print("=" * 70)
    print("DAY 2 TASK")
    print("DIRECT PROMPTING vs CHAIN-OF-THOUGHT")
    print("=" * 70)

    for number, question in enumerate(QUESTIONS, start=1):

        print("\n" + "=" * 70)
        print(f"QUESTION {number}")
        print("=" * 70)

        print(question)

        print("\n--- WITHOUT CoT ---")

        direct_answer = ask(
            DIRECT_PROMPT,
            question
        )

        print(direct_answer)

        print("\n--- WITH CoT ---")

        cot_answer = ask(
            COT_PROMPT,
            question
        )

        print(cot_answer)