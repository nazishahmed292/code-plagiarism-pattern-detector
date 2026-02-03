import pandas as pd

def validate_similarity(similarity_csv, cheating_csv, threshold=0.8):
    sim_df = pd.read_csv(similarity_csv)
    cheat_df = pd.read_csv(cheating_csv)

    # Normalize column names
    sim_df.columns = ["file1", "file2", "similarity"]
    cheat_df.columns = ["file1", "file2", "label"]

    # Prediction based on threshold
    sim_df["prediction"] = (sim_df["similarity"] >= threshold).astype(int)

    # Merge with ground truth
    merged = pd.merge(
        sim_df,
        cheat_df,
        on=["file1", "file2"],
        how="inner"
    )

    # Metrics
    tp = ((merged["prediction"] == 1) & (merged["label"] == 1)).sum()
    fp = ((merged["prediction"] == 1) & (merged["label"] == 0)).sum()
    fn = ((merged["prediction"] == 0) & (merged["label"] == 1)).sum()

    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0

    summary = {
        "Threshold": threshold,
        "Precision": round(precision, 3),
        "Recall": round(recall, 3),
        "F1 Score": round(f1, 3)
    }

    summary_df = pd.DataFrame([summary])
    summary_df.to_csv("results/validation_results.csv", index=False)

    print("\nValidation Metrics")
    print(summary_df)
