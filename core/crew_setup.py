from crewai import Agent, Task, Crew # pyright: ignore[reportMissingImports]
from agents.qa import qa
from agents.developer import developer

ollama_llm1 = "ollama/llama3"
ollama_llm = "ollama/mistral"


def run_crew(code_content):

    analyze_task = Task(
    description=f"Analyze this code and list all issues:\n{code_content} \n Identify facts of the current codebase and compare and contrast with best practices. If multiple solutions are present pick the one that is mostly leaning towards good software engineering practices.",
    expected_output="List of bugs and issues",
    agent=developer
    )

    fix_task = Task(
        description=f"Fix the issues identified in the previous analysis for this code:\n{code_content}\nReturn only the corrected code. Please be mindful of terminlogies and variable names. Do not change them unless necessary. Refer to best practices of software engineering and solve the problem as close as the anaylzed task as possible. Closest processes and best practices should be followed. If there are multiple solutions, pick the one that is mostly leaning towards good software engineering practices.",
        expected_output="Corrected code",
        agent=developer,
    )
    
    test_task = Task(
        description="Validate the corrected code from the previous task and ensure it works. Return the final validated code. Add test cases in any possble way the cases can be the following: 1. Expected Functionality 2. Edge Cases 3. Error Handling. 4. Maintainability based on best practices in a software test life cycle",
        expected_output="Final validated code",
        agent=qa,
    )

    crew = Crew(agents=[developer, qa], tasks=[analyze_task, fix_task, test_task], verbose=True)

    result = crew.kickoff()
    return str(result)
