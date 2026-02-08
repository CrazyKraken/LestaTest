import json
import pytest
from pathlib import Path

ENEMY_TEXT_PATH = Path(__file__).resolve().parent.parent / "data" / "enemy_text.json"
PLAYER_TEXT_PATH = Path(__file__).resolve().parent.parent / "data" / "player_text.json"
ROOM_DESCRIPTION_PATH = Path(__file__).resolve().parent.parent / "data" / "room_description.json"


def test_json_room_description():
    assert ROOM_DESCRIPTION_PATH.exists(), f"не найден: {ROOM_DESCRIPTION_PATH}"

    rooms = json.loads(ROOM_DESCRIPTION_PATH.read_text(encoding="utf8"))

    assert isinstance(rooms, dict), f"room_description.json должен быть dict, но получен {type(rooms).__name__}."

    assert "rooms" in rooms and isinstance(rooms['rooms'],
                                           list), f"rooms в room_description.json должен быть list, но получен {type(rooms['rooms']).__name__}."

    assert len(rooms['rooms']) > 0, "rooms в room_description.json должен содержать хотябы 1 элемент."
    assert "description" in rooms['rooms'][
        0], "rooms в room_description.json должен содержать обязательный заголовок description."
    assert isinstance(rooms['rooms'][0]['description'],
                      str), f"description в rooms в room_description.json должен быть str, но получен {type(rooms['rooms'][0]['description']).__name__}."


def test_json_player_text():
    assert PLAYER_TEXT_PATH.exists(), f"не найден: {PLAYER_TEXT_PATH}"
    player = json.loads(PLAYER_TEXT_PATH.read_text(encoding="utf8"))
    assert isinstance(player, dict), f"player_text.json должен быть dict, но получен {type(player).__name__}."
    assert "characters" in player and isinstance(player['characters'],
                                                 list), f"characters в player_text.json должен быть list, но получен {type(player['characters']).__name__}."
    assert "weapon" in player and isinstance(player['weapon'],
                                             dict), f"weapon в player_text.json должен быть dict, но получен {type(player['weapon']).__name__}."
    assert "armor" in player and isinstance(player['armor'],
                                            dict), f"armor в player_text.json должен быть dict, но получен {type(player['armor']).__name__}."
    assert "death_description" in player and isinstance(player['death_description'],
                                                        list), f"death_description в player_text.json должен быть list, но получен {type(player['death_description']).__name__}."

    assert len(player['characters']) > 0, "characters в player_text.json должен содержать хотябы 1 элемент."
    assert len(player['weapon']) > 0, "weapon в player_text.json должен содержать хотябы 1 элемент."
    assert len(player['armor']) > 0, "armor в player_text.json должен содержать хотябы 1 элемент."
    assert len(
        player['death_description']) > 0, "death_description в player_text.json должен содержать хотябы 1 элемент."

    assert "name" in player['characters'][
        0], "characters в player_text.json должен содержать обязательный заголовок name."
    assert "description" in player['characters'][
        0], "characters в player_text.json должен содержать обязательный заголовок description."
    assert "health_points" in player['characters'][
        0], "characters в player_text.json должен содержать обязательный заголовок health_points."

    assert "weapon_name" in player[
        "weapon"], "weapon в player_text.json должен содержать обязательный заголовок weapon_name."
    assert "weapon_description" in player[
        "weapon"], "weapon в player_text.json должен содержать обязательный заголовок weapon_description."
    assert "damage" in player['weapon'], "weapon в player_text.json должен содержать обязательный заголовок damage."
    assert "hit_chance" in player[
        "weapon"], "weapon в player_text.json должен содержать обязательный заголовок hit_chance."

    assert "armor_name" in player[
        "armor"], "armor в player_text.json должен содержать обязательный заголовок armor_name."
    assert "armor_description" in player[
        "armor"], "armor в player_text.json должен содержать обязательный заголовок armor_description."
    assert "defense" in player['armor'], "armor в player_text.json должен содержать обязательный заголовок defense."

    assert "description" in player['death_description'][
        0], "death_description в player_text.json должен содержать обязательный заголовок description."

    assert isinstance(player['characters'][0]
                      ['name'],
                      str), f"name в characters в player_text.json должен быть str, но получен {type(player['characters'][0]['name']).__name__}."
    assert isinstance(player['characters'][0]['description'],
                      str), f"description в characters в player_text.json должен быть str, но получен {type(player['characters'][0]['description']).__name__}."
    assert isinstance(player['characters'][0]['health_points'],
                      int), f"health_points в characters в player_text.json должен быть int, но получен {type(player['characters'][0]['health_points']).__name__}."

    assert isinstance(player['weapon']['weapon_name'],
                      str), f"weapon_name в weapon в player_text.json должен быть str, но получен {type(player['weapon'][0]['weapon_name']).__name__}."
    assert isinstance(player['weapon']['weapon_description'],
                      str), f"weapon_description в weapon в player_text.json должен быть str, но получен {type(player['weapon'][0]['weapon_description']).__name__}."
    assert isinstance(player['weapon']['damage'],
                      int), f"damage в weapon в player_text.json должен быть int, но получен {type(player['weapon'][0]['damage']).__name__}."
    assert isinstance(player['weapon']['hit_chance'],
                      int), f"damage в weapon в player_text.json должен быть int, но получен {type(player['weapon'][0]['hit_chance']).__name__}."

    assert isinstance(player['armor']['armor_name'],
                      str), f"armor_name в armor в player_text.json должен быть str, но получен {type(player['armor'][0]['armor_name']).__name__}."
    assert isinstance(player['armor']['armor_description'],
                      str), f"armor_description в armor в player_text.json должен быть str, но получен {type(player['armor'][0]['armor_description']).__name__}."
    assert isinstance(player['armor']['defense'],
                      int), f"defense в armor в player_text.json должен быть int, но получен {type(player['armor'][0]['defense']).__name__}."

    assert isinstance(player['death_description'][0]['description'],
                      str), f"description в death_description в player_text.json должен быть str, но получен {type(player['death_description'][0]['description']).__name__}."


