# from asyncio.windows_events import NULL
from math import nan


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    if isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
        return 0
    if isinstance(object, bool) and object is False:
        print("Fake:", object, type(object))
        return 0
    if isinstance(object, int) and object == 0:
        print("Zero:", object, type(object))
        return 0
    if isinstance(object, str) and object == "":
        print("Empty:", object, type(object))
        return 0

    print("Type not Found")

    return 1
