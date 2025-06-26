from unittest.mock import MagicMock

from openai_examples import openai_chat
from openai_examples.openai_utilities import MODELS, message


def test_get_chat_completion_success(mocker):
    """
    Tests that get_chat_completion returns the message content on a successful API call.
    """
    # Given
    mock_client = MagicMock()
    mock_response = MagicMock()
    expected_content = "1. L'Esprit Libre\n2. Sans Alcool Chic\n3. Le Nectar Vide"
    mock_response.choices[0].message.content = expected_content
    mock_client.chat.completions.create.return_value = mock_response

    # When
    result = openai_chat.get_chat_completion(mock_client)

    # Then
    assert result == expected_content
    mock_client.chat.completions.create.assert_called_once_with(
        model=MODELS[0],
        messages=[
            message("system", "You are crazy advertisement guru."),
            message(
                "user",
                "Create three names that consist of two or more words for a brand selling fake alcohol!",
            ),
            message(
                "assistant",
                "1. Faux Spirits\n2. Mocktail Makers\n3. Counterfeit Cocktails",
            ),
            message("user", "More sophisticated and a little french, please."),
        ],
    )


def test_get_chat_completion_api_error(mocker):
    """
    Tests that get_chat_completion handles an API error gracefully and returns None.
    """
    # Given
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = Exception("API connection failed")

    # When
    result = openai_chat.get_chat_completion(mock_client)

    # Then
    assert result is None
