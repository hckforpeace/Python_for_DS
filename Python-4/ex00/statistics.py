
def display_average(*args: any):
    try:
        assert len(args) != 0, "ERROR"

        avg = 0
        for arg in args:
            assert isinstance(arg, int), "ERROR"
            avg = avg + arg 

        print(f"mean : {avg / len(args)}")
    except AssertionError as error:
        print("ERROR")


def display_median(*args: any):
    try:
        assert len(args) != 0, "ERROR"
        args_list = list(args)
        args_list.sort()
        if len(args_list) % 2 == 1:
            med = args_list[(len(args_list) // 2)]
        else:
            med = (args_list[(len(args_list) // 2)] + args_list[(len(args_list) // 2) - 1]) / 2

        print(f"median : {med}")


    except AssertionError as error:
        print("ERROR")

def display_quartile(*args):
    sorted_list = sorted(args)
    n = len(sorted_list)
    
    # Simple method: multiply position by index range
    q1_index = int(0.25 * (n - 1))
    q3_index = int(0.75 * (n - 1))
    
    q1 = float(sorted_list[q1_index])
    q3 = float(sorted_list[q3_index])
    
    print(f"quartile : [{q1}, {q3}]")

def ft_statistics(*args: any, **kwargs: any) -> None:
    for k, v in kwargs.items():
        if (v == 'mean'):
            display_average(*args)
        elif v == 'median':
            display_median(*args)
            
        elif v == 'quartile':
            display_quartile(*args)
        # elif v == 'std':
        # elif v == 'var':
        #
        #

# 1. 11. 42. 43. 64. 360
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
