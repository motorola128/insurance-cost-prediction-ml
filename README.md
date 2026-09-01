# ACME Insurance — Medical Charges Prediction

## 📌 Project Overview

**ACME Insurance — Medical Charges Prediction** is a machine learning project that predicts an individual's **medical insurance charges** based on demographic, lifestyle, and health-related attributes.

The project focuses on building a complete machine learning workflow — from **data exploration and preprocessing to model training, evaluation, and prediction on new customer data**.

The goal is to help an insurance company estimate expected medical expenses and understand which factors have the greatest influence on insurance costs.

---

## 🎯 Business Problem

Insurance companies need to estimate potential healthcare costs when pricing insurance policies and assessing customer risk.

The objective of this project is to answer:

> **"Given a customer's demographic and health-related information, what medical insurance charge can we expect?"**

The model uses information such as:

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Residential region

to predict the customer's **medical insurance charges**.

---

## 📊 Dataset

The project uses a medical insurance dataset containing customer-level information and their corresponding medical charges.

### Features

| Feature    | Description                                 |
| ---------- | ------------------------------------------- |
| `age`      | Age of the individual                       |
| `sex`      | Gender of the individual                    |
| `bmi`      | Body Mass Index                             |
| `children` | Number of dependents/children               |
| `smoker`   | Whether the individual is a smoker          |
| `region`   | Residential region                          |
| `charges`  | Medical insurance charges — target variable |

### Target Variable

```text
charges
```

This is a **regression problem** because the target is a continuous numerical value.

---

## 🔎 Exploratory Data Analysis

The exploratory analysis examined:

* Distribution of medical charges
* Age and BMI distributions
* Relationship between smoking status and medical charges
* Relationship between BMI and charges
* Impact of age on insurance costs
* Regional differences
* Correlations between numerical variables
* Potential outliers
* Skewness of the target variable

One important observation from the analysis was that **medical charges are positively skewed**, with a relatively small number of customers having very high medical expenses.

This was considered during the preprocessing and modeling stage.

---

## 🛠️ Machine Learning Workflow

The project follows a standard end-to-end machine learning workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Analysis
     ↓
Data Preprocessing
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Selection
     ↓
Save Trained Model
     ↓
Prediction Function
     ↓
Predict Charges for New Customers
```

---

## 🧹 Data Preprocessing

The preprocessing stage included:

* Checking missing values
* Checking duplicate records
* Identifying numerical and categorical features
* Encoding categorical variables
* Analyzing outliers
* Examining feature distributions
* Preparing features for machine learning
* Splitting the dataset into training and testing sets

Categorical variables such as `sex`, `smoker`, and `region` were converted into machine-readable numerical representations before model training.

---

## 🤖 Machine Learning Model

This project treats medical charge prediction as a **supervised regression problem**.

The trained model learns the relationship between customer characteristics and historical medical charges.

Model performance was evaluated using appropriate regression metrics such as:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

### Why multiple metrics?

Using multiple evaluation metrics provides a better understanding of model performance.

For example:

* **MAE** shows the average absolute prediction error.
* **RMSE** gives greater importance to large prediction errors.
* **R²** indicates how much of the variation in medical charges is explained by the model.

---

## 💾 Saved Model

After training, the final model was saved as a `.pkl` file using `joblib`.

```text
insurance_charge_model.pkl
```

This allows the trained model to be reused without retraining it every time a prediction is required.

---

## 🔮 Prediction Function

A reusable prediction function was created so that the trained model can make predictions for new customers.

Example:

```python
from predict import predict_charges

predicted_charge = predict_charges(
    age=35,
    sex="male",
    bmi=28.5,
    children=2,
    smoker="no",
    region="southwest"
)

print(predicted_charge)
```

Example output:

```text
Predicted Medical Charges: $XXXX.XX
```

The prediction function separates the **model inference logic** from the exploratory/training notebooks, making the model easier to reuse in applications or APIs.

---

## 📁 Project Structure

```text
ACME-Insurance/
│
├── notebooks/
│   ├── 01_exploration_and_experiments.ipynb
│   └── medical_insurance_cost_prediction_cleaned.ipynb
│
├── models/
│   └── insurance_charge_model.pkl
│
├── reports/
│   ├── medical_insurance_stakeholder_report.docx
│   ├── medical_insurance_technical_report.docx
│   └── medical_insurance_eda_report.docx
│
├── src/
│   └── predict.py
│
├── README.md

