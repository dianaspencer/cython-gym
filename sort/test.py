from timeit import timeit
from numpy import sort
import mergesort_py
import mergesort_semi
import mergesort_cy

print("Testing Mergesort Algorithm")
print("----")

print("Pure Python: {}".format(mergesort_py.mergesort([4,2,9,-1,1,7,2])))
print("Semi Cython: {}".format(mergesort_semi.mergesort([4,2,9,-1,1,7,2])))
print("Cython: {}".format(mergesort_cy.mergesort([4,2,9,-1,1,7,2])))
print("Numpy: {}".format(sort(a=[4,2,9,-1,1,7,2], kind='mergesort')))

N = 1000
print("")
print("Running algorithm {} times".format(N))
print("----")
pt = timeit("mergesort_py.mergesort([4,2,9,-1,1,7,2])", setup="import mergesort_py", number=N)
st = timeit("mergesort_semi.mergesort([4,2,9,-1,1,7,2])", setup="import mergesort_semi", number=N)
ct = timeit("mergesort_cy.mergesort([4,2,9,-1,1,7,2])", setup="import mergesort_cy", number=N)
nt = timeit("sort(a=[4,2,9,-1,1,7,2], kind='mergesort')", setup="from numpy import sort", number=N)

print("-> Pure Python: {:.5f}".format(pt))
print("-> Semi Cython: {:.5f}".format(st))
print("-> Cython: {:.5f}".format(ct))
print("-> Numpy: {:.5f}".format(nt))

print("")
print("Semi Cython is {:.4f} times faster than pure Python".format(pt/st))
print("Cython is {:.4f} times faster than pure Python".format(pt/ct))
print("Cython is {:.4f} times faster than Numpy's mergesort".format(nt/ct))