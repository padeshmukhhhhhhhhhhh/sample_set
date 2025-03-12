from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_jlhAhnX2uYlkz07HEJ68TdxzGZbpJS1Ms2Vb")

# Prepare the Actor input
run_input = {
    "directUrls": ["https://www.instagram.com/bbcnews/"],
    "resultsType": "posts",
    "resultsLimit": 1,
    "searchType": "hashtag",
    "searchLimit": 1,
    "addParentData": False,
}

# Run the Actor and wait for it to finish
run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item['caption'])