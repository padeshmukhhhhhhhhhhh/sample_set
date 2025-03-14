from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch






class PostTweetAPITestCase(APITestCase):

    def test_empty_input(self):
        """Test API response when caption is empty."""

        url = reverse('post-tweet')
        data={"caption":""}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["msg"], "Please provide a caption")





    @patch("tweepy.Client.create_tweet")
    
    def test_post_tweet_success(self, mock_create_tweet):
        """Test successful tweet posting with mocked Tweepy API."""

        mock_response = type("MockResponse", (object,), {"data": {"id": "123456"}})()
        mock_create_tweet.return_value = mock_response

        url = reverse("post-tweet") 
        data = {"caption": "Hello, Twitter!"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Tweet posted successfully", response.data["msg"])  

