def count_in_list(arr: list[str], f: str) -> int:
    """this function will return the number of time
    the string f is found the list l"""
    cnt: int = 0
    for i in arr:
        if i == f:
            cnt += 1
    return cnt
