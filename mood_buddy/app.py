from google.cloud import language_v1
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Initialize the Google Cloud NLP client
def analyze_sentiment(text_content):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})
    return response.document_sentiment.score

def extract_keywords(text_content):
    # Create a client to interact with the NLP API
    client = language_v1.LanguageServiceClient()
    
    # Prepare the document object for NLP processing
    document = language_v1.Document(content=text_content, type_=language_v1.Document.Type.PLAIN_TEXT)
    
    # Use the API to analyze the entities in the text
    response = client.analyze_entities(request={'document': document})
    
    # Extract the names of entities (important words or concepts)
    keywords = []
    for entity in response.entities:
        keywords.append(entity.name)
    
    return keywords

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the text input from the user
    text = request.form['input_data']
    
    # Call the sentiment analysis function
    sentiment_score = analyze_sentiment(text)
    
    # Call the keyword extraction function
    keywords = extract_keywords(text)
    
    # Render the result in a new page, showing both sentiment and extracted keywords
    return render_template('result.html', sentiment_score=sentiment_score, keywords=keywords)
if __name__ == '__main__':
    app.run(debug=True)

# Initialize Vertex AI
def initialize_vertex_ai():
    aiplatform.init(
        project="",  # Replace with your Google Cloud project ID
        location=""      # e.g., "us-central1"
    )

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
