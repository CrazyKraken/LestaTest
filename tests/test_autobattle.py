import pytest
from src.characters import Character
from src.controller import GameController


@pytest.mark.parametrize(
    "start_hp, weapon_damage, defense, expected_hp, death",
    [
        (10, 5, 2, 7, ''),
        (10, 5, 5, 10, ''),
        (10, 3, 10, 10, ''),
        (1, 10, 0, -9, 'не'),
    ],
)
def test_damage_formula(start_hp, weapon_damage, defense, expected_hp,death):
    character = Character(
        name="",
        description="",
        health_points=start_hp,
        death_description="",
        weapon_name="",
        weapon_description="",
        damage=weapon_damage,
        hit_chance=100,
        armor_name="",
        armor_description="",
        defense=defense,
    )

    character.got_damage(weapon_damage)
    assert character.health_points == expected_hp, f"здоровье не совпадает с ожидаемым: ожидалось {expected_hp}, получено {character.health_points}"
    assert character.is_alive == (expected_hp > 0), f"персоонаж неожиданно {death} умер, хотя его здоровье {character.health_points}"

def test_attack_hit(make_character):
    attacker = make_character(name="attacker")
    target = make_character(defense=2, name="target")
    initial_health_points = target.health_points
    attacker.attack(target)
    assert target.health_points == initial_health_points + target.defense - attacker.damage

def test_attack_mis(make_character):
    attacker = make_character(hit_chance=0, name="attacker")
    target = make_character(name="target")
    initial_health_points = target.health_points
    attacker.attack(target)
    assert target.health_points == initial_health_points

def test_not_hut_after_death(make_character):
    player = make_character(hit_chance=100, name="player")
    enemy = make_character(health_points=5, name="enemy")
    initial_health_points = player.health_points
    GameController.fight(character_1=player,character_2=enemy)
    assert enemy.is_alive == False
    assert player.health_points == initial_health_points
