from src.similarity.file_compare import compare_all
from src.evaluation.validate import validate_similarity

def main():
    folder = "data/kaggle_submissions"

    # Run similarity analysis
    df = compare_all(folder)
    df.to_csv("results/similarity_scores.csv", index=False)
    print("Similarity analysis complete")

    # Validate against Kaggle labels
    validate_similarity(
        similarity_csv="results/similarity_scores.csv",
        cheating_csv="data/kaggle_metadata/cheating_dataset.csv",
        threshold=0.8
    )

if __name__ == "__main__":
    main()
