import game.characters.character as ch
import game.characters.evil as ev
import game.player as pl


class Pele(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')

    def get_evil(self):
        return [player for player in self.player.game.players if
                player.character.label == 'evil' and type(player.character) != ev.Corinthiano]


class Neymar(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')

    def get_pele(self):
        return [player for player in self.player.game.players if
                type(player.character) in (Pele, ev.Maradona)]


class Kaka(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')
