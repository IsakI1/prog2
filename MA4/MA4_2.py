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
	n = [num for num in range(20, 31)]
	matplotlib.use('Agg')

	for i in n:
		start = time.perf_counter()
		print(f.fib_py())
		end = time.perf_counter()
		tid = (start-end)
		lista_py.append(tid)
	pylab.plot(n,lista_py)
	pylab.savefig("test")

	#print(f.fib_numba())

if __name__ == '__main__':
	main()
