# Coder Agent

An AI-powered Python coding agent built with **CrewAI** and **Groq**.

The agent receives a programming assignment, writes a Python solution inside a dedicated sandbox directory, executes the generated program, checks the output, and returns a summary of the work and final result.

## Overview

The **Coder Agent** is designed to automate simple Python development tasks through an AI agent workflow.

Instead of directly generating code in the chat, the agent works through sandbox tools that allow it to:

1. Understand the given programming assignment.
2. Create a Python file inside the sandbox directory.
3. Run the generated Python program.
4. Inspect the execution result.
5. Provide a summary of the implementation and final result.

The project uses **CrewAI** to define and execute the agent workflow and **Groq** as the LLM provider.

## Architecture

```text
                    ┌──────────────────────┐
                    │   Programming Task   │
                    │     {assignment}      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Coder Agent      │
                    │    Python Developer  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Sandbox Tools     │
                    │                      │
                    │  Write Python File   │
                    │  Run Python Code     │
                    │  Check Output        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Execution Result   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    solution.md       │
                    │   Final Summary      │
                    └──────────────────────┘
```

## Features

- AI-powered Python code generation
- Sandbox-based code execution
- Automatic execution of generated Python programs
- Output inspection
- Sequential CrewAI workflow
- Groq LLM integration
- YAML-based agent and task configuration
- Configurable programming assignments
- CLI commands for running, training, testing, and replaying the crew

## Tech Stack

- **Python**
- **CrewAI 1.9.3**
- **CrewAI Tools 0.76.0**
- **Groq**
- **GPT-OSS 120B**
- **LiteLLM**
- **uv**
- **LanceDB**
- **ONNX Runtime**

## Project Structure

```text
coder/
├── src/
│   └── coder/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── sandbox_tools.py
│       │   └── custom_tool.py
│       │
│       ├── __init__.py
│       ├── crew.py
│       └── main.py
│
├── output/
│   └── solution.md
│
├── pyproject.toml
└── README.md
```

## Agent Configuration

The agent is defined as a Python Developer:

```yaml
coder:
  role: >
    Python Developer

  goal: >
    You use your sandbox tools to achieve this assignment: {assignment}
    Write a python file in the sandbox directory, then run it and check the output.

  backstory: >
    You're a seasoned python developer with a knack for writing clean, efficient code.

  llm: groq/openai/gpt-oss-120b
```

The agent is provided with the sandbox tools defined in:

```text
src/coder/tools/sandbox_tools.py
```

## Task Configuration

The main task receives the programming assignment dynamically through the `{assignment}` variable.

```yaml
coding_task:
  description: >
    Use your sandbox tools to write and run python code to achieve this: {assignment}

  expected_output: >
    A summary of what you did to achieve the assignment and the final result.

  agent: coder

  output_file: output/solution.md
```

This allows the same agent to solve different Python programming assignments without changing the CrewAI workflow.

## Crew Workflow

The project contains a single agent and a single task.

The crew uses a sequential process:

```python
Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
)
```

The workflow is:

```text
Assignment
    ↓
Coder Agent
    ↓
Sandbox Tools
    ↓
Generate Python File
    ↓
Execute Python File
    ↓
Check Output
    ↓
Generate solution.md
```

## Example Assignment

The current example assignment is:

```text
Write a python program to calculate the first 1,000,000 terms
of this series, multiplying the total by 4:

1 - 1/3 + 1/5 - 1/7 + ...
```

This is the **Leibniz formula for π**:

```text
π ≈ 4 × (1 - 1/3 + 1/5 - 1/7 + ...)
```

