import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool

# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add your Groq API key to the .env file."
    )

# ============================================================
# GROQ LLM
# ============================================================

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=api_key
)

# ============================================================
# TOOLS
# ============================================================

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        allowed = set("0123456789+-*/().% ")

        if not all(char in allowed for char in expression):
            return "Invalid mathematical expression."

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


@tool
def get_tasks() -> str:
    """Show all saved tasks."""

    if not os.path.exists("tasks.txt"):
        return "No tasks found."

    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = file.read().strip()

    if not tasks:
        return "No tasks found."

    return tasks


@tool
def add_task(task: str) -> str:
    """Add a new task to the task list."""

    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")

    return f"Task added successfully: {task}"


@tool
def remember(fact: str) -> str:
    """Save a non-sensitive user preference or fact to memory."""

    with open("memory.txt", "a", encoding="utf-8") as file:
        file.write(fact + "\n")

    return f"I remembered: {fact}"


@tool
def get_memory() -> str:
    """Read saved user memory."""

    if not os.path.exists("memory.txt"):
        return "No memory saved."

    with open("memory.txt", "r", encoding="utf-8") as file:
        memory = file.read().strip()

    if not memory:
        return "No memory saved."

    return memory


# ============================================================
# AGENT TOOLS
# ============================================================

tools = [
    calculator,
    add_task,
    get_tasks,
    remember,
    get_memory,
]

# ============================================================
# CREATE AGENT
# ============================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a helpful personal AI agent.

Your capabilities include:

1. Normal conversation
2. Mathematical calculations
3. Creating tasks
4. Reading tasks
5. Saving non-sensitive memories
6. Reading saved memories

Rules:

- Use the calculator tool for mathematical calculations.
- Use add_task when the user asks you to create or add a task.
- Use get_tasks when the user asks to see their tasks.
- Use remember when the user explicitly asks you to remember something.
- Use get_memory when saved memory is relevant.
- Do not claim that a task or memory was saved unless the tool confirms it.
- Be concise, clear, and helpful.
"""
)

# ============================================================
# TERMINAL CHAT
# ============================================================

print("=" * 55)
print("🤖 GROQ PERSONAL AI AGENT")
print("=" * 55)
print("Model: openai/gpt-oss-120b")
print("Status: Connected to Groq")
print("Type 'exit' or 'quit' to stop.")
print("=" * 55)

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("\nAgent: Goodbye! 👋")
        break

    if not user_input:
        continue

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        print("\nAgent:", answer)

    except Exception as e:

        print("\n❌ Agent Error:")
        print(e)