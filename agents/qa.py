from crewai import Agent # pyright: ignore[reportMissingImports]

ollama_llm = "ollama/mistral"

qa = Agent(
        role="QA Engineer",
        goal="Validate code correctness",
        backstory="Testing expert",
        llm=ollama_llm,
        verbose=True,
    )