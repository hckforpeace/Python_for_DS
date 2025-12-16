import sys as sys


def assert_int(x: any) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        return False
        

def what_is():
    if len(sys.argv) == 1:
        return
    try:
        assert len(sys.argv) == 2, "more than one argument provided"
        assert assert_int(sys.argv[1]), "argument is not an integer"

    except AssertionError as error:
        print("AssertionError:", error)
        return

    x = int(sys.argv[1])
    if x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")



if __name__ == "__main__":
    what_is()
