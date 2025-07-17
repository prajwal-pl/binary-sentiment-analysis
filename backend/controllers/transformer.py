# Use a pipeline as a high-level helper
from transformers import pipeline

model = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

def sentiment_analysis(text: str):
    try:
        text = text.strip()
        if not text:
            return "No text provided for sentiment analysis. Please provide a valid input and try again."
        result = model(text)
        print(f"Sentiment analysis result: {result}")
        return result
    except AttributeError:
        return "Invalid input type. Please provide a string."
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return "An error occurred during sentiment analysis."

