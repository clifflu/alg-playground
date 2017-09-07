
def auc(func, left, right, split_pct=0.01, min_x_interval=0.00001):
    """
    Find area under curve for y = func(x) for x between left and right
    """
    assert right > left

    return _auc(func, left, func(left), right, func(right), split_pct, min_x_interval)

def _auc(func, left, vleft, right, vright, split_pct, min_x_interval):

    if (right - left) < min_x_interval:
        return (vright + vleft) * (right - left) / 2.0

    mid = (right + left) / 2.0
    vmid = func(mid)
    vmid_expected = (vleft + vright) / 2.0

    if abs(vmid - vmid_expected) < abs(vmid) * split_pct:
        return (vright + vleft) * (right - left) / 2.0

    return _auc(func, left, vleft, mid, vmid, split_pct, min_x_interval) + \
        _auc(func, mid, vmid, right, vright, split_pct, min_x_interval)
