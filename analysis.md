# Day 2 Task: Reasoning and Acting

## 1. Scenario

For this task, I continued with the Student Academic Assistant scenario. The system works with private student academic information such as attendance percentages and pending assignments.

The student data used in the experiment contains the following attendance values: DBMS 82%, AI 91%, and CN 76%. The assignment information shows that DBMS has been submitted, while AI has 2 days remaining and CN has 5 days remaining.

The purpose of this task is to compare three approaches for solving questions in this scenario: Direct Prompting, Chain-of-Thought (CoT), and a ReAct agent. I also performed a self-consistency experiment using repeated Chain-of-Thought runs.

---

## 2. Direct Prompting

Direct prompting asks the language model to provide an answer directly without showing its reasoning and without using tools.

In my experiment, the direct prompt was tested with several attendance-related questions. For the question asking for the AI attendance percentage, the model returned 75%. However, the actual student data contains an AI attendance of 91%. This showed that the model could give an answer even when it did not have access to the private student data.

For the average attendance question, the direct response calculated the average as 83%, which was correct. For the question involving additional classes, the response calculated the updated attendance values as 83.64% for DBMS and 78.18% for CN.

For the question asking which subject had the highest attendance, the direct response answered DBMS. However, according to the actual student data, AI has the highest attendance at 91%.

These results show that direct prompting can work for calculations when the required values are available in the question, but it can produce unsupported or incorrect answers when private information is required.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting asks the model to solve a problem step by step before giving the final answer. This approach makes the calculation or reasoning process more visible.

In my experiment, Chain-of-Thought correctly calculated the average attendance as 83%. It also correctly calculated the updated attendance values as 83.64% for DBMS and 78.18% for CN.

However, Chain-of-Thought could not retrieve the private attendance information when it was not included in the question. For the question asking which subject had the highest attendance, the model stated that it needed the attendance values to determine the answer. It also could not independently retrieve the AI attendance value.

This demonstrates that step-by-step reasoning does not provide access to private information. Chain-of-Thought can reason over information available to the model, but it cannot fetch missing facts from the application's private data by itself.

---

## 4. ReAct Agent

The ReAct approach combines reasoning with actions. The agent can decide that it needs additional information, call a tool, observe the result, and then continue to the final answer.

The existing Student Academic Assistant contains tools for accessing student information, including `get_attendance()` and `get_pending_assignments()`.

For the ReAct experiment, I asked:

"Which assignments are currently pending, and how many days are left for each?"

The agent identified that it needed the pending-assignment information and called the `get_pending_assignments()` tool. The tool returned that AI had 2 days remaining and CN had 5 days remaining.

The agent then used the tool result to produce the final answer. The output therefore demonstrated the ReAct process of using a tool, receiving an observation, and then producing a final response.

This shows how ReAct can handle questions that require private information stored outside the model's direct knowledge.

---

## 5. Comparison Table

| Basis for comparison | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Gives a direct answer without visible reasoning. | Performs step-by-step reasoning and shows the steps. | Combines reasoning with tool actions and observations. |
| Tool usage | No tool usage. | No tool usage in this experiment. | Uses tools when additional student information is required. |
| Reliability on multi-step questions | Can solve some calculations but may give unsupported answers when information is missing. | Performs multi-step calculations more explicitly when the required information is available. | Can combine reasoning with information retrieved from tools. |
| Transparency | The response does not show the reasoning process. | The reasoning steps are shown in the response. | Tool calls and their returned observations are visible in the trace. |
| Speed / cost | Usually requires a direct model response and is relatively simple. | Produces longer responses because reasoning steps are included. | May require multiple model and tool interactions. |
| Consistency across repeated runs | Can vary depending on model settings. | Can vary at non-zero temperature. | Tool results remain tied to the underlying data, although generated responses can still vary. |

---

## 6. Self-Consistency Observation

For the self-consistency experiment, I used the question:

"A student has 82% attendance in DBMS, 91% in AI, and 76% in CN. What is the average attendance percentage?"

The correct calculation is:

(82 + 91 + 76) / 3 = 83%

I first ran the Chain-of-Thought prompt five times with a temperature of 0.8. The displayed final answers were all 83%. The program reported a majority count of 4 out of 5 because some returned strings contained small formatting differences. Therefore, the semantic answer across the displayed runs was 83%, and it was correct.

I then repeated the experiment with temperature 0. All five runs produced 83%, and the program reported a majority count of 5 out of 5.

This experiment showed that the repeated outputs were more consistent at temperature 0 for this question. It also showed that self-consistency depends on how final answers are extracted and compared because small formatting differences can affect exact string-based counting.

---

## 7. Suitability Analysis

The experiment shows that the three approaches are useful for different types of questions in the Student Academic Assistant scenario.

Direct Prompting is useful when the required information is already available to the model and a short answer is sufficient. It is simple and fast, but my experiment showed that it can produce an incorrect answer when private student information is not available in the prompt.

Chain-of-Thought is useful for questions involving calculations or multiple reasoning steps. In my experiment, it correctly calculated the average attendance and the updated attendance percentages. However, it could not retrieve private attendance information that was not provided in the question.

ReAct is useful when the question requires information from a private data source or tool. In my experiment, the ReAct agent used `get_pending_assignments()` and obtained the current assignment information before producing its final answer.

Therefore, the choice of approach depends on the problem. Direct Prompting can handle straightforward questions, Chain-of-Thought can help with multi-step reasoning, and ReAct can be used when reasoning needs to be combined with external or private information.

---

## 8. Conclusion

This task demonstrated the differences between Direct Prompting, Chain-of-Thought, and ReAct using a Student Academic Assistant scenario.

Direct Prompting generates an answer directly without visible reasoning or tool access. Chain-of-Thought makes the reasoning steps explicit and can help with multi-step calculations, but it cannot retrieve information that is not available to the model. ReAct combines reasoning with actions and observations, allowing the agent to use tools when additional information is required.

The experiments showed that the three approaches have different uses. Direct Prompting is suitable for simple questions where the required information is already available. Chain-of-Thought is useful for problems that require several reasoning or calculation steps. ReAct is useful when the task requires access to private data or other tool-based information.

The self-consistency experiment also showed that repeated Chain-of-Thought runs can be compared to identify a majority answer, while temperature 0 produced identical answers across the five runs for the tested question.