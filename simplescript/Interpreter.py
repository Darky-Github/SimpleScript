from utils import process_string
from types import TokenType

GLOBAL_SCOPE = {}

def interpret(tokens):
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        
        # Handle: say "text"
        if tok.type == TokenType.KEYWORD and tok.value == "say":
            next_tok = tokens[i + 1]
            
            if next_tok.type == TokenType.STRING:
                print(process_string(next_tok.value))
                i += 2
            elif next_tok.type == TokenType.IDENTIFIER:
                if next_tok.value in GLOBAL_SCOPE:
                    print(GLOBAL_SCOPE[next_tok.value])
                else:
                    print(f"Undefined variable: {next_tok.value}")
                i += 2
            elif next_tok.type == TokenType.IDENTIFIER and tokens[i + 2].value == "is" and tokens[i + 3].value == "ask":
                var_name = next_tok.value
                prompt = tokens[i + 4].value
                user_input = input(process_string(prompt))
                GLOBAL_SCOPE[var_name] = user_input
                print(user_input)
                i += 5
            else:
                print("Syntax error in say statement.")
                i += 1

        # Handle: type name is value
        elif tok.type == TokenType.TYPE:
            var_type = tok.value
            name_tok = tokens[i + 1]
            assign_tok = tokens[i + 2]
            val_tok = tokens[i + 3]
            if assign_tok.value == "is":
                value = val_tok.value
                if var_type == "int":
                    value = int(value)
                elif var_type == "doub":
                    value = float(value)
                elif var_type == "bool":
                    value = bool(value)
                elif var_type == "str":
                    value = process_string(value)
                elif var_type == "char":
                    value = str(value)
                GLOBAL_SCOPE[name_tok.value] = value
                i += 4
            else:
                print("Expected 'is' in variable declaration.")
                i += 1

        # Handle: reassignment name is value
        elif tok.type == TokenType.IDENTIFIER and tokens[i + 1].value == "is":
            var_name = tok.value
            new_value = tokens[i + 2].value
            GLOBAL_SCOPE[var_name] = new_value
            i += 3

        else:
            i += 1
