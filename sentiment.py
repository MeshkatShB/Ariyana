from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load a pre-trained Persian sentiment model
model_name = "HooshvareLab/bert-fa-base-uncased-sentiment-snappfood"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Set up the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Read and analyze the comments
with open("tweet_comments.txt", "r", encoding="utf-8") as f:
    comments = f.readlines()

with open("persian_sentiment_analysis.txt", "w", encoding="utf-8") as f:
    for comment in comments:
        result = sentiment_pipeline(comment.strip())[0]
        f.write(f"Comment: {comment.strip()}\nSentiment: {result['label']}, Score: {result['score']}\n\n")

print("Sentiment analysis results saved to 'persian_sentiment_analysis.txt'")
