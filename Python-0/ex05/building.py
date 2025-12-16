import sys as sys


def analyze_string(text: str):
    index = {
        "upper letters": 0,
        "lower letters": 0,
        "punctations marks": 0,
        "spaces": 0,
        "digits": 0,
    }

    for char in text:
        if char.islower():
            index["lower letters"] += 1
        elif char.isupper():
            index["upper letters"] += 1
        elif not char.isalnum() and not char.isspace():
            index["punctations marks"] += 1
        elif char.isspace():
            index["spaces"] += 1
        elif char.isdigit():
            index["digits"] += 1

    print("the text contains", len(text), "characters:")

    for key, value in index.items():
        print(value, key)


if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "more than one argument was provided"
        if len(sys.argv) == 1:
            args = ""
            print("What is the text to count?")
            for line in sys.stdin:
                args += line
            analyze_string(args)
        else:
            analyze_string(sys.argv[1])
    except AssertionError as error:
        print("AssertionError:", error)
