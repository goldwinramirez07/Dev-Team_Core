This project consists of two AI agents leveraging the computing capacity of Llama3 8b and Mistral 7b
**The model's performance is not measured by any metrics at all.

How to run the file model via Ollama
(on terminal)
- ollama run modelname [args] 
- python main.py
- File path to the prompt of main.py
  - Running can be continous modify the runner.py

GOAL: 
- Maximize the correct output by modifiying description, expected_output and agent attributes
- Make a functional team for low level tasks(Syntax correction, easy problems and repetitive tasks if applicable)
- Explore different small sized models (Experiment which of models works best with modified attributes mentioned above.)
- Compare and contrast input to output related to fix needed
- Make this AI team conversational between user and models via GUI


Specifications used:
.venv locked in 3.11.9 version
Ollama Version 0.19.0

any encountered error regarding pip install, crewai, langchain, ollama, langchain-ollama retry to install these dependencies via 
pip install --upgrade pip
pip install crewai langchain langchain-ollama ollama python-dotenv
