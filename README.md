# Instagram to X (Twitter) - Modular API

This project handles the process of fetching the latest post from the **a user-specified Instagram account**, summarizing the caption using an **LLM (AI model)**, and posting the summarized text to **X (Twitter)**. The system is structured into three separate modules for better modularity and maintainability.

### 🔍 Key Modules

1. **Instagram Fetching Module**: Uses the **Apify API** to retrieve the latest post caption and image from a user-specified Instagram account.
2. **AI Summarization Module**: Uses **DeepSeek R1 LLM with the help of OpenRouter API** to summarize the caption into a concise format suitable for a tweet.
3. **X.com Posting Module**: Uses the **official X.com API** to post the summarized text to Twitter.

### 🌐 Technologies Used

- **Python** (Django REST Framework)
- **Apify API** (for fetching Instagram posts)
- **OpenRouter API** (for AI-based text summarization)
- **Tweepy** (for X.com API integration)
- **dotenv** (for managing API keys securely)
- **pytest** (for unit testing)

---

## 🛠️ Setup Instructions

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd sample_set/Backend_assingment
   ```

3. Create a Virtual Environment

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## ⚠️ Note

I have provided all API keys required for the three modules in the code for testing purposes. If you prefer, you can create API keys using the steps provided in each section below.

## 🏆 Run the Instagram Fetching Module

### ✨ Step to Create an Apify Account and Get API Key

1. Go to [Apify](https://apify.com/) and **sign up** for a free account.
2. Once logged in, navigate to the **API** section in your account settings.
3. Generate a new **API Key** and copy it.
4. Store the API Key securely in a `.env` file in your project directory:
   ```
   API_TOKEN=your_api_key_here
   ```
5. Ensure your application loads the API key from the `.env` file.

   First, navigate to the **Instagram\_data\_fetching** folder:
   ```bash
   cd Instagram_data_fetching
   ```
   Then, run the following command:
   ```bash
   python instagram_caption.py
   ```
   It will prompt you to enter an Instagram username. Enter `bbcnews` (or any other username), and you will receive the most recent post caption and image as output.

## 📝 Run the Caption Summarization Module

### ✨ Step to Create an OpenRouter Account and Get API Key

1. Go to [OpenRouter](https://openrouter.ai/) and **sign up** for an account.
2. After logging in, navigate to the **API Keys** section in your account settings.
3. Click on **Generate New Key** and copy the API key.
4. Store the API Key securely in a `.env` file in your project directory:
   ```
   API_KEY=your_api_key_here
   ```
5. Ensure your application loads the API key from the `.env` file.

---

1. Navigate to the **Caption\_Summarization** folder:

   ```bash
   cd Caption_Summarization
   ```

2. Run the summarization script:

   ```bash
   python summarize.py
   ```

3. Enter the Instagram caption when prompted.

4. The script will generate a tweet-friendly summarized version of the caption and display it as output.

## 🚀 Run the X.com (Twitter) Posting Module

### ✨ Steps to Create an X.com Developer Account and Get API Keys

1. Go to [X Developer Portal](https://developer.x.com/) and **sign up** for a developer account.

2. Navigate to the **Developer Portal** and create a new project within your account.

3. First, change the permission of the app to **Read/Write**.

4. Go to the **Keys and Tokens** section to generate the following credentials:

   - `API_KEY`
   - `API_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_SECRET`
   - `BEARER_TOKEN`

5. Store these keys securely in a `.env` file in your project directory:

   ```
   API_KEY=your_api_key_here
   API_SECRET=your_api_secret_here
   ACCESS_TOKEN=your_access_token_here
   ACCESS_SECRET=your_access_secret_here
   BEARER_TOKEN=your_bearer_token_here
   ```

6. Ensure your application loads the API keys from the `.env` file.

7. Navigate to the **QuickTweet** folder:

   ```bash
   cd QuickTweet
   ```

8. Run the Django project:

   ```bash
   python manage.py runserver
   ```

9. Open your browser and visit:

   ```
   http://127.0.0.1:8000/post-tweet
   ```

10. In the API request, add the following JSON payload:

    ```json
    {
        "tweet": "Hi Bro"
    }
    ```

11. Click the **POST** button.

12. You will see a success message, and the tweet will be posted on the actual Twitter account.

---

## ⚡ Steps for Automation

To automate the process of fetching Instagram posts, summarizing captions, and posting to Twitter, follow these steps:

1. **Create a function **``** that does the following:**

   - Calls `fetch_instagram_post(username)` → returns `(caption, image)`.
   - Calls `summarize_caption(caption)` → returns `summarized_text`.
   - Calls `post_to_x(summarized_text, image)` → returns success/failure.

2. **Use a scheduler to run this function automatically.**

   - Install the `schedule` library:
     ```bash
     pip install schedule
     ```
   - Add the following scheduler in your script:
     ```python
     import schedule
     import time

     schedule.every(2).hours.do(process_instagram_to_tweet, username="bbcnews")

     while True:
         schedule.run_pending()
         time.sleep(60)
     ```
   - This will run the process automatically every 2 hours.

---
Thank You

