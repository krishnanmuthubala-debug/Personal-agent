# Simple LangChain Personal Life Agent

A beginner-friendly Agentic AI project using Python, LangChain and Google Gemini.

## Features

- Uses LangChain Agent
- Uses Gemini 2.5 Flash
- Understands a user's goal
- Breaks the goal into actionable steps
- Creates a practical schedule
- Runs in the VS Code terminal
- No frontend or database, so it is easy to learn

## Requirements

- Python 3.10+
- VS Code
- A Google Gemini API key

## Setup in VS Code

### 1. Open the project folder

Open `LangChain_Simple_Personal_Agent` in VS Code.

### 2. Open Terminal

Go to:

Terminal > New Terminal

### 3. Create virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate it

```bash
venv\Scripts\activate
```

If `python` does not work, try:

```bash
py -m venv venv
venv\Scripts\activate
```

### 5. Install packages

```bash
pip install -r requirements.txt
```

### 6. Create the .env file

Copy `.env.example` and rename the copy to:

```text
.env
```

Open `.env` and replace:

```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

with your actual Gemini API key.

Do not share the API key or upload `.env` to GitHub.

### 7. Run

```bash
python app.py
```

## Example

You:

```text
I have exams in 10 days. Create a study plan for Python, DBMS and AI.
```

The LangChain agent will generate a practical plan.

Another example:

```text
I want to become a Python developer in 3 months. Give me a weekly roadmap.
```

Type:

```text
exit
```

to stop the program.

## Architecture

```text
User
  |
  v
LangChain Agent
  |
  v
Gemini 2.5 Flash
  |
  v
Reasoning / Planning
  |
  v
Action Plan
```

## Important

This is intentionally a simple LangChain agent for learning and demonstration.

A next version can add real tools such as:
- Calculator
- Web search
- Calendar
- Task database
- Long-term memory
- Email notifications
