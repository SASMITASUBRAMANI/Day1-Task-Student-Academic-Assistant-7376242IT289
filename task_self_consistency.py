"""Day 2 Task: Self-consistency with Chain-of-Thought."""

from collections import Counter

from config import client, MODEL


QUESTION = (
    "A student has 82% attendance in DBMS, 91% in AI, "
    "and 76% in CN. What is the average attendance percentage?"
)


COT_PROMPT = """
You are a Student Academic Assistant.

Solve the problem step by step.

Number each step clearly.
Show the calculation.

After the steps, write:

Final Answer: <answer>
"""


RUNS = 5


def get_final_answer(text):

    for line in reversed(text.splitlines()):

        if "final answer" in line.lower():

            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip()


def run_experiment(temperature):

    answers = []

    print(
        f"\nTemperature = {temperature}"
    )

    print("-" * 60)

    for run in range(1, RUNS + 1):

        response = client.chat.completions.create(

            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": QUESTION
                }
            ],

            temperature=temperature
        )

        text = response.choices[0].message.content

        answer = get_final_answer(text)

        print(
            f"Run {run}: {answer}"
        )

        answers.append(answer)

    return answers


if __name__ == "__main__":

    print("=" * 70)
    print("DAY 2 TASK - SELF CONSISTENCY")
    print("=" * 70)

    print("\nQUESTION:")
    print(QUESTION)

    # Run 5 times with non-zero temperature
    answers = run_experiment(
        temperature=0.8
    )

    counts = Counter(answers)

    majority_answer, majority_count = (
        counts.most_common(1)[0]
    )

    print("\n--- MAJORITY ANSWER ---")

    print(
        majority_answer
    )

    print(
        f"Count: {majority_count}/{RUNS}"
    )

    # Run 5 times with temperature 0
    zero_answers = run_experiment(
        temperature=0
    )

    zero_counts = Counter(zero_answers)

    zero_answer, zero_count = (
        zero_counts.most_common(1)[0]
    )

    print("\n--- TEMPERATURE 0 RESULT ---")

    print(
        f"Majority answer: {zero_answer}"
    )

    print(
        f"Count: {zero_count}/{RUNS}"
    )