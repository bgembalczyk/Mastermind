from player import Player

def test_player__init__():
    rules = {}
    player = Player("Vishgraz", rules)
    assert player

def test_player_name():
    rules = {}
    player = Player("Nissa", rules)
    assert player.name() == "Nissa"

def test_player_rules():
    rules = {"monumentToPerfection": 1, "mirranSafehouse": 3, "minorMisstep": "U"}
    player = Player("Narset", rules)
    assert player.rules() == {"monumentToPerfection": 1, "mirranSafehouse": 3, "minorMisstep": "U"}

def test_player__str__():
    rules = {}
    player = Player("Lukka", rules)
    player.score = 5
    assert str(player) == "Lukka: 5"

def test_player_won():
    rules = {}
    player = Player("Jace", rules)
    player.score = 4
    player.won()
    assert player.score == 5

def test_player_checkCombination_wrong():
    rules = {"keyLength": 2, "numberOfColors": 3}
    combination = "33125271442023"
    player = Player("Atraxa", rules)
    assert player.checkCombination(combination) == False

def test_player_checkCombination_wrongColors():
    rules = {"keyLength": 4, "numberOfColors": 8}
    combination = "2920"
    player = Player("Dave", rules)
    assert player.checkCombination(combination) == False

def test_player_checkCombination_wrongLength():
    rules = {"keyLength": 1, "numberOfColors": 7}
    combination = "3136"
    player = Player("Cody", rules)
    assert player.checkCombination(combination) == False

def test_player_checkCombination_correct():
    rules = {"keyLength": 4, "numberOfColors": 5}
    combination = "3130"
    player = Player("Walter White", rules)
    assert player.checkCombination(combination) == True

