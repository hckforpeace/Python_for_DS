def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]


# def isPos(x: int) -> bool:
#     if x < 0:
#         return False
#     return True
#
#
# res = filter(isPos, [-1, -3, 0, 3, 234, -21])
# res1 = ft_filter(isPos, [-1, -3, 0, 3, 234, -21])
# # res = filter(None, [True, False, False, True])
# # res1 = ft_filter(None, [True, False, False, True])
#
# for i in res1:
#     print(i)
#
#
# for i in res:
#     print(i)
#
# print(filter.__doc__)
# print(ft_filter.__doc__)
