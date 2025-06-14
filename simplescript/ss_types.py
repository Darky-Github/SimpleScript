from enum import Enum

class TokenType(Enum):
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    TYPE = "TYPE"
    OPERATOR = "OPERATOR"
    STRING = "STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    CHARACTER = "CHARACTER"
    SYMBOL = "SYMBOL"
    ASSIGN = "ASSIGN"
    EOF = "EOF"

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type.name}:{self.value}"
