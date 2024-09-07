import unittest
from sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_analyze_sentiment(self):
        try:
            analyze_sentiment("Python programming")
        except Exception as e:
            self.fail(f"analyze_sentiment raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()