from AIPlayer import AIPlayerMedium

def test_AIPlayerMedium__init__():
    rules = {}
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer

def test_AIPlayerMedium_name():
    rules = {}
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.name() == "AI"

def test_AIPlayerMedium_rules():
    rules = {"Terror": "1B", "Street Wraith": "3BB", "Royal Assassin": "1BB", "Oversold Cemetery": 1}
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.rules() == {"Terror": "1B", "Street Wraith": "3BB", "Royal Assassin": "1BB", "Oversold Cemetery": 1}

def test_AIPlayerMedium__str__():
    rules = {}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.score = 95
    assert str(aiPlayer) == "AI: 95"

def test_AIPlayerMedium_won():
    rules = {}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.score = 82
    aiPlayer.won()
    assert aiPlayer.score == 83

def test_AIPlayerMedium_checkCombination_wrong():
    rules = {"keyLength": 8, "numberOfColors": 1}
    combination = "79"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerMedium_checkCombination_wrongColors():
    rules = {"keyLength": 8, "numberOfColors": 7}
    combination = "67636261"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerMedium_checkCombination_wrongLength():
    rules = {"keyLength": 5, "numberOfColors": 9}
    combination = "5654"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.checkCombination(combination) == False

def test_AIPlayerMedium_checkCombination_correct():
    rules = {"keyLength": 4, "numberOfColors": 8}
    combination = "4575"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.checkCombination(combination) == True

def test_AIPlayerMedium_answer_0():
    rules = {}
    key = "50123"
    guess = "75156"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.answer(key, guess) == (1, 1)

def test_AIPlayerMedium_answer_1():
    rules = {}
    key = "301"
    guess = "610"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.answer(key, guess) == (0, 2)

def test_AIPlayerMedium_answer_2():
    rules = {}
    key = "30"
    guess = "16"
    aiPlayer = AIPlayerMedium(rules)
    assert aiPlayer.answer(key, guess) == (0, 0)

def test_AIPlayerMedium_createGuessSet_0():
    rules = {"keyLength": 2, "numberOfColors": 3}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.createGuessSet()
    assert aiPlayer.guessSet == ["00", "01", "02", 
                                 "10", "11", "12",
                                 "20", "21", "22"]

def test_AIPlayerMedium_createGuessSet_1():
    rules = {"keyLength": 3, "numberOfColors": 2}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.createGuessSet()
    assert aiPlayer.guessSet == ["000", "001", "010", "011",
                                 "100", "101", "110", "111"]

def test_AIPlayerMedium_createGuessSet_2():
    rules = {"keyLength": 2, "numberOfColors": 5}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.createGuessSet()
    assert aiPlayer.guessSet == ["00", "01", "02", "03", "04", 
                                 "10", "11", "12", "13", "14",
                                 "20", "21", "22", "23", "24",
                                 "30", "31", "32", "33", "34",
                                 "40", "41", "42", "43", "44"]

def test_AIPlayerMedium_updateGuessSet():
    rules = {"keyLength": 5, "numberOfColors": 7}
    aiPlayer = AIPlayerMedium(rules)
    aiPlayer.createGuessSet()
    aiPlayer.prevGuess = [["52501", (2, 3)]]
    aiPlayer.updateGuessSet()
    listTmp = ["52015", "50512", "51205", "55021",
               "52150", "51520", "55102", "50251",
               "02515", "12550", "15502", "05521",
               "21505", "20551"]
    listTmp.sort()
    assert aiPlayer.guessSet == listTmp
