import json
import random
from pathlib import Path

ENEMY_TEXT_PATH = Path(__file__).resolve().parent.parent / "data" / "enemy_text.json"
PLAYER_TEXT_PATH = Path(__file__).resolve().parent.parent / "data" / "player_text.json"


class Character:
    def __init__(
            self,
            *,
            name: str,
            description: str,
            health_points: int,
            death_description,
            weapon_name: str,
            weapon_description: str,
            damage: int,
            hit_chance: float,
            armor_name: str,
            armor_description: str,
            defense: int,
    ):
        self.name = name
        self.description = description
        self.health_points = health_points
        self.death_description = death_description
        self.weapon_name = weapon_name
        self.weapon_description = weapon_description
        self.damage = damage
        self.hit_chance = hit_chance
        self.armor_name = armor_name
        self.armor_description = armor_description
        self.defense = defense

    def attack(self, target: "Character"):
        if random.random() < self.hit_chance:
            print(self.name, " попал")
            target.got_damage(self.damage)
        else:
            print(self.name, " промахнулся")

    def got_damage(self, damage: int):
        damage = damage - self.defense
        if damage > 0:
            print(self.name, "получает", damage, "урона", "текущее здоровье", self.health_points - damage)
            self.health_points -= damage

    @property
    def is_alive(self):
        return self.health_points > 0


class Enemy(Character):
    def __init__(self):
        with open(ENEMY_TEXT_PATH, "r", encoding="utf8") as enemy_json:
            enemy_description_dict = json.load(enemy_json)

        enemy = random.choice(enemy_description_dict['characters'])

        super().__init__(
            name=enemy['name'],
            description=enemy['description'],
            health_points=enemy['health_points'],
            death_description=enemy['death_description'],
            weapon_name=enemy['weapon_name'],
            weapon_description=enemy['weapon_description'],
            damage=enemy['damage'],
            hit_chance=enemy['hit_chance'] / 100,
            armor_name=enemy['armor_name'],
            armor_description=enemy['armor_description'],
            defense=enemy['defense'],
        )

    @property
    def enemy_meeting_description(self):
        enemy_meeting = (f"\nПеред вами возникает {self.description} "
                         f"Вы понимаете это обычный {self.name}\n"
                         f"Пытясь разглядеть противника получше вы оцениваете его броню и оружие\n"
                         f"Разглядывая то, что он сжимает в руках вы понимете, что это - {self.weapon_description}\n"
                         f"Его броня это - {self.armor_description}")
        return enemy_meeting


class Player(Character):
    def __init__(self):
        with open(PLAYER_TEXT_PATH, "r", encoding="utf8") as player_json:
            player_description_dict = json.load(player_json)
        player = random.choice(player_description_dict['characters'])
        armor = player_description_dict['armor']
        weapon = player_description_dict['weapon']
        super().__init__(
            name=player['name'],
            description=player['description'],
            health_points=player['health_points'],
            death_description=random.choice(player_description_dict['death_description']),
            weapon_name=weapon['weapon_name'],
            weapon_description=weapon['weapon_description'],
            damage=weapon['damage'],
            hit_chance=weapon['hit_chance'] / 100,
            armor_name=armor['armor_name'],
            armor_description=armor['armor_description'],
            defense=armor['defense'],
        )
