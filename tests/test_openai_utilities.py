from openai.openai_utilities import message, system_message, create_messages


def test_message_should_return_message():
    assert message("someRole", "someContent") == {
        "role": "someRole",
        "content": "someContent"
    }


def test_system_message_should_return_message():
    assert system_message("someContent") == {
        "role": "system",
        "content": "someContent"
    }


def test_create_messages_should_return_combined_messages():
    prompt = message("system", "somePrompt")
    user1 = message("user", "user1")
    user2 = message("user", "user2")
    history = [user1, user2]
    question = message("user", "someQuestion")
    assert create_messages(prompt, history, question) == [
        prompt, user1, user2, question
    ]
