from src.characters import Player, Enemy


def test_player_init():
    player = Player()

    assert isinstance(player.name, str) and player.name
    assert isinstance(player.description, str)
    assert isinstance(player.health_points, int)

    assert isinstance(player.weapon_name, str)
    assert isinstance(player.weapon_description, str)
    assert isinstance(player.damage, int)
    assert isinstance(player.hit_chance, float)

    assert isinstance(player.armor_name, str)
    assert isinstance(player.armor_description, str)
    assert isinstance(player.defense, int)

    assert isinstance(player.death_description, str) and player.death_description


def test_enemy_init():
    enemy = Enemy()

    assert isinstance(enemy.name, str) and enemy.name
    assert isinstance(enemy.description, str)
    assert isinstance(enemy.health_points, int)

    assert isinstance(enemy.weapon_name, str)
    assert isinstance(enemy.weapon_description, str)
    assert isinstance(enemy.damage, int)
    assert isinstance(enemy.hit_chance, float)

    assert isinstance(enemy.armor_name, str)
    assert isinstance(enemy.armor_description, str)
    assert isinstance(enemy.defense, int)

    assert isinstance(enemy.death_description, str) and enemy.death_description
