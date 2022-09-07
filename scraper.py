import praw

user_agent = "Scraper"
reddit = praw.Reddit(
    client_id = "aKfBu6Agrx3kW_ElCYh5nA",
    client_secret = "Ngao_Oo_eW8DFPy0qzjFhi5qSoBDHg",
    user_agent = user_agent
)

headlines = set()
for submission in reddit.subreddit('leagueoflegends').hot(limit=5):
    print(submission.title)