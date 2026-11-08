# 📉 Predicting Customer Churn for a Telecom Company

A beginner-friendly, line-by-line annotated Python script that builds a **Logistic Regression** model to predict customer churn using a telecom dataset — covering the full ML pipeline from data loading to model evaluation.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Pipeline Walkthrough](#pipeline-walkthrough)
- [Results](#results)
- [Notes](#notes)

---

## Overview

Customer churn — when a customer stops using a service — is a critical business problem in the telecom industry. This project demonstrates a complete supervised machine learning workflow to predict which customers are likely to churn, using **Logistic Regression** as the classification algorithm.

Every line of code includes an inline comment explaining what it does and why, making this script ideal for learners and those new to applied machine learning.

---

## Dataset

The script expects a CSV file named `telecom_churn.csv` in the same directory.

**Key columns used:**

| Column | Description |
|---|---|
| `account length` | Number of days the customer has been with the provider |
| `area code` | Customer area code |
| `voice mail plan` | Whether customer has a voicemail plan (Yes/No) |
| `number vmail messages` | Number of voicemail messages |
| `total day/eve/night/intl minutes` | Usage in minutes per time period |
| `total day/eve/night/intl calls` | Number of calls per time period |
| `total day/eve/night/intl charge` | Charges per time period |
| `customer service calls` | Number of calls made to customer service |
| `churn` | **Target variable** — whether the customer churned (True/False or Yes/No) |

> The `phone number` column is dropped during preprocessing as it is a unique identifier, not a predictive feature.

---

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/telecom-churn-prediction.git
cd telecom-churn-prediction
```

2. **Install dependencies:**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
```

3. **Add your dataset:**

Place your `telecom_churn.csv` file in the root of the project directory.

---

## Usage

Run the script directly:

```bash
python Predicting_Customer_Churn_for_a_Telecom_Company_Line-By-Line_Explanation.py
```

The script will:
- Print dataset summaries to the console
- Open interactive matplotlib windows for each plot (histograms, bar graphs, pairplot, correlation heatmap)
- Print model accuracy, confusion matrix, and classification report

> **Note:** Close each plot window to allow the script to continue to the next step.

---

## Project Structure

```
telecom-churn-prediction/
│
├── telecom_churn.csv                          # Dataset (not included — add your own)
├── Predicting_Customer_Churn_for_a_Telecom_Company_Line-By-Line_Explanation.py
└── README.md
```

---

## Pipeline Walkthrough

### 1. Data Loading & Exploration
- Loads `telecom_churn.csv` into a pandas DataFrame
- Displays the first few rows, shape, data types, and summary statistics
- Checks the distribution of the target variable (`churn`)

### 2. Exploratory Data Analysis (EDA)
- **Histograms** — generated individually for every numerical feature
- **Bar graphs** — generated for every categorical feature (excluding the target)
- **Pairplot** — scatter matrix of top 5 features most correlated with churn, colored by churn status
- **Correlation Heatmap** — annotated heatmap showing pairwise correlations among numeric features

### 3. Data Preprocessing
- Converts `voice mail plan` from `Yes`/`No` strings to `1`/`0`
- Drops `phone number` (non-informative unique identifier)
- Applies one-hot encoding (`pd.get_dummies`) to remaining categorical columns, dropping the first category to avoid multicollinearity
- Converts the `churn` target column to binary integer (`0` = stayed, `1` = churned)
- Handles missing values: numeric NaNs filled with column mean; categorical NaNs filled with column mode

### 4. Feature Scaling
- Applies `StandardScaler` to normalize all features to zero mean and unit variance

### 5. Train/Test Split
- Splits data 80/20 (training/testing) using `train_test_split` with `random_state=42` for reproducibility

### 6. Class Imbalance Handling (SMOTE)
- Uses `SMOTE` (Synthetic Minority Over-sampling Technique) to balance the minority churn class
- Applied strictly to the training split (`X_train`, `y_train`) to prevent data leakage into the test set

### 7. Model Training
- Trains a `LogisticRegression` model (`max_iter=1000`) on the SMOTE-balanced training set

### 8. Model Evaluation
- **Accuracy Score** — overall proportion of correct predictions
- **Confusion Matrix** — breakdown of true/false positives and negatives
- **Classification Report** — precision, recall, and F1-score for each class

---

## Results

After running the script, output similar to the following is expected in the console:

```
Accuracy: 0.86

Confusion Matrix:
[[TN  FP]
 [FN  TP]]

Classification Report:
                                                              precision  recall  f1-score  support
Customers who did not churn (i.e., they stayed...)             ...
Customers who did churn (i.e., they left/changed...)           ...
```

> Exact values will vary based on the dataset used.

---

## Notes

- This script is designed for **educational purposes** — every line is annotated with a plain-English explanation.
- Interactive plot windows will block script execution until closed. This is expected behavior with `plt.show()`.
- To save plots instead of displaying them interactively, replace `plt.show()` with `plt.savefig('filename.png')` followed by `plt.close()` (hints for this are included as comments in the script).
- Logistic Regression is used as a baseline model. For improved performance, consider experimenting with Random Forest, Gradient Boosting (XGBoost), or neural network approaches.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
