import numpy as np

def cosine_similarity(vec1, vec2):
    """
    Computes cosine similarity between two frequency vectors
    """
    all_tokens = set(vec1.keys()).union(set(vec2.keys()))

    v1 = np.array([vec1.get(token, 0) for token in all_tokens])
    v2 = np.array([vec2.get(token, 0) for token in all_tokens])

    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
