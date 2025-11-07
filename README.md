# SHL Assessment Recommendation Engine

### Author: Rohan Gandhi 
**Role Applied:** Research Intern – AI Team at SHL

---

## Project Overview

This project builds an **Assessment Recommendation Engine** using SHL’s provided dataset.  
The goal is to recommend the most relevant SHL assessments for a given **job description or hiring query**, based solely on historical data mapping queries to assessment URLs.

It demonstrates the ability to:
- Understand business context (assessment recommendation)
- Apply text processing and similarity modeling
- Produce interpretable, reproducible, and automatable results

---

## Problem Statement

Given:
- A *Train-Set* containing `Query` ↔ `Assessment_url` pairs  
- A *Test-Set* containing only `Query`

The task is to predict which SHL assessment(s) best match each test query.

The final output is an **Excel file** named  
`Recommendations_Output.xlsx` containing:

| Query | Recommended_Assessment | Similarity_Score | Explanation |
|--------|------------------------|------------------|--------------|

---

## ⚙️ Technical Approach

### Step 1. Data Loading
- Extracted queries and true hyperlinks from Excel (using `openpyxl`)
- Removed duplicates and missing values

### Step 2. Text Preprocessing
- Lowercased text  
- Removed punctuation and extra spaces  

### Step 3. TF-IDF Vectorization
- Converted queries to numerical vectors using `TfidfVectorizer`
- Used unigram + bigram representation for richer context

### Step 4. Similarity Computation
- Calculated **cosine similarity** between new (test) queries and historical (train) queries
- Returned the top-3 most similar assessments per query

### Step 5. Explanation Generation
- Highlighted overlapping key terms between the query and matched assessment
- Provides interpretable output for HR decision-makers

---

## Model Interpretation

The **Similarity_Score** ranges from **0 to 1**:
- `> 0.8` → Very strong match  
- `0.5–0.8` → Moderate similarity  
- `< 0.3` → Weak or no relation  

Each recommendation includes an **Explanation** so results are human-understandable and audit-friendly.

---

## Tech Stack

| Component | Library / Tool |
|------------|----------------|
| Data Processing | `pandas`, `openpyxl` |
| Text Modeling | `scikit-learn` (TF-IDF, cosine similarity) |
| Language | Python 3.12 |
| Output Format | Excel (`.xlsx`) |
| Version Control | Git + GitHub |

---

## How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/RohanGandhi980/Assessment-Recommendation.git
   cd Assessment-Recommendation
   ```
2. Run the Engine
   ```bash
    python main.py
   ```
3. Outputs stored at
   ```bash
     Recommendations_Output.xlsx
   ```
   