The agent is expected to create and execute a Python solution rather than simply provide the code.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd coder
```

### 2. Create the environment

Using `uv`:

```bash
uv venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
uv sync
```

The project currently uses:

```toml
crewai==1.9.3
crewai-tools==0.76.0
lancedb==0.14.0
litellm>=1.75.3
onnxruntime==1.23.2
```

## Environment Variables

The project uses an LLM through Groq/LiteLLM.

Create a `.env` file and configure your API key according to your CrewAI/LiteLLM setup.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit API keys or other secrets to Git.

## Running the Agent

The main entry point is:

```bash
uv run run_crew
```

or:

```bash
uv run coder
```

The CrewAI workflow receives the assignment defined in:

```text
src/coder/main.py
```

For example:

```python
assignment = """
Write a python program to calculate the first 1,000,000 terms
of this series, multiplying the total by 4:
1 - 1/3 + 1/5 - 1/7 + ...
"""
```

The agent then executes the task through the sandbox tools.

## Output

After completing the assignment, the task writes its final response to:

```text
output/solution.md
```

The output contains a summary of:

- What the agent implemented
- How the assignment was solved
- The execution result
- The final answer

## CLI Commands

The project exposes several commands through `pyproject.toml`.

### Run

```bash
uv run run_crew
```

Runs the CrewAI workflow.

### Train

```bash
uv run train <iterations> <filename>
```

Trains the crew for the specified number of iterations.

### Replay

```bash
uv run replay <task_id>
```

Replays a previous crew execution from a specific task.

### Test

```bash
uv run test <iterations> <evaluation_llm>
```

Runs CrewAI evaluation/testing.

### Trigger

```bash
uv run run_with_trigger '<json-payload>'
```

Runs the crew using a trigger payload.

## Sandbox Tools

The agent receives custom sandbox tools through:

```python
from .tools.sandbox_tools import sandbox_tools
```

These tools provide the agent with the ability to work with files and execute Python code within the project's sandbox environment.

This creates an execution loop:

```text
Think
  ↓
Use Sandbox Tool
  ↓
Write Code
  ↓
Execute Code
  ↓
Inspect Result
  ↓
Fix if Necessary
  ↓
Return Final Result
```

## Why Sandbox Execution?

Generating code is not enough for a coding agent.

The sandbox-based workflow allows the agent to validate its solution by actually executing the generated Python program.

This makes the workflow closer to how a developer works:

```text
Problem
  ↓
Implement
  ↓
Run
  ↓
Observe
  ↓
Debug
  ↓
Verify
```

## Configuration

Agent and task behavior are separated from the Python implementation through YAML files:

```text
src/coder/config/agents.yaml
src/coder/config/tasks.yaml
```

This makes it easier to modify the agent's role, goal, backstory, task description, and expected output without changing the CrewAI implementation.

## CrewAI Implementation

The crew is defined in:

```text
src/coder/crew.py
```

The project uses CrewAI decorators:

```python
@CrewBase
@agent
@task
@crew
```

The Coder agent receives the sandbox tools:

```python
return Agent(
    config=self.agents_config['coder'],
    verbose=True,
    tools=sandbox_tools
)
```

The task is then connected to the agent through the CrewAI configuration.

## Current Limitations

- The project currently focuses on Python programming assignments.
- Code execution depends on the available sandbox environment.
- The generated solution depends on the capabilities of the selected LLM.
- The current workflow contains one primary coding agent.
- The sandbox should be treated as an execution environment and should not be given access to sensitive files or credentials.

## Future Improvements

Potential improvements include:

- Add automated test generation
- Add automatic debugging and retry loops
- Add code quality checks
- Add Python linting and formatting
- Add unit-test execution after code generation
- Add structured execution logs
- Add multiple specialized coding agents
- Add a reviewer/debugger agent
- Add persistent project context
- Add support for additional programming languages
- Add stronger sandbox isolation
- Add automatic validation of generated files

## Example Workflow

Given:

```text
Assignment:
Calculate the first 1,000,000 terms of the Leibniz series
and multiply the result by 4.
```

The Coder Agent should:

```text
1. Understand the mathematical requirement
        ↓
2. Create a Python file in sandbox/
        ↓
3. Implement the calculation
        ↓
4. Execute the Python file
        ↓
5. Inspect the output
        ↓
6. Fix the implementation if required
        ↓
7. Report the final result
        ↓
8. Save the summary to output/solution.md
```

## License

This project is for educational and development purposes.