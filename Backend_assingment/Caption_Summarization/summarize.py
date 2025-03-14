import requests
import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API URL
API_URL = "https://openrouter.ai/api/v1/chat/completions"






def summarize_caption(caption):
    # Validate caption input
    if not caption or not isinstance(caption, str):
        logging.error("Invalid caption: Caption must be a non-empty string.")
        return {"error": "Caption must be a non-empty string"}

    try:
        logging.info("Sending request to OpenRouter AI...")

        headers = {
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize the following Instagram caption into a concise tweet (max 280 characters). Only give tweet in output: {caption}"
                }
            ]
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(data))

        # Check if request was successful
        if response.status_code != 200:
            logging.error(f"API Error: {response.status_code} - {response.text}")
            return {"error": f"API request failed with status {response.status_code}"}

        # Parse JSON response
        response_data = response.json()

        # Extract tweet summary using direct access like the original code
        tweet_summary = response_data['choices'][0]['message']['content']

        logging.info("Successfully received summarized tweet.")
        return tweet_summary

    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {e}")
        return {"error": "Network request failed"}
    
    except KeyError:
        logging.error("Unexpected JSON structure in API response.")
        return {"error": "Invalid API response format"}
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred"}

# Example usage
if __name__ == "__main__":
    caption = input("Enter Instagram caption: ").strip()  # Take user input
    tweet = summarize_caption(caption)  # Pass input caption
    print("Tweet Summary:", tweet)  # Print the summarized tweet
