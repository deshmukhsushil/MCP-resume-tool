import os
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("AI Resume Tool")

resume = os.path.join(os.path.dirname(__file__),"resume.md")

def ensure_file():
    if not os.path.exists(resume):
        print("Please add latest resume in md file format")
        with open(resume, "w") as f:
            f.write("")

@mcp.tool()
def read_resume() -> str:
    """
    Read and return the resume file.

    Returns:
        str: Resume contents from the MD file
    """
    ensure_file()
    with open(resume, "r") as f:
        content = f.read().strip()
    return content or "No Resume yet."

@mcp.prompt()
def job_app_answer_prompt() -> str:
    """
    Generate a prompt that asks the AI to answer the copied questions, using relevant context from the resume. 
    Anything asked outside the context of this job application and resume should be returned as "this is out of context."

    Returns:
        str: A prompt string that takes a resume reference and asks to answer the copied-and-pasted job application questions.
            If no resume exists, a message will be shown indicating that.
    """
    ensure_file()
    with open(resume, "r") as f:
        content = f.read().strip()
    if not content:
        return "There is no resume yet."

    return f"Considering the resume {content} and assuming the role of this person who has this professional experience, answer the following job application questions without em-dashes, robotic language. 
            Answer in a human way, which will go undetected by AI detectors. 
            Everything should sound genuine and have a personal touch, such that it feels very well thought out and researched for every company and role for which these answers are requested. 
            Always answer in 3-4 sentences with simple words that are not hard to understand. The answer should portray clarity, confidence, and vision. 
            If anything is asked out of context of the job application and the resume, you should say this is out of scope of the MCP tool."