def test_json_enemy_text():
    assert ENEMY_TEXT_PATH.exists(), f"не найден: {ENEMY_TEXT_PATH}"
    enemy = json.loads(ENEMY_TEXT_PATH.read_text(encoding="utf8"))
    assert isinstance(enemy, dict), f"enemy_text.json должен быть dict, но получен {type(enemy).__name__}."
    assert "characters" in enemy, "enemy_text.json должен содержать обязательный заголовок characters."
    assert isinstance(enemy['characters'],
                      list), f"characters в enemy_text.json должен быть list, но получен {type(enemy['characters']).__name__}."

    assert "name" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок name."
    assert "description" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок description."
    assert "health_points" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок health_points."
    assert "death_description" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок death_description."
    assert "weapon_name" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок weapon_name."
    assert "weapon_description" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок weapon_description."
    assert "damage" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок damage."
    assert "hit_chance" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок hit_chance."
    assert "armor_name" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок armor_name."
    assert "armor_description" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок armor_description."
    assert "defense" in enemy['characters'][
        0], "characters в enemy_text.json должен содержать обязательный заголовок defense."

    assert isinstance(enemy['characters'][0]['name'],
                      str), f"name в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['name']).__name__}."
    assert isinstance(enemy['characters'][0]['description'],
                      str), f"description в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['description']).__name__}."
    assert isinstance(enemy['characters'][0]['health_points'],
                      int), f"health_points в characters в enemy_text.json должен быть int, но получен {type(enemy['characters'][0]['health_points']).__name__}."
    assert isinstance(enemy['characters'][0]['death_description'],
                      str), f"death_description в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['death_description']).__name__}."
    assert isinstance(enemy['characters'][0]['weapon_name'],
                      str), f"weapon_name в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['weapon_name']).__name__}."
    assert isinstance(enemy['characters'][0]['weapon_description'],
                      str), f"weapon_description в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['weapon_description']).__name__}."
    assert isinstance(enemy['characters'][0]['damage'],
                      int), f"damage в characters в enemy_text.json должен быть int, но получен {type(enemy['characters'][0]['damage']).__name__}."
    assert isinstance(enemy['characters'][0]['hit_chance'],
                      int), f"hit_chance в characters в enemy_text.json должен быть int, но получен {type(enemy['characters'][0]['hit_chance']).__name__}."
    assert isinstance(enemy['characters'][0]['armor_name'],
                      str), f"armor_name в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['armor_name']).__name__}."
    assert isinstance(enemy['characters'][0]['armor_description'],
                      str), f"armor_description в characters в enemy_text.json должен быть str, но получен {type(enemy['characters'][0]['armor_description']).__name__}."
    assert isinstance(enemy['characters'][0]['defense'],
                      int), f"defense в characters в enemy_text.json должен быть int, но получен {type(enemy['characters'][0]['defense']).__name__}."
