import sys as sys


def print_text_to_morse(message: str):
    """This functions displays a string of alpha-numeric
characters and spaces to morse code"""
    message = message.lower()
    morse = {
        "a": ".-",
        "b": "-..",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "..-",
        "w": "...-",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }
    for i, c in enumerate(message):
        if i != len(message) - 1:
            print(morse[c], end=" ")
        else:
            print(morse[c])


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        assert all(x.isalnum() or x.isspace() for x in sys.argv[1]), (
            "the arguments are bad"
        )
        print_text_to_morse(sys.argv[1])
    except AssertionError as error:
        print("AssertionError:", error)
