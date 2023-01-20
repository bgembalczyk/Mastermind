from AIPlayer import AIPlayerEasy

def test_AIPlayerEasy__init__():
    rules = {}
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer

def test_AIPlayerEasy_name():
    rules = {}
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.name() == "AI"

def test_AIPlayerEasy_rules():
    rules = {"Damping Sphere": 2, "Crawlspace": 3, "Life": "G", "Death": "1B"}
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.rules() == {"Damping Sphere": 2, "Crawlspace": 3, "Life": "G", "Death": "1B"}

def test_AIPlayerEasy__str__():
    rules = {}
    aiPlayer = AIPlayerEasy(rules)
    aiPlayer.score = 171
    assert str(aiPlayer) == "AI: 171"

def test_AIPlayerEasy_won():
    rules = {}
    aiPlayer = AIPlayerEasy(rules)
    aiPlayer.score = 2023
    aiPlayer.won()
    assert aiPlayer.score == 2024

def test_AIPlayerEasy_checkCombination_wrong():
    rules = {"keyLength": 6, "numberOfColors": 2}
    combination = "17012023"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerEasy_checkCombination_wrongColors():
    rules = {"keyLength": 8, "numberOfColors": 5}
    combination = "26120231"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerEasy_checkCombination_wrongLength():
    rules = {"keyLength": 9, "numberOfColors": 6}
    combination = "1521"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerEasy_checkCombination_correct():
    rules = {"keyLength": 5, "numberOfColors": 7}
    combination = "12612"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.checkCombination(combination) == True

def test_AIPlayerEasy_answer_0():
    rules = {}
    key = "15126"
    guess = "11492"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.answer(key, guess) == (1, 2)

def test_AIPlayerEasy_answer_1():
    rules = {}
    key = "612"
    guess = "023"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.answer(key, guess) == (0, 1)

def test_AIPlayerEasy_answer_2():
    rules = {}
    key = "10"
    guess = "82"
    aiPlayer = AIPlayerEasy(rules)
    assert aiPlayer.answer(key, guess) == (0, 0)
