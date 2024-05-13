#!/usr/bin/env python3

from person import *


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())
	f.setAge(20)
	print(f.fib_py())
	print(f.fib_numba())

if __name__ == '__main__':
	main()
