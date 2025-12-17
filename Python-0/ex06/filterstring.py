import sys as sys
from ft_filter import ft_filter


def filterstring(text: list[str], size: int):
    """Function that filters a string and retreives the words of length
(size)"""
    res = ft_filter(lambda x: len(x) == size, text)
    for r in res:
        print(r)


if __name__ == "__main__":
    args = sys.argv
    try:
        assert len(args) == 3, (
            "Wrong number of arguments, the program needs 2 \
            arguments: \"text\" size"
        )
        size = int(args[2])
        assert size > 0, "Second argument must be positive"

        textList = args[1].split(" ")
        filterstring(textList, size)
    except AssertionError as error:
        print("AssertionError:", error)
    except ValueError as error:
        print(error)
