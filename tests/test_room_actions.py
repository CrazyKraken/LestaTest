from src import rooms
from src.rooms import EnterDungeon, EnemyRoom, ExitDungeon, EmptyRoom

def test_enter_room_actions(make_room_without_json):
    room = EnterDungeon()
    actions = room.action()

    assert any("Пойти дальше" in a for a in actions)
    assert all("Вернуться" not in a for a in actions)
    assert all("Сражаться" not in a for a in actions)
    assert all("Выйти" not in a for a in actions)

def test_empty_room_actions(make_room_without_json):
    room = EmptyRoom()
    actions = room.action()

    assert any("Пойти дальше" in a for a in actions)
    assert any("Вернуться" in a for a in actions)
    assert all("Сражаться" not in a for a in actions)
    assert all("Выйти" not in a for a in actions)


def test_exit_room_actions(make_room_without_json):
    room = ExitDungeon()
    actions = room.action()

    assert all("Пойти дальше" not in a for a in actions)
    assert any("Вернуться" in a for a in actions)
    assert all("Сражаться" not in a for a in actions)
    assert any("Выйти" in a for a in actions)


def test_living_enemy_room_actions(monkeypatch, make_character, make_room_without_json):
    monkeypatch.setattr(rooms, "Enemy", lambda: make_character(health_points=1))
    room = EnemyRoom()
    actions = room.action()

    assert all("Пойти дальше" not in a for a in actions)
    assert any("Вернуться" in a for a in actions)
    assert any("Сражаться" in a for a in actions)
    assert all("Выйти" not in a for a in actions)



def test_died_enemy_room_actions(monkeypatch, make_character, make_room_without_json):
    monkeypatch.setattr(rooms, "Enemy", lambda: make_character(health_points=0))
    room = EnemyRoom()
    actions = room.action()

    assert any("Пойти дальше" in a for a in actions)
    assert any("Вернуться" in a for a in actions)
    assert all("Сражаться" not in a for a in actions)
    assert all("Выйти" not in a for a in actions)
