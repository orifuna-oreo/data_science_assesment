
# **Open University Learning Analytics - Student Performance Prediction**  

## **Project Overview**  
This project analyzes student performance using data from the **Open University Learning Analytics Dataset (OULAD)**. The objective is to predict student outcomes (`final_result`) based on **pass rates** and **weighted grades** using three different machine learning models:  

- **Random Forest Classifier**  
- **Logistic Regression**  
- **Linear Discriminant Analysis (LDA)**  

The analysis involves **data preparation, model training, evaluation, and visualization** to understand key factors influencing student success.  

---

## **Dataset Description**  
The dataset consists of multiple CSV files related to student engagement, assessments, and demographics. The key files used in this project include:  

- `studentInfo.csv` – Contains student demographic data.  
- `studentAssessment.csv` – Records student scores on assessments.  
- `studentVle.csv` – Logs student interactions with the Virtual Learning Environment (VLE).  
- `assessments.csv` – Provides assessment details.  

### **Key Features Used for Prediction**  
1. **Pass Rate (`pass_rate`)** – The percentage of completed assessments that a student has passed.  
2. **Weighted Grade (`weighted_grade`)** – The overall performance score adjusted by assessment weight.  
3. **Final Result (`final_result`)** – The target variable with categories: `Withdrawn`, `Fail`, `Pass`, `Distinction`.  

---

## **Data Preparation & Cleaning**  
1. **Handling Missing Values**  
   - Used **forward fill** to replace missing values where applicable.  
2. **Removing Duplicates**  
   - Eliminated duplicate records for consistency.  
3. **Merging Relevant Datasets**  
   - Combined `studentAssessment` with `assessments` and then merged it with `studentInfo` to create a unified dataset.  
4. **Feature Engineering**  
   - Mapped categorical target values to numerical labels (`0 = Withdrawn`, `1 = Fail`, `2 = Pass`, `3 = Distinction`).  
   - Selected **pass rate** and **weighted grade** as the primary predictive features.  

---

## **Machine Learning Models Used**  

-  **Random Forest** - Handles non-linearity well, robust to noise. Can be computationally expensive.     
- **Logistic Regression** - Simple, interpretable, good for binary cases.Assumes linear relationships.
- **Linear Discriminant Analysis (LDA)**-  Reduces dimensionality, effective for classification. Assumes normality of data distribution.

---

## **Model Evaluation**  
The models were evaluated based on the following metrics:  
- **Accuracy** – Overall correctness of predictions.  
- **Precision & Recall** – Measures for identifying at-risk students.  
- **F1-Score** – Balances precision and recall.  

**Summary of Results:**  
- **Random Forest** achieved the highest accuracy but lacked interpretability.  
- **Logistic Regression** provided clear insights but had lower predictive power.  
- **LDA** performed well in distinguishing student categories but required assumptions on data distribution.  

---

## **Key Findings & Insights**  
### **Technical Takeaways:**  
1. Students with **higher pass rates** and **weighted grades** are more likely to succeed.  
2. **Random Forest** was the most accurate, while **Logistic Regression** was the most interpretable.  
3. **LDA** effectively distinguished student categories but was sensitive to data assumptions.  

### **Actionable Insights (For Educators & Admins):**  
✔️ **Support Low-Performing Students** – Identify students with low pass rates early and offer targeted support.  
✔️ **Optimize Course Content** – Improve engagement with students struggling in key subjects.  
✔️ **Use Predictive Models for Early Intervention** – Flag at-risk students for additional guidance.  

---

## **How to Reproduce This Analysis**  
### **Prerequisites**  
Ensure you have the following Python libraries installed:  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
### **Steps to Run the Project**  
1. Place the dataset files in the project directory.  
2. Run the Python script to clean the data, train models, and generate results:  
   ```bash
   python analysis_script.py
   ```
3. Review the output, including accuracy scores, classification reports, and visualizations.  

---

## **Next Steps & Future Improvements**  
🚀 **Feature Expansion:** Include more engagement metrics (e.g., VLE interactions) for better predictions.  
📊 **Advanced Models:** Test gradient boosting methods (e.g., XGBoost) for performance improvements.  
🔍 **Explainability:** Use SHAP values to enhance interpretability of model predictions.  

---

## **Contributors**  
- **[Orifuna Nemusombori]** – Data Analysis, Machine Learning, Report Writing  