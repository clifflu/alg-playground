def _quick(lst, left, right):
    if left >= right:
        return

    pivot_value = lst[left]
    _l, _r = left + 1, right

    while lst[_r] > pivot_value:
        _r -= 1
    # lst[_r] is now <= pivot_value
    # guaranteed to stop as lst[0] = pivot_value is not GT itself

    # in that case, _r = _l = 1, and the following loop would be skipped over
    while _r >= _l:
        if lst[_l] > pivot_value:
            lst[_r], lst[_l] = lst[_l], lst[_r]
            _l += 1
            while lst[_r] > pivot_value:
                _r -= 1
            continue
        _l += 1

    lst[_r], lst[left] = lst[left], lst[_r]
    _quick(lst, left, _r-1)
    _quick(lst, _l, right)


def quick(lst):
    """
    >>> lst = [3, 1, 7, 4]; quick(lst); lst
    [1, 3, 4, 7]
    >>> lst = [3, 3, 4]; quick(lst); lst
    [3, 3, 4]
    >>> lst = [3, 1, 3, 4, 1, 5]; quick(lst); lst
    [1, 1, 3, 3, 4, 5]
    """
    return _quick(lst, 0, len(lst)-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
