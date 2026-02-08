import builtins
import pytest
from src.rooms import Room
from src.controller import GameController

@pytest.mark.parametrize("user_input", ["1", " 1", "1 ", " 1 ", "2"])
def test_parse_input_positive(monkeypatch,  user_input, capsys, make_room_without_json):
    room = Room()
    monkeypatch.setattr(room, "action", lambda: ["One", "Two"])
    inputs = iter([user_input])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = GameController._parse_choices(room)
    out = capsys.readouterr().out
    assert result == user_input.strip()
    assert "Некорректный ввод:" not in out
    assert "Введите доступный вариант: 1, 2." not in out


@pytest.mark.parametrize("user_input", ["", " asd", "*** ", " 4 "])
def test_parse_input_negative(monkeypatch, user_input, capsys, make_room_without_json):
    room = Room()
    monkeypatch.setattr(room, "action", lambda : ['One'])
    inputs = iter([user_input, "1"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    GameController._parse_choices(room)
    out = capsys.readouterr().out
    assert "Некорректный ввод:" in out
    assert "Введите доступный вариант: 1." in out
