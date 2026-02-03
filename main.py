from src.preprocessing.clean_code import clean_code
from src.preprocessing.tokenize import tokenize_code
from src.similarity.vectorize import build_frequency_vector
from src.similarity.similarity_score import cosine_similarity

def analyze(code1, code2):
    c1 = build_frequency_vector(tokenize_code(clean_code(code1)))
    c2 = build_frequency_vector(tokenize_code(clean_code(code2)))
    return cosine_similarity(c1, c2)

def main():
    code_a = """
    for(int i=0;i<n;i++){
        sum += i;
    }
    """

    code_b = """
    for(int j=0;j<n;j++){
        total = total + j;
    }
    """

    score = analyze(code_a, code_b)
    print(f"Similarity Score: {score:.2f}")

if __name__ == "__main__":
    main()
