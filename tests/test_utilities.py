# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
from domain import Person, Scene
from utilities import load_from_file, _load_json, _load_yaml, rename_file
import pytest
from pathlib import Path


def test_load_json_should_return_content():
    data = _load_json("tests/examples/example.json")
    assert data["description"] == "This is the description"
    assert len(data["persons"]) == 2
    assert data["persons"][0]["name"] == "A"
    assert data["persons"][0]["prompt"] == "You are A"
    assert data["persons"][0]["voice"] == "onyx"
    assert data["persons"][1]["name"] == "B"
    assert data["persons"][1]["prompt"] == "B is a person"
    assert data["persons"][1]["voice"] == "nova"


def test_load_yaml_should_return_content():
    content = _load_yaml("tests/examples/example.yaml")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"
    assert len(scene.persons) == 2
    assert scene.persons[0] == Person(name="C", prompt="You are C", voice="onyx")
    assert scene.persons[1] == Person(
        name="D", prompt="D is a multi-line person\n", voice="nova"
    )


def test_load_from_file_should_return_content_if_json():
    content = load_from_file("tests/examples/example.json")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"


def test_load_from_file_should_return_content_if_yaml():
    content = load_from_file("tests/examples/example.yaml")
    scene = Scene.model_validate(content)
    assert scene.description == "This is the description"


@pytest.mark.parametrize(
    "original_filename, new_name_base, existing_files, expected_new_filename",
    [
        ("original.txt", "new_file_name", [], "new_file_name.txt"),
        ("original.jpg", "new name: with chars", [], "new_name-_with_chars.jpg"),
        ("source.png", "target_name", ["target_name.png"], "target_name_1.png"),
        (
            "source.md",
            "target_name",
            ["target_name.md", "target_name_1.md"],
            "target_name_2.md",
        ),
        ("another.txt", "clean_name", ["clean_name.txt"], "clean_name_1.txt"),
    ],
)
def test_rename_file(
    tmp_path: Path,
    original_filename: str,
    new_name_base: str,
    existing_files: list[str],
    expected_new_filename: str,
):
    """Tests the rename_file function with various scenarios."""
    # Given
    original_path = tmp_path / original_filename
    original_path.touch()
    for f in existing_files:
        (tmp_path / f).touch()

    # When
    new_path = rename_file(original_path, new_name_base)

    # Then
    expected_path = tmp_path / expected_new_filename
    assert not original_path.exists()
    assert new_path.exists()
    assert new_path == expected_path
    for f in existing_files:
        assert (tmp_path / f).exists()
