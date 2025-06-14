from types import Token, TokenType

KEYWORDS = {"say", "ask", "is", "loop", "do", "while", "if", "else", "in"}
TYPES = {"int", "doub", "str", "bool", "char"}
OPERATORS = {
    "+", "-", "*", "**", "/", "//", "#", "%", "mod", "rem", "div", "mul", "sub", "addTo",
    "is", "greater", "less", "and", "or", "not", "&&", "||", "&", "|", "!"
}
SYMBOLS = {"(", ")", "{", "}", ";", ","}

def tokenize(code):
    tokens = []
    words = code.replace("(", " ( ").replace(")", " ) ").replace("{", " { ").replace("}", " } ").split()
    
    for word in words:
        if word in KEYWORDS:
            tokens.append(Token(TokenType.KEYWORD, word))
        elif word in TYPES:
            tokens.append(Token(TokenType.TYPE, word))
        elif word in OPERATORS:
            tokens.append(Token(TokenType.OPERATOR, word))
        elif word in SYMBOLS:
            tokens.append(Token(TokenType.SYMBOL, word))
        elif word == "is":
            tokens.append(Token(TokenType.ASSIGN, word))
        elif word.startswith('"') and word.endswith('"'):
            tokens.append(Token(TokenType.STRING, word[1:-1]))
        elif word.startswith("'") and word.endswith("'") and len(word) == 3:
            tokens.append(Token(TokenType.CHARACTER, word[1]))
        elif word.isdigit():
            tokens.append(Token(TokenType.NUMBER, int(word)))
        elif word.lower() in {"true", "false"}:
            tokens.append(Token(TokenType.BOOLEAN, word.lower() == "true"))
        else:
            tokens.append(Token(TokenType.IDENTIFIER, word))
    tokens.append(Token(TokenType.EOF, None))
    return tokens
