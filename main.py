from src.preprocessing.clean_code import clean_code
from src.preprocessing.tokenize import tokenize_code

def main():
    sample_code = """
    // Sample loop
    for (int i = 0; i < n; i++) {
        sum += i;
    }
    """

    cleaned = clean_code(sample_code)
    tokens = tokenize_code(cleaned)

    print("CLEANED CODE:")
    print(cleaned)
    print("\nTOKENS:")
    print(tokens)

if __name__ == "__main__":
    main()
