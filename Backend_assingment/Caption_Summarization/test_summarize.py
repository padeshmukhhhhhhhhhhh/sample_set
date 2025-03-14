from summarize import *

def test_summarize_caption_success(mocker):
    """Test successful Instagram caption summarization"""

    # Mock API response
    mock_response = {
        "choices": [{"message": {"content": "This is a summarized tweet."}}]
    }

    # Patch requests.post
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    # Call function
    result = summarize_caption("This is a long Instagram caption.")

    # Assertions
    assert result == "This is a summarized tweet."

def test_summarize_caption_network_failure(mocker):
    """Test network failure scenario"""

    # Patch requests.post to simulate a network error
    mocker.patch("requests.post", side_effect=requests.exceptions.RequestException("Network error"))

    # Call function
    result = summarize_caption("This is a long Instagram caption.")

    # Assertions
    assert "error" in result
    assert result["error"] == "Network request failed"

def test_summarize_caption_api_failure(mocker):
    """Test API returning non-200 status code"""

    # Patch requests.post to return an error response
    mocker.patch("requests.post", return_value=mocker.Mock(status_code=500, text="Internal Server Error"))

    # Call function
    result = summarize_caption("This is a long Instagram caption.")

    # Assertions
    assert "error" in result
    assert result["error"] == "API request failed with status 500"

def test_summarize_caption_empty_string():
    """Test when caption is an empty string."""
    
    result = summarize_caption("")

    # Assertions
    assert isinstance(result, dict)
    assert "error" in result
    assert result["error"] == "Caption must be a non-empty string"

