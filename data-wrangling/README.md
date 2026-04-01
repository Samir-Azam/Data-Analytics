# 📊 Data Wrangling Project – E-commerce Customer Behavior

## 📌 Overview

This project focuses on cleaning and preparing raw e-commerce customer behavior data for analysis.
The dataset contains customer demographics, shopping behavior, and preferences.

---

## 🎯 Objectives

* Understand raw dataset structure
* Identify data quality issues
* Clean and transform data
* Prepare dataset for analysis

---

## 🗂️ Project Structure

```
data-wrangling/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── scripts/
├── reports/
│
├── README.md
├── requirements.txt
```

---

## ⚙️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 🔍 Data Issues Identified

* Missing values in multiple columns
* Irrelevant/sparse columns
* Inconsistent column names
* Incorrect data types

---

## 🧹 Data Cleaning Steps

* Dropped highly missing/irrelevant columns
* Renamed columns for clarity
* Handled missing values
* Converted timestamp to datetime
* Removed duplicate records

---

## 📦 Output

* Clean dataset: `data/processed/cleaned_data.csv`
* Data quality report available

---

## 🚀 How to Run

```bash
# Activate environment
source venv/Scripts/activate

# Run cleaning script
python scripts/data_cleaning.py
```

---

## 💡 Key Learnings

* Real-world data is messy and requires preprocessing
* Data cleaning is a crucial step in analytics pipelines
* Structured workflows improve reproducibility

---

## 📌 Future Improvements

* Add visualization dashboard
* Perform exploratory data analysis
* Build predictive models

---
