import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as SIA
import pandas as pd
import praw

sia = SIA()

user_agent = "Scraper"
reddit = praw.Reddit(
    client_id = "aKfBu6Agrx3kW_ElCYh5nA",
    client_secret = "Ngao_Oo_eW8DFPy0qzjFhi5qSoBDHg",
    user_agent = user_agent
)

headlines = set()
for submission in reddit.subreddit('leagueoflegends').hot(limit=5):
    headlines.add(submission.title)
print(headlines)

df = pd.DataFrame(headlines)
print(df)