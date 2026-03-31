from core.crew_setup import run_crew
from services.file_service import read_file, write_file
from utils.code_cleaner import extract_code
import os

def run_once(file_name):
    try:
        code = read_file(file_name)
        clean_code = run_with_retry(code)

        base_name = os.path.basename(file_name)
        output_file = f"data/output/fixed_{base_name}"

        write_file(output_file, clean_code)

        print(f"✅ Saved: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


def run_continuous():
    while True:
        file_name = input("Enter file (or exit): ")

        if file_name == "exit":
            break

        run_once(file_name)

def is_valid_python(code):
    import ast
    try:
        ast.parse(code)
        return True
    except:
        return False

def run_with_retry(code, max_attempts=3):
    for attempt in range(max_attempts):
        result = run_crew(code)
        clean_code = extract_code(result)

        if is_valid_python(clean_code):
            print(f"✅ Valid code found on attempt {attempt+1}")
            return clean_code

        print(f"❌ Invalid code on attempt {attempt+1}, retrying...")

    print("⚠️ Max attempts reached, saving best effort")
    return clean_code
