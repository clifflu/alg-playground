def bin_search(find, lst):
    """

    >>> bin_search(0, [0, 1])
    0

    >>> bin_search(1, [0, 1])
    1

    >>> bin_search(2, [0, 1])
    -1

    >>> bin_search(0, [0, 1, 2])
    0

    >>> bin_search(1, [0, 1, 2])
    1

    >>> bin_search(2, [0, 1, 2])
    2

    >>> bin_search(3, [0, 1, 3, 5])
    2

    >>> bin_search(4, [0, 1, 3, 5])
    -1
    """

    left, right = 0, len(lst) - 1
    while (right >= left):
        mid = (left + right) // 2
        if lst[mid] == find:
            return mid

        if lst[mid] > find:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
