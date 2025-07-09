# 🎓 Personalized Learning Path Recommender

This project builds an intelligent system that recommends **personalized learning paths** for students based on their academic performance, learning preferences, and background. It leverages machine learning and data-driven techniques to adaptively guide students toward the most effective learning sequences.

---

## 🚀 Features

- 📊 **Student Performance Analysis**  
  Analyze students' strengths and weaknesses across subjects and time.

- 🧠 **Learning Path Recommendations**  
  Suggest tailored course sequences using clustering, classification, and rule-based inference.

- 🤖 **ML/DL Model Integration**  
  Includes ensemble models, transformers (BERT), and decision trees to predict performance.

- 🌐 **Interactive Streamlit Dashboard**  
  An easy-to-use UI for uploading data, viewing recommendations, and monitoring metrics.

- 🛠️ **Modular Design**  
  Clean and maintainable codebase using standard project structure.

---

## 🗂️ Project Structure

```text
Personalized-Learning-Path-Recommender/
├── app/                     # Streamlit application
│   └── app.py               # Main dashboard
├── data/                    # Student data
│   ├── raw/                 # Raw input files
│   └── processed/           # Cleaned datasets
├── models/                  # Trained ML models
├── notebooks/               # Jupyter notebooks for each phase
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
├── src/                     # Source code
│   ├── data_processing/     # Preprocessing scripts
│   ├── models/              # Model logic
│   ├── recommendation/      # Learning path recommender
│   └── utils/               # Helper functions
├── configs/                 # Configuration files
│   ├── model_config.yaml
│   └── app_config.yaml
├── reports/                 # Reports and logs
├── tests/                   # Unit tests
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── colab_notebook.py        # Colab-ready pipeline script
```


---

## 📈 Model Pipeline

1. **Data Preprocessing**  
   Handle missing values, normalize features, encode categories.

2. **Feature Engineering**  
   Extract important learning signals from attendance, GPA, feedback, etc.

3. **Model Training**  
   Train classifiers (e.g., Random Forest, XGBoost) to predict outcomes.

4. **Recommendation Engine**  
   Generate optimized learning paths using predicted outcomes and clustering.

5. **Streamlit UI**  
   Upload student data → Get visualized recommendations.

---

## 🧪 Tech Stack

- **Python 3.8+**
- **Libraries**:  
  `pandas`, `scikit-learn`, `xgboost`, `lightgbm`, `transformers`, `streamlit`, `plotly`
- **Visualization**: `seaborn`, `matplotlib`, `plotly`
- **Web Interface**: `streamlit`
- **Configs**: `yaml`

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/pavankalyan2/Personalized-Learning-Path-Recommender-using-Student-Performance-Data.git
cd Personalized-Learning-Path-Recommender-using-Student-Performance-Data
pip install -r requirements.txt

streamlit run app/app.py
