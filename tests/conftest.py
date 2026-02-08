import sys
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.characters import Character
from src.rooms import Room
@pytest.fixture
def make_character():
    def _make_char(*, health_points=10, damage=5, hit_chance=100, defense=0, name=""):
        return Character(
            name=name,
            description="",
            health_points=health_points,
            death_description="",
            weapon_name="",
            weapon_description="",
            damage=damage,
            hit_chance=hit_chance,
            armor_name="",
            armor_description="",
            defense=defense,
        )

    return _make_char

@pytest.fixture
def make_room_without_json (monkeypatch):
    def empty_init(self, *args, **kwarg):
        self.room_description_data = {"description":""}
    monkeypatch.setattr("src.rooms.Room.__init__" , empty_init)


@pytest.fixture
def make_fake_actions_in_room():
    def factory(controller, steps):
        it = iter(steps)

        def fake_actions_in_room(_room):
            expected_idx, action = next(it)
            assert controller.room_number == expected_idx
            return action

        return fake_actions_in_room

    return factory
