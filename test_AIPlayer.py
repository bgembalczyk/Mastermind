from AIPlayer import AIPlayer

def test_AIPlayer__init__():
    rules = {}
    aiPlayer = AIPlayer(rules)
    assert aiPlayer

def test_AIPlayer_name():
    rules = {}
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.name() == "AI"

def test_AIPlayer_rules():
    rules = {"Boba Fett's Starship Microfighter": 75344, "501st Clone Troopers Battle Pack": 75345, "TIE Bomber": 75347}
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.rules() == {"Boba Fett's Starship Microfighter": 75344, "501st Clone Troopers Battle Pack": 75345, "TIE Bomber": 75347}

def test_AIPlayer__str__():
    rules = {}
    aiPlayer = AIPlayer(rules)
    aiPlayer.score = 213
    assert str(aiPlayer) == "AI: 213"

def test_AIPlayer_won():
    rules = {}
    aiPlayer = AIPlayer(rules)
    aiPlayer.score = 261
    aiPlayer.won()
    assert aiPlayer.score == 262

def test_AIPlayer_checkCombination_wrong():
    rules = {"keyLength": 2, "numberOfColors": 8}
    combination = "2612023331197"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayer_checkCombination_wrongColors():
    rules = {"keyLength": 8, "numberOfColors": 5}
    combination = "26120231"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayer_checkCombination_wrongLength():
    rules = {"keyLength": 8, "numberOfColors": 6}
    combination = "2023"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayer_checkCombination_correct():
    rules = {"keyLength": 7, "numberOfColors": 9}
    combination = "2612023"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.checkCombination(combination) == True

def test_AIPlayer_answer_0():
    rules = {}
    key = "25026"
    guess = "12023"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.answer(key, guess) == (2, 1)

def test_AIPlayer_answer_1():
    rules = {}
    key = "244"
    guess = "261"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.answer(key, guess) == (1, 0)

def test_AIPlayer_answer_2():
    rules = {}
    key = "20"
    guess = "32"
    aiPlayer = AIPlayer(rules)
    assert aiPlayer.answer(key, guess) == (0, 1)
