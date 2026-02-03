import re

def remove_comments(code: str) -> str:
    """
    Removes single-line and multi-line comments
    Supports Python, C, Java style comments
    """
    code = re.sub(r'#.*', '', code)                 # Python comments
    code = re.sub(r'//.*', '', code)                # C/Java single-line
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)      # C/Java multi-line
    return code


def normalize_whitespace(code: str) -> str:
    """
    Normalizes whitespace for consistent analysis
    """
    code = re.sub(r'\s+', ' ', code)
    return code.strip()


def clean_code(code: str) -> str:
    """
    Full preprocessing pipeline
    """
    code = remove_comments(code)
    code = normalize_whitespace(code)
    return code
