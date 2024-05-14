""" Python interface to the C++ Person class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')
from numba import njit, types

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
		lib.Person_fib_cpp.argtypes = [ctypes.c_void_p]
		lib.Person_fib_cpp.restype = ctypes.c_int
		lib.Person_fib_cpp_helper.argtypes = [ctypes.c_void_p, ctypes.c_int]
		lib.Person_fib_cpp_helper.restype = ctypes.c_int
	def getAge(self):
		return lib.Person_getAge(self.obj)

	def setAge(self, age):
		lib.Person_setAge(self.obj, age)

	def getDecades(self):
		return lib.Person_getDecades(self.obj)
        
	def __del__(self):
		return lib.Person_delete(self.obj)
	
	def fib_cpp(self):
		return lib.Person_fib_cpp(self.obj)
	
	def fib_py(self, n=None):
		if n is None:
			n = self.getAge()
		if n <= 1:
			return n
		else:
			return self.fib_py(n-1) + self.fib_py(n-2)

	
			

def fib_numba(person: Person) -> int:
	n = person.getAge()
	return fib_numba_helper(n)

@njit
def fib_numba_helper(n: int) -> int:
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)