import mergesort_py
import mergesort_semi
import mergesort_cy
import numpy
import pytest
import time


def test_pure_python(benchmark):
    result = benchmark(mergesort_py.mergesort, [4,2,9,-1,1,7,2])
    assert result == [-1,1,2,2,4,7,9]

def test_semi_cython(benchmark):
    result = benchmark(mergesort_semi.mergesort, [4,2,9,-1,1,7,2])
    assert result == [-1,1,2,2,4,7,9]

def test_cython(benchmark):
    result = benchmark(mergesort_cy.mergesort, [4,2,9,-1,1,7,2])
    assert result == [-1,1,2,2,4,7,9]

def test_numpy(benchmark):
    result = list(benchmark(numpy.sort, [4,2,9,-1,1,7,2], kind='mergesort'))
    assert result == [-1,1,2,2,4,7,9]

def test_matching_numpy_result():
    my_result = mergesort_py.mergesort([4,2,9,-1,1,7,2])
    np_result = list(numpy.sort(a=[4,2,9,-1,1,7,2], kind='mergesort'))
    assert my_result == np_result