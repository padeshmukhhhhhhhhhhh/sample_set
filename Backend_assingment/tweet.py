import tweepy

# Replace with your credentials
API_KEY = "UF9IDgtoQYqsNnvaxmh03Cwos"
API_SECRET = "nnQgNBvF2nGTpSA02r34YilWl2HQicUBovsI13aJoHvAD4fDPK"
ACCESS_TOKEN = "1899722157686685696-gXuG0uVzBpgHcqy4RjJ9rSLJieVkyJ"
ACCESS_SECRET = "LvL251eX9owe24KDGA0CBfXl74jHMMKXGv1ci3UaNR7r2"
# consumer_key = 'SUtFRTAtMlAyRWJ6bzAtSUVDdzc6MTpjaQ'
# consumer_secret = 'aWJhZGJhZGJhDj9XWyM5p1se4MmKXEy4JyRKqTSQ9aBhLMsiVTCvqhFGwzXjVTZGJh'
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAALGKzwEAAAAA4Qt8g2s22HYajEU%2F7dmkX5avjPU%3DWh8pPs5l5crCvPAEAZH8zE5PupM46vjxBWf6utik9V4XNOG6Uf"

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Post a tweet
response = client.create_tweet(text="Hello, Twitter API v2! 🚀 #Tweepy")

print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")