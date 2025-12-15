def all_thing_is_obj(object: any) -> int:
    t = type(object)

    if t.__name__ == "list":
        print(t.__name__.capitalize(), ":", t)
    elif t.__name__ == "tuple":
        print(t.__name__.capitalize(), ":", t)
    elif t.__name__ == "set":
        print(t.__name__.capitalize(), ":", t)
    elif t.__name__ == "dict":
        print(t.__name__.capitalize(), ":", t)
    elif t.__name__ == "str":
        print(object, "is in the kitchen :", t)
    else:
        print("Type not found")
    return 42
