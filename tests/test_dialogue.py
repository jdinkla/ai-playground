from dialogue import Dialogue
from domain import Person, Scene

person = Person(name="name", prompt="prompt")
scene = Scene(description="description", persons=[person])

secondPerson = Person(name="secondName", prompt="secondPrompt")
secondScene = Scene(description="description", persons=[person, secondPerson])


def test_dialogue_should_initialize(mocker):
    mock_client_factory = mocker.MagicMock()
    dialogue = Dialogue(scene, mock_client_factory)

    assert dialogue.scene == scene
    assert dialogue.history == {"name": []}
    assert dialogue.clients == {"name": mock_client_factory()}
    assert dialogue.prompts == {"name": "\ndescription\n\nprompt\n"}
    assert dialogue.subscribers == []


def test_dialogue_should_add_subscriber(mocker):
    mock_client_factory = mocker.MagicMock()
    dialogue = Dialogue(scene, mock_client_factory)
    dialogue.subscribe(mocker.MagicMock())

    assert dialogue.subscribers.__len__() == 1


def test_dialogue_should_play(mocker):
    mock_client = mocker.MagicMock()
    mock_client.chat.completions.create.return_value.choices[
        0
    ].message.content = "someResponse"
    dialogue = Dialogue(scene, lambda: mock_client)
    subscriber = mocker.MagicMock()
    dialogue.subscribe(subscriber)

    # when
    turns = 3
    dialogue.play(turns, "model")

    # then
    assert subscriber.call_count == turns


def test_dialogue_should_turn(mocker):
    mock_client = mocker.MagicMock()
    mock_client.chat.completions.create.return_value.choices[
        0
    ].message.content = "someResponse"
    dialogue = Dialogue(scene, lambda: mock_client)
    subscriber = mocker.MagicMock()
    dialogue.subscribe(subscriber)

    # when
    dialogue.turn(person, "model")

    # then
    subscriber.assert_called_once_with(mock_client, person, "someResponse")


def test_add_to_histories_should_add(mocker):
    mock_client_factory = mocker.MagicMock()
    dialogue = Dialogue(secondScene, mock_client_factory)
    assert dialogue.history == {"name": [], "secondName": []}

    dialogue.add_to_histories("name", "msg")
    assert dialogue.history == {
        "name": [{"role": "user", "content": "msg"}],
        "secondName": [{"role": "assistant", "content": "msg"}],
    }
