
# 🎯 Student Performance Indicator - End-to-End ML Project

A complete **machine learning project pipeline** that predicts student math scores based on demographic and academic inputs. This project includes data analysis, model training, a web application for live predictions, and cloud deployment on **Azure via GitHub Actions**.

---

## 🚀 Project Highlights

* 📊 **EDA**: Explored how factors like gender, ethnicity, and parental education impact student performance.
* 🧠 **Modeling**: Trained multiple regression models with hyperparameter tuning and evaluation.
* 🌐 **Web App**: Built an interactive Flask-based web interface to input student details and predict math scores.
* ☁️ **Deployment**: CI/CD pipeline with GitHub Actions for deployment on Microsoft Azure.

---

## 📁 Directory Structure

```
├── artifacts/                   # Model artifacts (preprocessor.pkl, model.pkl,train.csv,test.csv)
├── logs/                        # Logging for experiments
├── src/                         # Source code: pipelines, utils, etc.
│   ├── components/              # Data transformation & model training scripts
│   ├── pipelines/               # Training & prediction pipeline definitions
├── templates/                   # HTML templates for Flask
│   ├── index.html               # Home page
│   └── home.html                # Form input page
├── app.py                       # Flask app runner
├── application.py              # Flask routes and inference logic
├── requirements.txt             # Python dependencies
├── setup.py                     # Project install script
├── .github/workflows/           # GitHub Actions for Azure deployment
│   └── azure_deploy.yml
├── README.md                    # Project description and instructions
└── notebooks/
    ├── 1. EDA STUDENT PERFORMANCE.ipynb
    └── 2. MODEL TRAINING.ipynb
```

---

## 🧪 How to Use

### ⚙️ 1. Local Setup

```bash
git clone https://github.com/<your-username>/Student_performance_indicator_End_to_End_ML_project.git
cd Student_performance_indicator_End_to_End_ML_project
pip install -r requirements.txt
python app.py
```

Open your browser and visit: `http://localhost:5000`

---

### ☁️ 2. Azure Deployment

* GitHub Actions handles:

  * Model packaging
  * App build & push
  * Azure deployment

✅ **CI/CD enabled** for seamless deployment.

---

## 🔍 Input Features

| Feature                     | Type        | Description                             |
| --------------------------- | ----------- | --------------------------------------- |
| Gender                      | Categorical | Male/Female                             |
| Race/Ethnicity              | Categorical | Group A–E                               |
| Parental Level of Education | Categorical | High school, Bachelor’s, Master’s, etc. |
| Lunch                       | Categorical | Standard or Free/Reduced                |
| Test Preparation Course     | Categorical | Completed / None                        |
| Reading Score               | Numeric     | 0-100                                   |
| Writing Score               | Numeric     | 0-100                                   |

---

## 📈 Model Performance

* Best model: **XGBoost**
* R² Score: 86%

---

## 🛠 Tech Stack

* Python (Flask, Pandas, scikit-learn)
* HTML, CSS (Jinja Templates)
* Azure App Service
* GitHub Actions (CI/CD)
* XGBoost, CatBoost

---

## 🙌 Author

**Subhash Pavan Chakravarthy**
*• ML Developer • Azure Deployer*

