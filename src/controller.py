from src.rooms import EnterDungeon, EmptyRoom, EnemyRoom, ExitDungeon, Room
from src.characters import Player, Character


class GameController:
    def __init__(self, dungeom_map: list[str]):
        self.dungeom_map = dungeom_map
        self.room_number = 0
        self.in_dungeon = True
        self.rooms_list = []
        self.player = Player()
        self._validate_map()

    @staticmethod
    def _create_room(room_type: str):
        if room_type == "St":
            return EnterDungeon()
        if room_type == " ":
            return EmptyRoom()
        if room_type == "E":
            return EnemyRoom()
        if room_type == "Ex":
            return ExitDungeon()
        raise ValueError(f"Неизвестный тип комнаты {room_type}")

    def _validate_map(self):
        if len(self.dungeom_map) == 0:
            raise ValueError("Карта не должна быть пуста")
        if self.dungeom_map[0] != "St":
            raise ValueError("Карта должна начинаться с 'St'.")

        if self.dungeom_map[-1] != "Ex":
            raise ValueError("Карта должна заканчиваться 'Ex'.")

        if self.dungeom_map.count("St") != 1:
            raise ValueError("На карте должен быть ровно один 'St'.")

        if self.dungeom_map.count("Ex") != 1:
            raise ValueError("На карте должен быть ровно один 'Ex'.")

    def run(self):
        while self.in_dungeon:
            if len(self.rooms_list) == self.room_number:
                self.rooms_list.append(self._create_room(self.dungeom_map[self.room_number]))
            room = self.rooms_list[self.room_number]
            print(room.room_description)
            if isinstance(room, EnemyRoom) and room.enemy.is_alive:
                print(room.enemy.enemy_meeting_description)

            action = self.actions_in_room(room)
            if action == "1":
                self.room_number += 1
            elif action == "2":
                self.room_number -= 1
            elif action == "3":
                self.in_dungeon = False

    @staticmethod
    def fight(*, character_1: Character, character_2: Character):
        while character_1.is_alive and character_2.is_alive:
            character_1.attack(target=character_2)
            if character_2.is_alive:
                character_2.attack(target=character_1)

    @staticmethod
    def _parse_choices(room):
        print("Возможные действия:")
        action_list = room.action()
        for s in action_list:
            print(s)
        allowed = [str(i) for i in range(1, len(action_list) + 1)]
        while True:
            actions = input("Ваши действия: ").strip()
            if actions in allowed:
                return actions
            print(f"Некорректный ввод: {actions}.\nВведите доступный вариант: {', '.join(allowed)}.")

    def actions_in_room(self, room: Room):
        action = self._parse_choices(room)
        if room.action()[0] == "1. Сражаться" and action == "1":
            self.fight(character_1=self.player, character_2=room.enemy)
            if not self.player.is_alive:
                print(self.player.death_description)
                return "3"
            else:
                print(room.enemy.death_description)
            action = self._parse_choices(room)
            return action
        elif room.action()[0] == "1. Выйти из подземелья" and action == "1":
            return "3"
        return action
