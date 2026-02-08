import pytest
from src import controller
from src.controller import GameController

@pytest.mark.parametrize(
    "steps",
    [
        [(0, "1"), (1, "1"), (2, "3")],
        [(0, "1"), (1, "2"), (0, "1"), (1, "1"), (2, "3")],
        [(0, "1"), (1, "1"), (2, "2"), (1, "1"), (2, "3")],
    ]
)
def test_movement_changes_indices(monkeypatch, make_room_without_json, make_character, make_fake_actions_in_room, steps):
    monkeypatch.setattr(controller, "Player", lambda: make_character())
    dungeon_map = GameController(["St", " ", "Ex"])
    it = iter(steps)
    monkeypatch.setattr(dungeon_map, "actions_in_room", make_fake_actions_in_room(dungeon_map, it))
    dungeon_map.run()
    assert dungeon_map.room_number == 2
    assert dungeon_map.in_dungeon is False

