from crewai import Agent # pyright: ignore[reportMissingImports]

ollama_llm = "ollama/mistral"

developer = Agent(
        role="Software Engineer",
        goal="Fix bugs in code",
        backstory="Expert developer",
        llm=ollama_llm,
        verbose=True,
    )