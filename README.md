# Personality Detector


## Overview
This project predicts an individual's personality type (introvert, extrovert, or ambivert) based on their behavioral and psychological characteristics. 
Ratings of Individual characteristics (1-10) via interaction with a Streamlit frontend provides data, which is then processed by a trained model running locally through a FastAPI backend


## Project Structure
```
Personality-Type-Dectector/
│
├── backend/
│   ├── app/
│   │   ├── main.py             # FastAPI code for data input validation and serving predictions
│   │   ├── preprocessing.py    # Code for preprocessing data (scaling) before feeding it into the
│   │   └── utils.py            # Code for formating predictions 
│   │
│   └── models/
│       ├── column_names.pkl     # Saved column names used in feature processing.
│       ├── final_model.pkl      # The trained model file for personality classification.
│       ├── label_encoder.pkl    # Encoder for transforming categorical labels (e.g., "Introvert", "Extrovert", "Ambivert").
│       └── scaler.pkl
│   
│   
├── data/                
│   └── personality_synthetic_dataset.csv       # dataset used for model training      
│   
├── frontend/
│   └── app.py               # Streamlit frontend app         
│
├── notebooks/
│   └── model_training.py    # Jupyter notebook for model training and experimentation.
│
├── .dockerignore           # Python dependencies
├── .gitignore              # Python dependencies
├── Dockerfile              # Python dependencies
├── README.md               # Python dependencies
└── requirements.txt        # Project documentation
```


## Technical Stack
- Python 
- Scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn


## Data
The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/miadul/introvert-extrovert-and-ambivert-classification). It is a synthetic dataset (free from missing values and outliers) designed to simulate human personality types — Introvert, Extrovert, and Ambivert — based on various behavioral and psychological traits. It contains 20,000 entries and 30 columns, including 29 numerical features representing personality indicators and 1 label column (personality_type). A balanced dataset with approximately 30% frequency for each class.


## Model Architecture
- Experimented with 5 baseline models (logistic regression, SVM, AdaBoost, Gradient Boosting and XGBoost) all trained in a Google collab jupiter notebook
- Evaluation metrics:
    - Confusion Matrix
    - Classification report
    - Accuracy score
    - Micro-F1 score (since it's a balanced dataset)
- Best model (SVM) performance metrics:
    - Accuracy score: 0.99850
    - Micro-F1 score: 0.99850


## Live Link


## Setup and Installation
- Clone the repository
    ```
    git clone https://github.com/yusuf17ml/Personality-Type-Detector.git
    ```

- Navigate to the project drectory
    ```
    cd Personality-Type-Detector
    ```

- Create a virual environment
    ```
    python -m venv .venv
    ```
    
- Activate the virtual environment
    - Linux/macOS:
    ```
    source .venv/bin/activate
    ```
    - Windows:
    ```
    .venv\Scripts\activate
    ```

- Install the required packages
    ```
    pip install -r requirements.txt
    ```


## Usage
- Run the FastAPI backend
    ```
    uvicorn app.main:app --reload
    ```
- Run the streamlit frontend
    ```
    streamlit run frontend/app.py
    ```
*Interact with the app via the streamlit frontend to get a fast and seamless response from the FastAPI backend*


## What I learned 
It was a great learning project for me as i was able to:
- Deepen my understanding of FastAPI’s ability to serve machine learning models at scale.
- Implement model predictions through an API endpoint

