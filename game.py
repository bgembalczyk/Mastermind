from auxiliaries import *
from exceptions import *
from output import display
from player import Player

class Game:
    """
    Class Game supports one game of mastermind with designated encrypting, decrypting players and set of rules.
    """
    def __init__(self, encryptingPlayer, decryptingPlayer, rules):
        self.key = None
        self._encryptingPlayer = encryptingPlayer
        self._decryptingPlayer = decryptingPlayer
        self._rules = rules

    def encryptingPlayer(self) -> Player:
        return self._encryptingPlayer

    def decryptingPlayer(self) -> Player:
        return self._decryptingPlayer

    def rules(self) -> dict:
        return self._rules

    def insertKey(self) -> None:
        self.key = self.encryptingPlayer().createKey()
        return

    def start(self) -> None:
        self.insertKey()
        self.decryptingPlayer().prevGuess = []
        return

    def turn(self, guess) -> tuple:
        """
        !!! self._rules[numberOfTurns] !!!
        Method supporting each turn in one Game of Mastermind, compares guess with the key and returns number of pegs
        :param guess: Player's guess in each turn
        :return: Tuple with numbers of red, white pegs
        """
        correct = compare(guess, self.key)
        while True:
            try:
                red, white = self.encryptingPlayer().answer(self.key, guess)
                if (red, white) == correct:
                    break
                raise GameRulesViolation
            except GameRulesViolation:
                print("This is not a correct answer. Do not cheat!")
        self.decryptingPlayer().prevGuess.append((guess, (red, white)))
        return red, white

    def ifCorrect(self, red) -> bool:
        return red == len(self.key)

    def success(self) -> Player:
        """
        This method is called when the decrypting player cracks the code.
        :return: Reference to object of decrypting player
        """
        print(f"Winner: {self.decryptingPlayer().name()}")
        return self.decryptingPlayer()

    def loss(self) -> Player:
        """
        This method is called when the decrypting player doesn't crack the code.
        :return: Reference to object of encrypting player
        """
        print(f"Winner: {self.encryptingPlayer().name()}")
        return self.encryptingPlayer()

    def end(self) -> None:
        """
        Method called when one game of Mastermind ends.
        At the moment it displays state of the game when it ended in the clear window of the terminal
        """
        display(self.decryptingPlayer().prevGuess, self.rules()["keyLength"], self.rules()["numberOfRounds"])
        del self.decryptingPlayer().prevGuess
        self.decryptingPlayer().prevGuess = []
        if self.decryptingPlayer().name() == "AI":
            if self.decryptingPlayer().difficulty == "medium":
                del self.decryptingPlayer().guessSet
                self.decryptingPlayer().guessSet = []
        return
