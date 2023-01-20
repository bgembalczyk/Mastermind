from mastermind import Mastermind
from player import Player

def test_Mastermind__init__():
    mastermind = Mastermind()
    assert mastermind

def test_score():
    rules = {}
    mastermind = Mastermind()
    mastermind.players = [Player("Król Crack", {}), Player("Ahsoka Tano", {}), Player("Vraska", {})]
    for i in range(3):
        mastermind.players[i].score = i
    assert mastermind.score() == "Król Crack: 0\nAhsoka Tano: 1\nVraska: 2\n"
