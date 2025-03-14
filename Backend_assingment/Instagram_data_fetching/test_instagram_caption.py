import pytest
from unittest.mock import patch
from instagram_caption import fetch_latest_instagram_post

# ✅ Test when username is empty
def test_fetch_latest_instagram_post_empty_username():
    """Test that an empty username returns an error"""
    
    # Call the function with an empty username
    result = fetch_latest_instagram_post("")
    
    # Assert expected vs actual
    assert result == {"error": "Username cannot be empty"}  


def test_fetch_latest_instagram_post_invalid_username(mocker):
    """Test handling of a non-existent Instagram username"""

    # Mock the actor call to return a response with no dataset ID
    mock_actor = mocker.patch("instagram_caption.client.actor")
    mock_actor.return_value.call.return_value = {"defaultDatasetId": None}

    # Call the function with an invalid username
    response = fetch_latest_instagram_post("invalid_username")

    # Assertions
    assert "error" in response
    assert response["error"] == "Failed to retrieve dataset ID"

def test_fetch_latest_instagram_post_no_posts(mocker):
    """Test when the user exists but has no posts"""

    # Mock the actor call with a valid dataset ID
    mock_actor = mocker.patch("instagram_caption.client.actor")
    mock_actor.return_value.call.return_value = {"defaultDatasetId": "mock_dataset_id"}

    # Mock dataset iteration to return an empty list (no posts)
    mock_dataset = mocker.patch("instagram_caption.client.dataset")
    mock_dataset.return_value.iterate_items.return_value = []

    # Call function
    response = fetch_latest_instagram_post("new_user_no_posts")

    # Assertions
    assert "error" in response
    assert response["error"] == "No recent posts found"

def test_fetch_latest_instagram_post_api_failure(mocker):
    """Test when API call fails"""

    # Mock Apify client behavior
    mock_client = mocker.patch("instagram_caption.client")
    
    # Simulate an API failure
    mock_client.actor.return_value.call.side_effect = Exception("API Failure")

    # Call function
    results = fetch_latest_instagram_post("validuser")

    # Assertions
    assert "error" in results
    assert results["error"] == "An unexpected error occurred"
