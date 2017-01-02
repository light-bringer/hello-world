def shift_left(lst, n):
    """Shifts the lst over by n indices

    >>> lst = [1, 2, 3, 4, 5]
    >>> shift_left(lst, 2)
    >>> lst
    [3, 4, 5, 1, 2]
    """
    assert (n > 0), "n should be non-negative integer"
    def shift(ntimes):
        if ntimes == 0:
            return
        else:
            temp = lst[0]
            for index in range(len(lst) - 1):
                lst[index] = lst[index + 1]         
            lst[index + 1] = temp
            return shift(ntimes-1)
    return shift(n)

a = "abcd"
print a
b = list(a)
print b
print shift_left(b, 1)
