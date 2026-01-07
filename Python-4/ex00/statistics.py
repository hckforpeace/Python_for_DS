def var(*args: any):
    assert len(args) != 0, "ERROR"
    avg = mean(*args)
    num = 0
    for arg in args:
        num += (arg - avg) ** 2
    return float(num / len(args))


def mean(*args: any):
    assert len(args) != 0, "ERROR"

    avg = 0
    for arg in args:
        assert isinstance(arg, int), "ERROR"
        avg = avg + arg

    return avg / len(args)


def median(*args):
    assert len(args) != 0, "ERROR: No values provided"

    args_list = list(args)
    args_list.sort()

    length = len(args_list)

    if length % 2 == 1:
        med = args_list[length // 2]
    else:
        med = (args_list[length // 2] + args_list[(length // 2) - 1]) / 2

    return med


def quartile(*args):
    assert len(args) != 0, "ERROR"
    sorted_list = sorted(args)
    n = len(sorted_list)

    if n % 2 == 0:
        lower_half = sorted_list[: n // 2]
        upper_half = sorted_list[n // 2:]
    else:
        # Include median in both halves for Tukey method
        lower_half = sorted_list[: n // 2 + 1]
        upper_half = sorted_list[n // 2:]

    q1 = float(median(*lower_half))
    q3 = float(median(*upper_half))
    return [q1, q3]


def ft_statistics(*args: any, **kwargs: any) -> None:
    for k, v in kwargs.items():
        try:
            display_stats(v, *args)
        except AssertionError:
            print("ERROR")


def display_stats(statname: any, *args: any):
    if statname == "mean":
        print(f"mean : {mean(*args)}")
    elif statname == "median":
        print(f"median : {median(*args)}")
    elif statname == "quartile":
        print(f"quartile : {quartile(*args)}")
    elif statname == "std":
        print(f"std : {var(*args) ** 0.5}")
    elif statname == "var":
        print(f"var : {var(*args)}")
