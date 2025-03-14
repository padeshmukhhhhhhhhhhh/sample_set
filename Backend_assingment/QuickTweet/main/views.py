
import logging
import tweepy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class post_tweet(APIView):

    def post(self, request):
        tweet = request.data.get("tweet")

        if not tweet:
            logger.warning("No tweet provided in request")
            return Response({"msg": "Please provide a tweet"}, status=400)

        try:
            logger.info("Initializing Twitter client")

            client = tweepy.Client(
                bearer_token=settings.BEARER_TOKEN,
                consumer_key=settings.API_KEY,
                consumer_secret=settings.API_SECRET,
                access_token=settings.ACCESS_TOKEN,
                access_token_secret=settings.ACCESS_SECRET
            )

            logger.info("Posting tweet")
            response = client.create_tweet(text=tweet)

            logger.info(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
            return Response({"msg": f"Tweet posted successfully! Tweet ID: {response.data['id']}"})

        except tweepy.TweepyException as e:
            logger.error(f"Error posting tweet: {str(e)}", exc_info=True)
            return Response(
                {"msg": "Error posting tweet", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
