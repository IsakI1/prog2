#!/usr/bin/env python3

from person import *
import time
from matplotlib import pyplot as plt
import matplotlib
import pylab

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())
	f.setAge(20)

	lista_py = []
	lista_cpp = []
	lista_numba = []
	n = [num for num in range(20, 30)]
	matplotlib.use('Agg')
	
	"""
	for i in n:
		start = time.perf_counter()
		f.setAge(i)
		print(f.fib_py())
		end = time.perf_counter()
		tid = (end-start)
		lista_py.append(tid)
	
	for i in n:
		start = time.perf_counter()
		f.setAge(i)
		print(f.fib_cpp())
		end = time.perf_counter()
		tid = (end-start)
		lista_cpp.append(tid)
	
	"""
	for i in n:
		start = time.perf_counter()
		f.setAge(i)
		print(fib_numba())
		end = time.perf_counter(i)
		tid = (end-start)
		lista_numba.append(tid)
	"""
	start = time.perf_counter()
	f.fib_cpp(47)
	end = time.perf_counter()
	tid = end-star
	print('n = 47 för c++ tid: ',tid)
	"""

	#pylab.plot(n,lista_py)
	#pylab.plot(n,lista_numba)
	#pylab.plot(n,lista_cpp)
	#pylab.savefig("test")

	#print(f.fib_numba())

if __name__ == '__main__':
	main()
