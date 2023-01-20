from exceptions import *
from output import *

class Player:
    """
    Class Players provides support for physical and computer players.
    It keeps players' name, score and other attributes required for game to happen
    """
    def __init__(self, name, rules):
        self._name = name
        self.score = 0
        self.prevGuess = []
        self._rules = rules

    def name(self) -> str:
        return self._name

    def rules(self) -> dict:
        return self._rules

    def __str__(self) -> str:
        """
        :return: string with player name and score
        """
        return f"{self.name()}: {self.score}"

    def won(self) -> None:
        self.score += 1
        return

    def checkCombination(self, combination) -> bool:
        """
        This method checks if the combination of colors provided by the player is possible and correct in the term of game rules.
        :param combination: string representing different colors
        """
        if len(combination) != self.rules()["keyLength"]:
            return False
        for number in combination:
            if int(number) >= self.rules()["numberOfColors"]:
                return False
        return True

    def createKey(self) -> str:
        """
        This method is used only for physical players. The AI player has overloaded version of it.
        It supports physical encrypting player to input theirs key into the game.
        The key is then checked if it's proper for set before game rules.
        :return: key, for decrypting player to guess
        """
        while True:
            try:
                key = input(f"{self.name()} is entering theirs key: ")
                if len(key) != self.rules()["keyLength"]:
                    raise GameRulesViolation
                key = int(key)
                if not self.checkCombination(str(key).zfill(self.rules()["keyLength"])):
                    raise GameRulesViolation
                elif key < 0:
                    raise NegativeInput
                else:
                    break
            except ValueError:
                print("This is not a valid key. Try again.")
            except GameRulesViolation:
                print("This is not a valid key. Try again.")
            except NegativeInput:
                print("This is not a valid key. Try again.")
        key = str(key).zfill(self.rules()["keyLength"])
        print(displayGuess(key))
        print("\n")
        return key

    def guess(self) -> str:
        """
        This method is used only for physical players. The AI player has overloaded version of it.
        It supports physical decrypting player to input theirs guess each round into the game.
        The guess is then checked if it's proper for set before game rules.
        :return: Player's guess in held in string with leading zeros if needed.
        """
        while True:
            try:
                tmp = input(f"{self.name()} is entering theirs guess: ")
                playerGuess = int(tmp)
                if not self.checkCombination(str(playerGuess).zfill(self.rules()["keyLength"])):
                    raise GameRulesViolation
                elif playerGuess < 0:
                    raise NegativeInput
                elif len(tmp) != self.rules()["keyLength"]:
                    raise GameRulesViolation
                else:
                    break
            except ValueError:
                print("This is not a valid key. Try again.")
            except GameRulesViolation:
                print("This is not a valid key. Try again.")
            except NegativeInput:
                print("This is not a valid key. Try again.")
        return str(playerGuess).zfill(self.rules()["keyLength"])

    def answer(self, key=None, guess=None) -> tuple:
        """
        This method is used only for physical players. The AI player has overloaded version of it.
        It supports physical encrypting player to input answer with the number of red and white pegs.
        The answer is then checked if it's proper for set before game rules.
        :param key: Both parameters are here for being compatible with subclass AI overloaded method.
        :param guess: --||--
        """
        while True:
            try:
                red = int(input(f"{self.name()} is entering number of red pegs: "))
                if not 0 <= red <= self.rules()["keyLength"]:
                    raise InvalidRangeInput(1, self.rules()["keyLength"])
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, number not in range. Try again.")
        while True:
            try:
                white = int(input(f"{self.name()} is entering number of white pegs: "))
                if not 0 <= white <= self.rules()["keyLength"] - red:
                    raise InvalidRangeInput(1, self.rules()["keyLength"] - red)
                else:
                    break
            except ValueError:
                print("Incorrect input, not a number. Try again.")
            except InvalidRangeInput:
                print("Incorrect input, number not in range. Try again.")
        return red, white
