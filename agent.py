"""System 3: AI agent = LLM + Tools + Loop."""

import json

from config import client, MODEL, QUESTIONS
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a student academic assistant. "
    "The student's data is private and must be accessed only through tools. "
    "Never guess attendance or assignment status. "
    "Use get_attendance for attendance, "
    "get_pending_assignments for pending work, "
    "and calculator for arithmetic. "
    "Use tools when needed, then continue until you can give the final answer."
)


def agent(question, max_steps=6):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0,
            parallel_tool_calls=False
        )

        message = response.choices[0].message

        # If the model has finished and does not need a tool
        if not message.tool_calls:
            return (message.content or "").strip()

        # Store the assistant's tool calls
        assistant_calls = []

        for call in message.tool_calls:

            # Some models may return extra information after |
            name = call.function.name.split("|", 1)[0]

            assistant_calls.append(
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": name,
                        "arguments": call.function.arguments
                    }
                }
            )

        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": assistant_calls
            }
        )

        # Execute each requested tool
        for call in message.tool_calls:

            name = call.function.name.split("|", 1)[0]

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            if function:

                # get_pending_assignments does not need arguments
                if name == "get_pending_assignments":
                    result = function()

                else:
                    result = function(**arguments)

            else:
                result = f"Unknown tool: {name}"

            print(
                f"  step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                }
            )

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    print("=== SYSTEM 3: AI AGENT ===")

    for question in QUESTIONS:

        print("Q:", question)

        print("A:", agent(question))

        print("-" * 70)