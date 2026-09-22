# Day 1 Task: Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

For this task, I chose a small **Student Academic Assistant** scenario. The system uses a local student record that contains attendance percentages for DBMS, AI, and CN, along with information about pending assignments and their due time.

I used the same student information with three different approaches: a plain chatbot, a rule-based workflow, and an AI agent. The main purpose is to understand how each approach works and how their behavior changes when the same problem is solved in different ways.

In this scenario, the plain chatbot mainly uses an LLM to generate answers, the rule-based workflow follows predefined conditions without using an LLM, and the AI agent combines an LLM, tools, and a loop to complete the task.

## 2. Plain Chatbot

The plain chatbot gets the student's private information through the conversation context. The student data and the question are sent to the LLM, and the LLM generates the answer.

There are no separate tools in this approach. The chatbot simply uses the information provided in its prompt to answer the question.

One advantage is that the chatbot can understand different ways of asking the same question because the LLM can interpret natural language. However, it can only work with the private information that is provided to it in the conversation. It also does not have a separate tool for retrieving data or doing calculations.

For example, if I ask, **"What is my attendance in AI?"**, the chatbot uses the attendance information given in its context and generates the answer.

## 3. Rule-Based Workflow

The rule-based workflow works differently because it does not use an LLM. Instead, it uses Python code and predefined conditions.

The student information is stored in Python dictionaries. Based on the question, the program checks the conditions and returns the required information. For example, it can find a subject's attendance, identify pending assignments, or compare attendance with 75%.

The main advantage of this approach is that the result is predictable for the questions covered by the rules. However, it is less flexible. If the user asks a question that was not considered while writing the rules, the program may not understand it. To support new types of questions, additional conditions have to be added to the code.

For example, when the user asks about CN attendance and the 75% requirement, the workflow follows the predefined condition and calculates the difference.

## 4. AI Agent

The AI agent follows the idea of **LLM + Tools + Loop**.

In this approach, the LLM receives the user's question and decides which tool is needed. The tools can be used to access the student's attendance, find pending assignments, or perform calculations.

After a tool is called, its result is returned to the agent. The agent can then use that result and decide whether another tool is required. This process continues until the agent has enough information to give the final answer.

For example, if the user asks whether their CN attendance is above 75%, the agent can first use the attendance tool to get the CN attendance. It can then use the calculator tool to find the difference between the attendance and 75%.

This makes the agent more flexible and useful for multi-step questions. At the same time, it is more complex to implement because the tools and the tool-calling loop have to work correctly.

## 5. Comparison Table

| Basis for comparison | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Can understand different natural-language questions | Works mainly with predefined question patterns | Can understand different questions and decide which tools to use |
| Decision-making | The LLM generates the response | Decisions are made using fixed conditions | The LLM decides which tool or action is needed |
| Tool usage | No separate tools | Uses predefined Python rules and data | Uses attendance, assignment, and calculator tools |
| Private-data access | Private data is given through the prompt/context | Directly accesses local student data | Accesses private data through tools |
| Multi-step task handling | Limited in this implementation | Must be manually programmed | Can perform multiple tool calls in a loop |
| Automation | Automatically generates responses | Automatically follows fixed rules | Can automatically select and use tools |
| Reliability | Depends on the generated response | Predictable for supported rules | Depends on both the tools and the model's tool selection |

## 6. Suitability Analysis

The three approaches can all be used for the Student Academic Assistant, but they work differently depending on the type of question.

A **plain chatbot** is useful when the main requirement is to have a natural conversation and the required information can simply be provided in the prompt. It is easy to use and can handle different ways of asking a question.

A **rule-based workflow** is useful when the questions and conditions are already known. For example, if the system only needs to check attendance, list pending assignments, and apply a fixed percentage rule, predefined Python rules can handle these tasks in a predictable way.

An **AI agent** is useful when the user may ask different types of questions and the task may require more than one action. In this project, the agent can access private information through tools and can perform multiple steps before giving the final response.

Therefore, the suitable approach depends on the requirements of the problem. A fixed task can be handled using rules, a simple conversational task can use a chatbot, and a task involving flexible questions and multiple tool-based actions can use an AI agent.

## 7. Conclusion

Through this task, I understood that a chatbot, a rule-based workflow, and an AI agent can solve the same problem in three different ways.

A **plain chatbot** mainly depends on an LLM to understand the question and generate a response. A **rule-based workflow** does not use an LLM and instead follows conditions that have already been programmed. An **AI agent** combines an LLM with tools and a loop, allowing it to select actions, receive results, and continue working until it can answer the user's request.

In general, a chatbot is useful when conversational responses are the main requirement. A rule-based workflow is useful for predictable tasks with clearly defined conditions. An AI agent is useful when a task requires flexible understanding, controlled access to data, tool usage, and multiple steps.