"""Day 2 Task: Run the existing ReAct agent on the chosen scenario."""

from agent import agent


QUESTION = (
    "Which assignments are currently pending, "
    "and how many days are left for each?"
)


if __name__ == "__main__":

    print("=" * 70)
    print("DAY 2 TASK - ReAct AGENT")
    print("=" * 70)

    print("\nQUESTION:")
    print(QUESTION)

    print("\n--- REACT TRACE ---")

    answer = agent(
        QUESTION,
        max_steps=6
    )

    print("\n--- FINAL ANSWER ---")
    print(answer)