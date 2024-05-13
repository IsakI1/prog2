""" Python interface to the C++ Person class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')
from numba import jit, types


class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]
		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_getAge.argtypes = [ctypes.c_void_p]
		lib.Person_getAge.restype = ctypes.c_int
		lib.Person_setAge.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_getDecades.argtypes = [ctypes.c_void_p]
		lib.Person_getDecades.restype = ctypes.c_double
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def getAge(self):
		return lib.Person_getAge(self.obj)

	def setAge(self, age):
		lib.Person_setAge(self.obj, age)

	def getDecades(self):
		return lib.Person_getDecades(self.obj)
        
	def __del__(self):
		return lib.Person_delete(self.obj)
	
	
	def fib_py(self, n=None):
		if n is None:
			n = self.getAge()
		if n <= 1:
			return n
		else:
			return self.fib_py(n-1) + self.fib_py(n-2)
		
	@jit
	def fib_numba(self, n=None):
		if n is None:
			n = self.getAge()
		if n <= 1:
			return n
		else:
			return self.fib_py(n-1) + self.fib_py(n-2)

