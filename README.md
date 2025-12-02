# 🌟 MCP Resume Tool

---

## 📝 Brief Description

The **MCP Resume Tool** is a simple utility that leverages the **Multi-Context Processing (MCP)** technique to answer job application questions.

It works by loading your **resume** (usually a PDF or similar document) as the central context for a **Large Language Model (LLM)**. This allows the LLM to generate highly relevant, personalized answers to common application prompts, drawing directly from the specific details of your professional history.

---

## 🚀 Local Installation and Usage

Follow these steps to get the tool running on your local machine.

### 1. Prerequisites

You will need the following installed:

* **Python 3.8+**
* **Git**
* An **LLM API Key** (e.g., a Gemini API Key or similar, depending on the LLM configuration in the script).

### 2. Setup

1.  **Clone the Repository:**
    Open your terminal or command prompt and run:

    ```bash
    git clone [https://github.com/deshmukhsushil/MCP-resume-tool.git](https://github.com/deshmukhsushil/MCP-resume-tool.git)
    cd MCP-resume-tool
    ```

2.  **Create a Virtual Environment (Recommended):**
    
    ```bash
    # Create the environment
    python -m venv .venv
    # Activate the environment (Linux/macOS)
    source .venv/bin/activate
    # Activate the environment (Windows PowerShell)
    # .venv\Scripts\Activate.ps1
    ```

3.  **Install Dependencies:**
    Install all required packages listed in the `pyproject.toml` file:

    ```bash
    pip install .
    ```

4.  **Set Your API Key:**
    The tool requires your LLM API key to run. Set it as an environment variable (replace `YOUR_API_KEY_HERE` with your actual key):

    ```bash
    # Example (replace LLM_API_KEY with the variable name required by main.py)
    export LLM_API_KEY="YOUR_API_KEY_HERE"
    ```
5. **Add Resume file in markdown format in the project directory**
   For Privacy, remove identification information like Name, email ID, phone number, etc. from the resume and add the rest as a markdown file [resume.md] in project directory.
   
### 3. Run the Tool

1.  Make sure your resume file (e.g., `my_resume.pdf`) is ready.
2.  Execute the main script:

    ```bash
    python main.py
    ```
3.  The script will prompt you to enter the path to your resume and the job application question you want the LLM to answer.

