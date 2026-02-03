import re

TOKEN_PATTERN = r"[A-Za-z_][A-Za-z0-9_]*|==|!=|<=|>=|[+\-*/%=<>{}();]"

def tokenize_code(code: str):
    """
    Tokenizes source code into lexical tokens
    """
    tokens = re.findall(TOKEN_PATTERN, code)
    return tokens
