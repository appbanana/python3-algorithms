from com.jqc.map.testModel.person import Person
# import hashlib
# import unittest
import operator

if __name__ == '__main__':
	p1 = Person('abc', 18, 1.78)
	p2 = Person('xyz', 18, 1.80)
	
	# print(p1 == p2)
	# print(hash('abc'))
	# print(hash(99))
	# print(hash(p1))
	# print(hash(p2))
	# print(hash(None))
	print(operator.eq(p1, p2))
	
