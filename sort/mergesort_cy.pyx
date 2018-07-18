"""Rough attempt of Mergesort with C-types."""

cdef merge(L, R, v):
    cdef int i = 0

    while (len(L) > 0 and len(R) > 0):
        if (L[0] < R[0]):
            v[i] = L[0]
            L = L[1:]
        else:
            v[i] = R[0]
            R = R[1:]
        i += 1

    while (len(L) > 0):
        v[i] = L[0]
        L = L[1:]
        i += 1

    while (len(R) > 0):
        v[i] = R[0]
        R = R[1:]
        i += 1

def mergesort(v):
    cdef int split

    if len(v) == 1:
        return v

    split = len(v) // 2
    left = v[:split]
    right = v[split:]
    mergesort(left)
    mergesort(right)
    merge(left, right, v)

    return v