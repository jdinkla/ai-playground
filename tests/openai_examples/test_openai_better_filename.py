"""
Unit tests for the openai_better_filename.py script.
"""

from unittest.mock import MagicMock, patch
from openai_examples.openai_better_filename import generate_filename


def test_generate_filename():
    """
    Tests the generate_filename function, mocking external dependencies.
    """
    # Given
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_message = MagicMock()
    mock_message.content = " a_descriptive_filename "
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]
    mock_client.chat.completions.create.return_value = mock_response

    image_path = "/fake/path/to/image.png"

    with patch(
        "openai_examples.openai_better_filename.encode_image_to_base64",
        return_value="dGVzdF9jb250ZW50",  # "test_content" in base64
    ) as mock_encode:
        # When
        result = generate_filename(mock_client, image_path)

        # Then
        mock_encode.assert_called_once_with(image_path)
        mock_client.chat.completions.create.assert_called_once()

        call_args = mock_client.chat.completions.create.call_args.kwargs
        image_url = call_args["messages"][0]["content"][1]["image_url"]["url"]
        assert image_url == "data:image/png;base64,dGVzdF9jb250ZW50"
        assert result == "a_descriptive_filename"
