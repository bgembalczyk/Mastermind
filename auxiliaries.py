def increase(word, n, maxC) -> str:
    """
    Auxiliary function which takes string holding numbers and increasing number on each of position by parameter n;
    if set number is bigger than maxC, it's limited to maxC
    :param word: string holding numbers corresponding to guess
    :param n: number of times numbers in word should be increased
    :param maxC: parameter corresponding to number of colors in the game of Mastermind
    :return: string of numbers
    """
    result = ""
    for letter in word:
        resLetter = letter
        for i in range(n):
            if resLetter < str(maxC):
                resLetter = chr(ord(resLetter) + 1)
            else:
                resLetter = "0"
        while resLetter in result:
            if resLetter < str(maxC):
                resLetter = chr(ord(resLetter) + 1)
            else:
                resLetter = "0"
        result += resLetter
    return result

def compare(guess, key) -> tuple:
    """
    Auxiliary function ultimately used to comparing first player's guess with second player's key
    """
    red, white = 0, 0
    restOfGuess = ""
    restOfKey = ""
    for i, letter in enumerate(guess):
        if letter == key[i]:
            red += 1
        else:
            restOfGuess += letter
            restOfKey += key[i]
    for letter in restOfGuess:
        if letter in restOfKey:
            white += 1
            restOfKey = restOfKey[:restOfKey.find(letter)] + restOfKey[restOfKey.find(letter) + 1:]
    return red, white
