
from apify_client import ApifyClient
import logging
import os
from dotenv import load_dotenv

load_dotenv()



# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize the ApifyClient with your API token (replace with your actual token)

client = ApifyClient(os.getenv('API_TOKEN'))

def fetch_latest_instagram_post(username):
    try:
        username = username.strip()
        if not username:
            logging.error("Invalid username provided.")
            return {"error": "Username cannot be empty"}

        logging.info(f"Fetching Instagram data for username: {username}")

        # Prepare the Actor input
        run_input = {
            "directUrls": [f"https://www.instagram.com/{username}/"],
            "resultsType": "posts",
            "resultsLimit": 1,
            "searchType": "hashtag",
            "searchLimit": 1,
            "addParentData": False,
        }

        # Run the Actor and wait for it to finish
        run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

        # Fetch and print Actor results from the run's dataset (if there are any)
        dataset_id = run.get("defaultDatasetId")
        if not dataset_id:
            logging.error("No dataset ID found in the response.")
            return {"error": "Failed to retrieve dataset ID"}

        results = []
        for item in client.dataset(dataset_id).iterate_items():
            caption = item.get("caption", "No caption available")
            image_url = item.get("displayUrl", "No image available")
            results.append({"caption": caption, "image_url": image_url})

            

        if not results:
            logging.warning(f"No posts found for username: {username}")
            return {"error": "No recent posts found"}

        logging.info("Successfully retrieved Instagram post.")
        return results[0]  # Returning the first post data

    except Exception as e:
        logging.error(f"Error fetching Instagram post: {e}")
        return {"error": "An unexpected error occurred"}

# Example usage
if __name__ == "__main__":
    username = input("Enter Instagram username: ").strip()
    post_data = fetch_latest_instagram_post(username)
    print(post_data)
