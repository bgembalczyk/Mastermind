from player import Player
from random import randint
from auxiliaries import *

class AIPlayer(Player):
    """
    Player subclass AIPlayer provides support for computer players, it has set name to 'AI',
    overloaded methods dependent on different difficulty level.
    """
    def __init__(self, rules):
        super().__init__("AI", rules)
        self.difficulties = ["easy", "medium"]

    def createKey(self) -> str:
        """
        This is overloaded Player.createKey() method
        This method creates and return random and accordant to game rule key.
        It's same for different difficulty level
        """
        key = ""
        for i in range(self.rules()["keyLength"]):
            key += str(randint(0, self.rules()["numberOfColors"] - 1))
        return key

    def answer(self, key=None, guess=None) -> tuple:
        """
        This is overloaded Player.answer(key, guess) method
        Using decrypting player's key and encrypting computer player's guess,
        this method returns a tuple with number of red and white pegs.
        Additionally, the tuple is printed in the terminal:
            number of red pegs in red text on black background;
            number of white pegs in white text on black background.
        """
        red, white = compare(guess, key)
        print('\x1b[0;31;40m' + str(red) + '\x1b[0m', '\x1b[0;37;40m' + str(white) + '\x1b[0m')
        return red, white

class AIPlayerEasy(AIPlayer):
    """
    AIPlayer subclass AIPlayerEasy creates a computer player that's guessing always random.
    """
    def __init__(self, rules):
        super().__init__(rules)
        self.difficulty = self.difficulties[0]

    def guess(self) -> str:
        """
        This is overloaded Player.guess() method
        Because the physical player's playing on the easy mode, the computer player always answer random.
        :return: Computer player's guess on easy mode
        """
        AIGuess = ""
        for i in range(self.rules()["keyLength"]):
            AIGuess += str(randint(0, self.rules()["numberOfColors"] - 1))
        return str(AIGuess)

class AIPlayerMedium(AIPlayer):
    """
    AIPlayer subclass AIPlayerMedium creates a computer player that's guessing the colors combinations based on the algorythm.
    The algorythm is based on Donald Knuth's Five guess algorythm, which was made for 4 pegs and 6 colors.
    Typically, the computer player on medium mode is guessing in about 6-8 guesses,
    but it depends on starting combination which is random.
    """
    def __init__(self, rules):
        super().__init__(rules)
        self.difficulty = self.difficulties[1]
        self.guessSet = None

    def createGuessSet(self) -> None:
        """
        This method creates a set representing each possible combination of code.
        """
        self.guessSet = []
        for i in range(0, int(str(self.rules()["numberOfColors"] - 1) * self.rules()["keyLength"]) + 1):
            i = str(i).zfill(self.rules()["keyLength"])
            if not sum(list([int(number) >= self.rules()["numberOfColors"] for number in i])):
                self.guessSet.append(i)
        return

    def updateGuessSet(self) -> None:
        """
        After each answer, the computer player goes through the set of each possible code and crosses out every non-matching ones.
        """
        last = self.prevGuess[-1]
        i = 0
        while i < len(self.guessSet):
            if compare(str(last[0]), str(self.guessSet[i])) != last[1]:
                self.guessSet.pop(i)
            else:
                i += 1
        return

    def guess(self) -> str:
        """
        This is overloaded Player.guess() method
        Because the physical player's playing on the medium mode the computer player's guess is a best guess based on the my algorythm,
        which unfortunately isn't the best way to defeat game of Mastermind.
        The first guess is completely random.
        If the previous guess is totally missed with 0 red and white pegs,
        there's created temporary guess which number on each position is increased and set to all be different.
        Otherwise, the first code in the set AIPlayerMedium.guessSet attribute is returned.
        After getting the guess from the physical player the method AIPlayerMedium.updateGuessSet() is called, 
        which crosses out non-matching codes.
        :return: Computer player's guess on medium mode
        """
        if len(self.prevGuess) != 0:
            self.updateGuessSet()
            if sum(list(sum(i[1]) for i in self.prevGuess)) == 0 or sum(self.prevGuess[-1][1]) == 0:
                tmp = increase(self.prevGuess[-1][0], self.rules()["keyLength"], self.rules()["numberOfColors"] - 1)
                if tmp in self.guessSet:
                    return tmp
                else:
                    while int(tmp) < int(self.guessSet[-1]):
                        tmp = str(int(tmp) + 1).zfill(self.rules()["keyLength"])
                        if tmp in self.guessSet:
                            return tmp
                    return self.guessSet[0]
            else:
                return self.guessSet[0]
        else:
            res = ""
            for i in range(self.rules()["keyLength"]):
                res += str(randint(0, self.rules()["numberOfColors"] - 1))
            return res
