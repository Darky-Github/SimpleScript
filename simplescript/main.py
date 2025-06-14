from lexer import tokenize
from parser import parse
from interpreter import interpret

def run_simplescript(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    interpret(ast)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            code = file.read()
            run_simplescript(code)
    else:
        print("SimpleScript REPL. Type 'exit' to quit.")
        while True:
            try:
                line = input(">>> ")
                if line.strip().lower() == "exit":
                    break
                run_simplescript(line)
            except Exception as e:
                print(f"Error: {e}")
