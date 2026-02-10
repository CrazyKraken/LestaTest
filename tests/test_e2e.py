import pytest
from src.controller import GameController
@pytest.mark.parametrize(
    "dungeon_map, player_hp, player_damage, expected_room_number,expected_alive",
    [
        (['St', ' ', 'Ex'],1,1,2, True),
        (['St', ' ', 'E', 'Ex'],10000, 4,3, True),
        (['St', ' ', 'E', 'Ex'],10, 0,2, False),
    ],
)
def test_e2e(monkeypatch, dungeon_map, player_hp, player_damage,expected_room_number,expected_alive):
    dungeon = GameController(dungeon_map)
    dungeon.player.health_points = player_hp
    dungeon.player.damage = player_damage
    inputs = ['1']* (len(dungeon_map) + 1)
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda *_: next(it))
    dungeon.run()
    assert dungeon.in_dungeon is False
    assert dungeon.player.is_alive is expected_alive
    assert dungeon.room_number == expected_room_number