```

> The original dataset is not included if it is subject to dataset licensing or repository-size limitations. Instructions for obtaining the dataset can be provided separately.

---

## ⚙️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* plotly

### Machine Learning

* Scikit-learn

### Model Persistence

* Joblib

### Development Environment

* Google colab

---

## 🚀 How to Run the Project

Follow the steps below to set up and run the ACME Insurance Medical Charges Prediction project locally.

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd ACME-Insurance
```

### 2. Create a Virtual Environment

Creating a virtual environment keeps the project's dependencies isolated from other Python projects.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

Install the required Python packages:

```bash
pip install pandas numpy scikit-learn joblib
```

### 4. Run the Prediction Function

The trained machine learning model is already saved in:

```text
models/
└── insurance_charge_model.pkl
```

The reusable prediction function is located in:

```text
src/
└── predict.py
```

You can import the function and make predictions for a new customer:

```python
from src.predict import predict_charges

predicted_charge = predict_charges(
    age=35,
    sex="male",
    bmi=28.5,
    children=2,
    smoker="no",
    region="southwest"
)

print(f"Predicted Medical Charges: ${predicted_charge:,.2f}")
```

### 5. Explore the Notebooks

The repository contains two notebooks:

#### `01_exploration_and_experiments.ipynb`

This notebook contains the initial:

* Data exploration
* Data analysis
* Visualizations
* Experiments
* Model experimentation

#### `medical_insurance_cost_prediction_cleaned.ipynb`

This notebook contains the cleaned and organized machine learning workflow, including:

* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Final model development

You can open the notebooks using Jupyter:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```
## 📄 Project Reports

The `reports/` directory contains three documents covering different aspects of the project:

- **Medical Insurance EDA Report**  
  Documents the exploratory data analysis, including data distributions, relationships between variables, outlier analysis, and key findings from the dataset.

- **Medical Insurance Technical Report**  
  Provides a detailed technical overview of the machine learning workflow, including data preprocessing, feature engineering, model development, evaluation, and prediction.

- **Medical Insurance Stakeholder Report**  
  Presents the project findings from a business perspective, focusing on key insights, factors influencing medical insurance charges, and how the analysis can support insurance-related decision-making.

### 📂 Reports Directory

```text
reports/
├── medical_insurance_stakeholder_report.docx
├── medical_insurance_technical_report.docx
└── medical_insurance_eda_report.docx
```
### 📌 Important

The repository already contains the trained model (`insurance_charge_model.pkl`), so **you do not need to retrain the model to make predictions**.

If you only want to use the model for prediction, you can directly use the `predict_charges()` function from `src/predict.py`.

If you want to understand how the model was developed, explored, and evaluated, run the notebooks in the `notebooks/` directory.



### 📈 Key Insights

The exploratory data analysis identified several important factors associated with medical insurance charges:

* **Smoking Status:** Smokers tend to have substantially higher medical insurance charges compared with non-smokers.
* **Age:** Medical charges generally increase with age, although the relationship is not strictly linear.
* **BMI:** BMI is associated with medical expenses, particularly when considered alongside other customer characteristics.
* **Combined Effects:** Insurance charges are influenced by multiple factors simultaneously, highlighting the importance of considering interactions between demographic and health-related features.

---

## 💡 What I Learned

This project provided practical experience in:

* Performing end-to-end exploratory data analysis
* Identifying patterns and relationships in real-world data
* Handling numerical and categorical features
* Analyzing skewed target variables and outliers
* Preparing data for machine learning
* Training and evaluating regression models
* Comparing models using appropriate evaluation metrics
* Saving and reusing trained machine learning models
* Building a reusable prediction function for new data
* Structuring an ML project beyond a single notebook

---

## 🔮 Future Improvements

The project can be extended into a more complete production-oriented machine learning application by:

* Deploying the prediction model as a **FastAPI** REST API
* Building an interactive prediction interface using **Streamlit**
* Adding model explainability using **SHAP**
* Performing hyperparameter optimization
* Experimenting with additional regression algorithms
* Adding model monitoring and performance tracking
* Containerizing the application using **Docker**
* Deploying the application to a cloud platform

---

## 👨‍💻 About This Project

This project was developed as part of my **machine learning and data analytics portfolio** to demonstrate an end-to-end approach to solving a regression problem — from exploratory data analysis and model development to saving the trained model and creating a reusable prediction function.
