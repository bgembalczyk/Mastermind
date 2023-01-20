from mastermind import Mastermind
from exceptions import *

def main():
    """
    Main function starting the Game.
    The Game is divided in any number rounds of mastermind with players swapping encrypting and decrypting.
    Each round is divided in set number of turns with one players guessing and second responding accordingly.
    :return:
    """
    mastermind = Mastermind()
    mastermind.start()
    mastermind.round()
    print(mastermind.score())
    while True:
        userInput = input("Another one?: [Y/N] ")
        try:
            if not userInput:
                raise EmptyInput
            elif userInput not in "ynYN":
                raise InvalidInput
            elif userInput.lower() == "n":
                break
            elif userInput.lower() == "y":
                mastermind.round()
                print(mastermind.score())
        except EmptyInput:
            print("Invalid input. Input cannot be empty.")
        except InvalidInput:
            print("This is not a correct input. Try again.")


if __name__ == '__main__':
    main()
