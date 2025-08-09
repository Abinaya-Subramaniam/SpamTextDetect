import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download once (you can comment these out after first run)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load saved model and vectorizer
model = joblib.load('spam_detector_model.joblib')
tfidf = joblib.load('tfidf_vectorizer.joblib')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = text.strip()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)

def predict_spam(message):
    clean_msg = preprocess_text(message)
    vectorized_msg = tfidf.transform([clean_msg])
    prediction = model.predict(vectorized_msg)
    return prediction[0]

st.title("Spam SMS Detector")

user_input = st.text_area("Enter your SMS message here:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        result = predict_spam(user_input)
        if result == 'spam':
            st.error("🚨 This message is detected as SPAM!")
        else:
            st.success("✅ This message is NOT spam (ham).")
