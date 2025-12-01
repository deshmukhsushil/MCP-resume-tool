
🌟 Brief Description
The MCP Resume Tool is a simple utility that leverages Multi-Context Processing (MCP) to answer job application questions.

It works by loading your resume (usually a PDF or similar document) as the central context for a Large Language Model (LLM). This allows the LLM to generate highly relevant, personalized answers to common application prompts using the specific details from your professional history.

🚀 Local Installation and Usage
Follow these steps to get the tool running on your local machine.

1. Prerequisites
You will need the following installed:

Python 3.8+

Git

An LLM API Key (e.g., a Gemini API Key or similar, depending on the LLM configuration in the script).

2. Setup
Clone the Repository: Open your terminal or command prompt and run:

Bash

git clone https://github.com/deshmukhsushil/MCP-resume-tool.git
MCP-resume-tool
Create a Virtual Environment (Recommended):

Bash

# Create the environment
python -m venv .venv
# Activate the environment (Linux/macOS)
source .venv/bin/activate
# Activate the environment (Windows PowerShell)
# .venv\Scripts\Activate.ps1
Install Dependencies: Install all required packages listed in the pyproject.toml file:

Bash

pip install .
Set Your API Key: The tool requires your LLM API key to run. Set it as an environment variable (replace YOUR_API_KEY_HERE with your actual key):

Bash

# Example (replace LLM_API_KEY with the variable name required by main.py)
export LLM_API_KEY="YOUR_API_KEY_HERE"
3. Run the Tool
Make sure your resume file (e.g., my_resume.pdf) is ready.

Execute the main script:

Bash

python main.py
The script will prompt you to enter the path to your resume and the job application question you want the LLM to answer.


