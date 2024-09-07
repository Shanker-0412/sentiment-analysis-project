import tweepy
from textblob import TextBlob
import config

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

def analyze_sentiment(query):
    try:
        tweets = api.search_tweets(q=query, count=10)
        
        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
            print(f'Tweet: {tweet.text}')
            print(f'Sentiment: {sentiment}')
            print('---')
    except tweepy.TweepError as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    query = "Python programming"  # Example query
    analyze_sentiment(query)