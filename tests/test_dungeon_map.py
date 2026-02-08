import pytest
from src import controller
from src.controller import GameController


def test_positive_map_validation(monkeypatch, make_character):
    monkeypatch.setattr(controller, "Player", lambda: make_character())
    dungeon_map = GameController(["St", " ", "E", "Ex"])
    dungeon_map._validate_map()


@pytest.mark.parametrize(
    "invalid_map, tested_validation",
    [
        ([],"Карта не должна быть пуста"),
        (["E", "Ex"],"Карта должна начинаться с 'St'."),
        (["St", "E"],"Карта должна заканчиваться 'Ex'."),
        (["St", "St", "Ex"],"На карте должен быть ровно один 'St'."),
        (["St", "Ex", "Ex"],"На карте должен быть ровно один 'Ex'."),
    ],
)
def test_negative_map_validation(invalid_map, tested_validation, make_character, monkeypatch):
    monkeypatch.setattr(controller, "Player", lambda: make_character())
    try:
        GameController(invalid_map)
    except ValueError as exeption:
        assert tested_validation in str(exeption), f"Ошибка не совпадает с ожидаемой. Была выброшена ошибка: {exeption}"
        return
    pytest.fail(f"Ожидалась ValueError: {tested_validation}, но ошибка не была выброшена")