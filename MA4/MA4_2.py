#!/usr/bin/env python3

from person import Person
from person import fib_py


def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

if __name__ == '__main__':
	main()
