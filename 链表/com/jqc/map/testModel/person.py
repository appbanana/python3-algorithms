# https://blog.csdn.net/anlian523/article/details/80910808
class Person(object):
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
	
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__class__.__name__ != other.__class__.__name__
		else:
			return False
	
	# def __eq__(self, other):
	# 	return self.age == other.age
	
	def __hash__(self) -> int:
		hash_code = hash(self.age)
		hash_code += hash_code * 31 + hash(self.height)
		hash_code += hash_code * 31 + hash(self.name if self.name else 0)
		return hash(self.age)
