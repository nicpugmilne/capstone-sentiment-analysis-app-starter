"""
SentimentScope - Sentiment Analysis Application

This Flask application provides sentiment analysis using two different models:
1. VADER (Valence Aware Dictionary and sEntiment Reasoner) - for general sentiment analysis
2. Custom Keras model - trained on UCI Labelled Sentences dataset

The app allows users to input text and receive sentiment analysis results from both models.
"""

import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence

from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Global variables for model and tokenizer
model = None
tokenizer = None

def load_keras_model():
    """
    Load the pre-trained Keras sentiment analysis model.
    
    The model is trained on the UCI Labelled Sentences dataset and achieves
    approximately 79.7% accuracy on the test set.
    """
    global model
    model = load_model('models/uci_sentimentanalysis.h5')

def load_tokenizer():
    """
    Load the tokenizer used for text preprocessing.
    
    The tokenizer converts text input into sequences that the model can process.
    """
    global tokenizer
    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

def sentiment_analysis(input):
    """
    Perform sentiment analysis using the custom Keras model.
    
    Args:
        input (str): The text to analyze
        
    Returns:
        float: Sentiment score between 0 and 1, where values > 0.5 indicate positive sentiment
    """
    user_sequences = tokenizer.texts_to_sequences([input])
    user_sequences_matrix = sequence.pad_sequences(user_sequences, maxlen=1225)
    prediction = model.predict(user_sequences_matrix, verbose=0)
    return round(float(prediction[0][0]), 2)

@app.before_first_request
def before_first_request():
    """
    Initialize the application by loading the model and tokenizer.
    
    This function is called before the first request to ensure the model
    is loaded and ready for predictions.
    """
    load_keras_model()
    load_tokenizer()

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for the sentiment analysis application.
    
    Handles both GET requests (display form) and POST requests (analyze text).
    
    Returns:
        str: Rendered HTML template with sentiment analysis results
    """
    sentiment = None
    if request.method == "POST":
        text = request.form.get("user_text")
        if text:
            # VADER sentiment analysis
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(text)
            
            # Custom model sentiment analysis
            sentiment["custom model positive"] = sentiment_analysis(text)
    
    return render_template('form.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run()
