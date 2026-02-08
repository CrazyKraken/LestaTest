import json
import random
from pathlib import Path
from src.characters import Enemy

ROOM_DESCRIPTION_PATH = Path(__file__).resolve().parent.parent / "data" / "room_description.json"


class Room:
    def __init__(self):
        with open(ROOM_DESCRIPTION_PATH, "r", encoding='utf8') as room_json:
            room_description_dict = json.load(room_json)
        self.room_description_data = random.choice(room_description_dict['rooms'])

    @property
    def room_description(self):
        return self.room_description_data['description']

    def action(self):
        raise NotImplementedError


class EnterDungeon(Room):
    def action(self):
        return ['1. Пойти дальше']


class EmptyRoom(Room):
    def action(self):
        return ["1. Пойти дальше", "2. Вернуться"]


class EnemyRoom(Room):
    def __init__(self):
        super().__init__()
        self.enemy = Enemy()

    def action(self):
        if self.enemy.is_alive:
            return ["1. Сражаться", "2. Вернуться"]
        return ["1. Пойти дальше", "2. Вернуться"]


class ExitDungeon(Room):
    def action(self):
        return ["1. Выйти из подземелья", "2. Вернуться"]
