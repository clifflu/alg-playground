"""
max heap
"""

def parentIdx(idx):
    """
    >>> parentIdx(1)
    0
    >>> parentIdx(2)
    0
    >>> parentIdx(3)
    1
    >>> parentIdx(4)
    1
    """
    return (idx - 1) // 2

def childIdx(idx):
    """
    >>> childIdx(0)
    (1, 2)
    >>> childIdx(1)
    (3, 4)
    >>> childIdx(2)
    (5, 6)
    """
    base = idx * 2
    return (base + 1, base + 2)

def swap(lst, idx1, idx2):
    """
    >>> swap([0, 1, 2], 0, 1)
    [1, 0, 2]
    >>> swap([0, 1, 2], 0, 0)
    [0, 1, 2]
    """
    # print("Swapping [{}, {}] from {}".format(idx1, idx2, lst))
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    # print("resulting to {}".format(lst))
    return lst


def heapPop(lst):
    """
    >>> lst = [3, 2, 1]; [heapPop(lst), lst]
    [3, [2, 1]]
    >>> lst = [2, 1]; [heapPop(lst), lst]
    [2, [1]]
    >>> lst = [1]; [heapPop(lst), lst]
    [1, []]
    >>> lst = []; [heapPop(lst), lst]
    [None, []]
    """

    if not lst:
        return None

    if len(lst) == 1:
        return lst.pop()

    output, lst[0] = lst[0], lst.pop()
    last_idx = len(lst) - 1
    _i = 0

    while _i <= last_idx:
        _clarge = -1
        for _c in childIdx(_i):
            if _c > last_idx:
                continue
            if _clarge != -1 and lst[_clarge] > lst[_c]:
                pass # _clarge exists and is larger, keep it
            else:
                _clarge = _c

        if _clarge == -1:
            break # heapify complete

        swap(lst, _clarge, _i)
        _i = _clarge

    return output


def heapify(lst):
    """
    >>> heapify([0, 1])
    [1, 0]
    >>> heapify([3, 2, 1])
    [3, 2, 1]
    >>> heapify([0, 1, 2, 3])
    [3, 2, 1, 0]
    """
    for idx in range(1, len(lst)):
        _i = idx
        while _i > 0:
            _p = parentIdx(_i)
            if (lst[_i] <= lst[_p]):
                break

            swap(lst, _i, _p)
            _i = _p

    return lst

def heapSort(lst):
    """
    >>> heapSort([3, 7, 4, 2, 1])
    [7, 4, 3, 2, 1]
    >>> heapSort([1])
    [1]
    >>> heapSort([])
    []
    """
    heapify(lst)
    return [heapPop(lst) for _ in range(len(lst))]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
