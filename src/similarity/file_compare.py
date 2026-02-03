import os
import pandas as pd
from src.preprocessing.clean_code import clean_code
from src.preprocessing.tokenize import tokenize_code
from src.similarity.vectorize import build_frequency_vector
from src.similarity.similarity_score import cosine_similarity

def read_code_files(folder_path):
    files = {}
    for file in os.listdir(folder_path):
        if file.endswith((".c", ".py", ".java")):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                files[file] = f.read()
    return files

def compare_all(folder_path):
    files = read_code_files(folder_path)
    vectors = {}

    for name, code in files.items():
        cleaned = clean_code(code)
        tokens = tokenize_code(cleaned)
        vectors[name] = build_frequency_vector(tokens)

    results = []
    names = list(vectors.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            f1, f2 = names[i], names[j]
            score = cosine_similarity(vectors[f1], vectors[f2])
            results.append({
                "File 1": f1,
                "File 2": f2,
                "Similarity Score": round(score, 3)
            })

    return pd.DataFrame(results)
