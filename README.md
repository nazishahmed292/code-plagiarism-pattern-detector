# Code Plagiarism Pattern Detector

A scalable, token-based code similarity analysis system designed to detect plagiarism patterns across large collections of source code files. The project focuses on statistical similarity detection and validation using real-world labeled datasets.

---

## Overview

This project implements a code similarity detection pipeline that analyzes source code submissions and computes similarity scores using token frequency vectors and cosine similarity. The system is evaluated against a labeled plagiarism dataset to validate its effectiveness.

The goal is not to determine plagiarism intent, but to identify structural and lexical similarity patterns that may indicate potential academic dishonesty.

---

## Key Features

- Language-agnostic preprocessing (Python, C, Java)
- Comment removal and whitespace normalization
- Tokenization and frequency-based feature extraction
- Pairwise cosine similarity computation
- Large-scale comparison across hundreds of files
- Validation against labeled plagiarism ground truth
- CSV-based result generation for analysis and reporting

---

## Dataset

The project uses a publicly available Kaggle dataset containing:

- Raw source code submissions (`.py`)
- Labeled cheating pairs (`cheating_dataset.csv`)
- Precomputed feature metadata (`cheating_features_dataset.csv`)

Only the raw source code files are used for similarity detection. The metadata CSVs are retained strictly for validation and result interpretation to avoid biasing the detection process.

---

## Project Structure

```text
code-plagiarism-pattern-detector/
│
├── data/
│   ├── kaggle_submissions/        # Source code files used for analysis
│   └── kaggle_metadata/           # Ground-truth labels and metadata
│
├── src/
│   ├── preprocessing/             # Code cleaning and tokenization
│   ├── similarity/                # Vectorization and similarity scoring
│   ├── evaluation/                # Validation and metrics computation
│
├── results/
│   ├── similarity_scores.csv
│   └── validation_results.csv
│
├── main.py                        # Pipeline entry point
├── requirements.txt
└── README.md
