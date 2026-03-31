from crewai import Agent, Task, Crew  # pyright: ignore[reportMissingImports]
from agents.qa import qa, ollama_llm
from agents.developer import developer

ollama_llm1 = "ollama/llama3"
ollama_llm = "ollama/mistral"


def run_crew(code_content):

    analyze_task = Task(
        description=f"""
    You are strictly identifying problem and goal in a code base.
    
    RULES:
    - Output must be ONLY a valid Python Code
    - Exclude explanation that will cause confusion or outside the code.
    - Do not use uncertain libraries that are not in the code base.
    - Only modify parts that are necessary to solve the problem.
    - If problem is unclear and cannot be solve identify it and list it as a problem that is beyond your capacity.

    PROCESS:
    - Identify the problem
    - Identify the goal
    - Identify the issue
    - Add comment on problems and issues in the code you cannot solve.

    EXAMPLE:
    - Input code:
        import math

def factor_trinomial(a, b, c):
    try:
        # Only handle simple integer factorization
        if a == 0:
            return "# Not a trinomial"

        # Discriminant
        D = b*b - 4*a*c

        # If negative or not a perfect square → too complex
        if D < 0:
            return "# Cannot solve: complex roots"

        sqrt_D = int(math.isqrt(D))
        if sqrt_D * sqrt_D != D:
            return "# Cannot solve: non-factorable over integers"

        # Roots
        x1 = (-b + sqrt_D) // (2*a)
        x2 = (-b - sqrt_D) // (2*a)

        # Check if clean integer roots
        if (2*a*x1 != -b + sqrt_D) or (2*a*x2 != -b - sqrt_D):
            return "# Cannot solve: non-integer roots"

        return f"(x - (x1))(x - (x2))" # type: ignore

    except Exception:
        return "# Unable to process this trinomial"
    
    - Output Code:
        def process_trinomial(a, b, c):
    result = factor_trinomial(a, b, c)

    if result.startswith("#"):
        return result  # return failure message

    return f"Factored form: result"

    - Execution of sample code:
    print(process_trinomial(1, -5, 6))
    # → Factored form: (x - 2)(x - 3)

    print(process_trinomial(1, 2, 5))
    # → # Cannot solve: complex roots

    print(process_trinomial(2, 3, 1))
    # → Factored form: (x - -1)(x - -0.5) OR fallback depending on strictness
        
    ANALYZE THIS CODE:
    {code_content}

    """,
        expected_output="List of issues to be sovled and facts that are helpful to the problem.",
        agent=developer,
    )

    fix_task = Task(
        description=f"""
You are a strict Python code fixer.

RULES:
- Output ONLY valid Python code
- Do NOT include explanations outside the code
- Do NOT hallucinate missing functions or libraries
- Only modify what is necessary
- If import is needed to solve problem, only use necessary imports
- If something is unclear, add a Python comment instead of guessing

PROCESS:
1. Identify the bug
2. Fix the bug
3. Add comments explaining the fix

EXAMPLE:

Input:
def add(a, b):
    return a - b

Output:
def add(a, b):
    # Fixed incorrect operator
    return a + b

---

Now fix this code:

{code_content}
""",
        expected_output="Corrected code that solved the problem anaylzed in python code.",
        agent=developer,
    )

    test_task = Task(
        description="Validate the corrected code from the previous task and ensure it works. Return the final validated code. Add test cases in any possble way the cases can be the following: 1. Expected Functionality 2. Edge Cases 3. Error Handling. 4. Maintainability based on best practices in a software test life cycle",
        expected_output="Final validated code",
        agent=qa,
    )

    crew = Crew(
        agents=[developer, qa], tasks=[analyze_task, fix_task, test_task], verbose=True
    )

    result = crew.kickoff()
    return str(result)
