import ast

def extract_code(text):
    """
    Extract only valid Python code from the LLM output.
    First tries to find code blocks marked with ```, then falls back to parsing line by line.
    """
    # Try to extract from code blocks first
    if "```" in text:
        parts = text.split("```")
        for i in range(1, len(parts), 2):  # Code blocks are between ```
            part = parts[i].strip()
            if part.startswith("python") or part.startswith("py"):
                part = part[6:].strip()  # Remove "python" or "py"
            try:
                ast.parse(part)
                return part
            except:
                continue
    
    # Fallback to line-by-line parsing
    lines = text.split("\n")
    cleaned_lines = []
    
    for line in lines:
        cleaned_lines.append(line)
        
        try:
            ast.parse("\n".join(cleaned_lines))
        except:
            cleaned_lines.pop()
            break
    return "\n".join(cleaned_lines).strip()
            