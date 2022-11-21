class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)
        return f"Successfully added: {','.join(added)}"

    def add_supply(self, *supplys):
        self.supplies.extend(supplys)

    def __find_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == 'Food':
            raise Exception("There are no food supplies left!")
        if supply_type == 'Drink':
            raise Exception("There are no drink supplies left!")

    def __find_player(self, name):
        for obj in self.players:
            if obj.name == name:
                return obj

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__find_supply(sustenance_type)
        if supply:
            player.sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def _attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_player_stamina(*args):
        result = []
        for player in args:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return '\n'.join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        result = self.__check_player_stamina(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self._attack(first_player, second_player)
        else:
            return self._attack(second_player, first_player)

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, 'Food')
            self.sustain(p.name, 'Drink')

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = '\n'.join(info)
        return result
