# from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

# completion = client.chat.completions.create(
# #   extra_headers={
# #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
# #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
# #   },
#   extra_body={},
#   model="deepseek/deepseek-r1:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )
# print(completion.choices[0].message.content)

# client_id =SUtFRTAtMlAyRWJ6bzAtSUVDdzc6MTpjaQ

# client_secret= Dj9XWyM5p1se4MmKXEy4JyRKqTSQ9aBhLMsiVTCvqhFGwzXjVT

# api key= kUhqfJUSmyDLcGAqiUGT0gPS7

# api key secrer= Dd1elf5axjNNiTDeqs4kMLO4ngIp4MbZ7pKucXxkzuOv5GoBTg

# access_toekn_secret=0a02Pz05E96xbLyOznKBBzkgzsQNS5D3e6zuCRMPngM5n

# access_token=1899722157686685696-T5CoWYKFXuiiAVuKa7EpPSsJ64ET6d

# beare_token=AAAAAAAAAAAAAAAAAAAAALGKzwEAAAAA9KmqWcbUp95q7Ri8hAa%2FVbjlGEE%3Daq4HTbOZR8fBytTDdYgX8CIx1VwMTB4OMQBNDGLNDBY2A1ZxBD

import requests
import json
cap = "Actor Pierce Brosnan has said it is a given that the next James Bond should be British.\n\nBrosnan played Bond between 1995 and 2002—and said he thought it was the \"right decision\" for producers to hand creative control to Amazon.\n\nBut who will be Daniel Craig's successor?\n\nJames Norton, Aaron Taylor-Johnson, and Theo James—all English—are among the bookmakers' favorites to fill Craig's shoes.\n\nWho do you think should take the role? ⬇️\n\nTap the link in @BBCNews’s bio to read about a California-born actor who is one of the rumored names to play the role.\n\n#BBCNews"

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
    # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1:free",
    "messages": [
      {
        "role": "user",
        "content": f"Summarize the following Instagram caption into a concise tweet  (max 280 characters).and only give tweet in output {cap}"
      }
    ],
    
  })
)
data=response.json()
print(data['choices'][0]['message']['content'])