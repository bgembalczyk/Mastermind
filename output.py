import curses
from terminedia import pause

def displayGuess(word) -> str:
    """
    This function display one row of guess to terminal using 8-bit colors.
    :param word: key/guess in the form of string
    :return: string with appropriate format to display color rectangles in terminal
    """
    res = ""
    for number in word:
        tmp = ';'.join(["1", str(30 + int(number)), str(40 + int(number))])
        res += '\x1b[%sm %s \x1b[0m' % (tmp, number)
    return res


def displayBoard(prevGuess) -> None:
    for row in prevGuess:
        print(displayGuess(row[0]), '\x1b[0;31;40m' + str(row[1][0]) + '\x1b[0m', '\x1b[0;37;40m' + str(row[1][1]) + '\x1b[0m')
    return

def display(prevGuess, keyLength, numberOfRounds) -> None:
    """
    Function displaying whole Mastermind board and pegs in the new window of terminal
    :param prevGuess: Reference to class Player attribute based on which Mastermind board is draw
    :param keyLength: Width of Mastermind board
    :param numberOfRounds: Height of Mastermind board
    """
    def pbar(window) -> None:
        """
        Auxiliary functions supporting window service
        """
        window.clear()
        curses.start_color()
        colors = [curses.COLOR_BLACK,
                  curses.COLOR_RED,
                  curses.COLOR_GREEN,
                  curses.COLOR_YELLOW,
                  curses.COLOR_BLUE,
                  curses.COLOR_MAGENTA,
                  curses.COLOR_CYAN,
                  curses.COLOR_WHITE]
        for i, color in enumerate(colors):
            curses.init_pair(i + 1, curses.COLOR_BLACK, color)

        x, y = 5, 10
        for i in range(numberOfRounds):
            for j in range(keyLength):
                window.addstr(x - 1 + i * 3, y - 2 + j * 6, "X" * 6, curses.color_pair(8))
                window.addstr(x + i * 3, y - 2 + j * 6, "X" * 2, curses.color_pair(8))
                window.addstr(x + 1 + i * 3, y - 2 + j * 6, "X" * 2, curses.color_pair(8))
            window.addstr(x + i * 3 - 1, y + (keyLength + 1) * 5 - 3, "X" * 2, curses.color_pair(8))
            window.addstr(x + i * 3, y + (keyLength + 1) * 5 - 3, "X" * 2, curses.color_pair(8))
            window.addstr(x + i * 3 + 1, y + (keyLength + 1) * 5 - 3, "X" * 2, curses.color_pair(8))
        window.addstr(x + 3 * numberOfRounds - 1, y - 2, "X" * (6 * keyLength + 2), curses.color_pair(8))
        window.refresh()

        for i, row in enumerate(prevGuess):
            for j, num in enumerate(row[0]):
                window.addstr(x + i * 3, y + j * 6, " " * 4, curses.color_pair(int(num) + 1))
                window.addstr(x + i * 3 + 1, y + j * 6, " " * 4, curses.color_pair(int(num) + 1))
            for k in range(sum(row[1])):
                if k < row[1][0]:
                    window.addstr(x + i * 3 + 1 * (k > 1), y + keyLength * 6 + 3 + 2 * (k % 2 == 1), str(k + 1) * 2, curses.color_pair(2))
                elif row[1][0] <= k < sum(row[1]):
                    window.addstr(x + i * 3 + 1 * (k > 1), y + keyLength * 6 + 3 + 2 * (k % 2 == 1), str(k + 1 - row[1][0]) * 2, curses.color_pair(8))

        window.addstr(50, 50, "")
        window.refresh()
        pause()
        return

    curses.wrapper(pbar)
    return
