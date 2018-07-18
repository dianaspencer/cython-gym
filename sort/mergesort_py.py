"""Implementation of Mergesort in pure Python."""

def merge(L, R, v):
    i = 0
    while (len(L) > 0 and len(R) > 0):
        if (L[0] < R[0]):
            v[i] = L.pop(0)
        else:
            v[i] = R.pop(0)
        i += 1
    
    while (len(L) > 0):
        v[i] = L.pop(0)
        i += 1
    
    while (len(R) > 0):
        v[i] = R.pop(0)
        i += 1

def mergesort(v):
    if len(v) == 1:
        return v

    split = len(v) // 2
    left = v[:split]
    right = v[split:]
    mergesort(left)
    mergesort(right)
    merge(left, right, v)
    
    return v