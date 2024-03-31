from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
#nltk.download('vader_lexicon')

s = input("Enter your Feedback:")
sa = SentimentIntensityAnalyzer()
factor = sa.polarity_scores(s)
if factor['neg'] != 0:
    print("The comment is bad")
else:
    print("The Comment is good")