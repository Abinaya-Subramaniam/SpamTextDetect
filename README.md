# SpamDetect

## 📌 Overview

**SpamDetect** is a machine learning project aimed at classifying SMS messages as either **spam** or **ham** (non-spam). Utilizing Natural Language Processing (NLP) techniques and a Naive Bayes classifier, the model achieves high accuracy in distinguishing between unsolicited promotional messages and legitimate communications.

## 🔍 Project Highlights

- **Data Preprocessing**: 
  - Lowercased text
  - Removal of punctuation, numbers, and extra spaces
  - Stopword elimination
  - Lemmatization

- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization

- **Modeling**: Naive Bayes Classifier

- **Deployment**: Streamlit web interface for real-time SMS classification

## 📊 Dataset

The dataset used for this project is the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) from Kaggle. It comprises 5,574 English SMS messages labeled as 'spam' or 'ham', collected for SMS spam research.

## 🚀 Features

- **Real-time SMS Classification**: Input any SMS message to receive an instant classification as spam or ham.
- **User-Friendly Interface**: Built using Streamlit for an interactive experience.
- **Model Accuracy**: Achieved an accuracy of 97% on the test set.

## 🛠️ Installation & Usage
### Prerequisites

Ensure you have Python 3.7+ installed. It's recommended to use a virtual environment.

### 1. Clone the Repository

```bash
git clone https://github.com/Abinaya-Subramaniam/spamdetect.git
cd spamdetect
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App
```bash
streamlit run app.py
```

