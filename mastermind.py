from game import Game
from player import Player
from AIPlayer import AIPlayerEasy, AIPlayerMedium
from exceptions import *
from output import *

class Mastermind:
    """
    This class supports whole gameplay.
    The attribute game contains object of class Game which supports one round of mastermind.
    """
    def __init__(self):
        self.game = None
        self.gameIndex = 0
        self.players = None
        self._rules = None

    def rules(self) -> dict:
        return self._rules

    def inputRules(self) -> None:
        """
        This method runs during initialization of class and handles setting rules of each mastermind game.
        This set of rules is held in attribute _rules
        """
        self._rules = {}
        while True:
            try:
                self._rules["numberOfPlayers"] = int(input("Enter number of players: [1-2] "))
                if not 1 <= self.rules()["numberOfPlayers"] <= 2:
                    raise InvalidRangeInput(1, 2)
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, number not in range. Try again.")
        while True:
            try:
                self._rules["numberOfRounds"] = int(input("Enter number of rounds in a game: [1-15] "))
                if not 1 < self.rules()["numberOfRounds"] < 15:
                    raise InvalidInput
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, it has to be at least one round. Try again.")
        while True:
            try:
                self._rules["keyLength"] = int(input("Enter key length: [2-6] "))
                if not 2 <= self.rules()["keyLength"] <= 6:
                    raise InvalidRangeInput(2, 6)
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, number not in range. Try again.")
        while True:
            try:
                self._rules["numberOfColors"] = int(input("Enter number of colors: [2-8] "))
                if not 2 <= self.rules()["numberOfColors"] <= 8:
                    raise InvalidRangeInput(2, 8)
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, number not in range. Try again.")
        if self.rules()["numberOfPlayers"] == 1:
            while True:
                try:
                    self._rules["difficultyLevel"] = int(input("Enter difficulty level: [1-2] "))
                    if not 1 <= self.rules()["difficultyLevel"] <= 2:
                        raise InvalidRangeInput(1, 2)
                    else:
                        break
                except ValueError:
                    print("Incorrect input, not a number. Try again.")
                except InvalidRangeInput:
                    print("Incorrect input, number not in range. Try again.")
        return

    def start(self) -> None:
        """
        After initialization this is a proper method starting the round of Mastermind.
        It inputs the players names and checks if they're correct.
        """
        self.players = []
        for playerNum in range(self.rules()["numberOfPlayers"]):
            while True:
                try:
                    name = input(f"Enter Player {playerNum + 1}'s name: ")
                    if name == "AI":
                        raise RestrictedInput
                    elif name:
                        break
                    raise EmptyInput
                except RestrictedInput:
                    print("'AI' cannot be used as player's name")
                except EmptyInput:
                    print("Invalid input. Name of the player cannot be empty.")
            self.players.append(Player(name, self.rules()))
        if self.rules()["numberOfPlayers"] == 1:
            if self.rules()["difficultyLevel"] == 1:
                self.players.append(AIPlayerEasy(self.rules()))
            elif self.rules()["difficultyLevel"] == 2:
                self.players.append(AIPlayerMedium(self.rules()))
        return

    def round(self) -> None:
        """
        Method supporting game of Mastermind.
        It swaps encrypting and decrypting player, it operates players' guesses and answers.
        After every turn this method checks if the Game is won or should it be continued.
        """
        if self.rules()["numberOfPlayers"] == 1 and self.rules()["difficultyLevel"] == 2:
            self.players[-1].createGuessSet()
        if self.gameIndex % 2 == 0:
            self.game = Game(self.players[0], self.players[1], self.rules())
        else:
            self.game = Game(self.players[1], self.players[0], self.rules())
        self.game.start()
        for i in range(self.rules()["numberOfRounds"]):
            playerGuess = self.game.decryptingPlayer().guess()
            displayBoard(self.game.decryptingPlayer().prevGuess)
            print(displayGuess(playerGuess))
            turn = self.game.turn(playerGuess)
            if self.game.ifCorrect(turn[0]):
                self.game.success().won()
                self.gameIndex += 1
                self.game.end()
                return
        self.game.loss().won()
        self.gameIndex += 1
        self.game.end()
        return

    def score(self) -> str:
        """
        Method printing players score after each game of Mastermind.
        """
        result = ""
        for player in self.players:
            result += str(player) + "\n"
        return result
