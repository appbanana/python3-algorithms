class DynamicArray(object):
	
	def __init__(self, capacity=10):
		self._size = 0  # size
		self.elements = [None] * capacity
	
	def clear(self):
		"""
		清空
		:return:
		"""
		self._size = 0
	
	def size(self):
		"""
		返回动态数组大小
		:return: 返回len(self.elements)
		"""
		return self._size
	
	def is_empty(self):
		"""
		判断数组是否为空
		:return: bool 值
		"""
		return self._size == 0
	
	def contains(self, element):
		"""
		判断是否包含某个元素
		:param element: 元素
		:return:
		"""
		return self.index_of(element) != -1
	
	def add(self, element):
		"""
		添加元素
		:param element:
		:return:
		"""
		pass
	
	def get(self, index=0):
		"""
		根据索引获取元素
		:param index: 索引下标
		:return:
		"""
		pass
	
	def remove(self, index=0):
		"""
		删除指定索引位置的元素
		:param index: 索引
		:return: 返回删除的元素
		"""
		pass
	
	def index_of(self, element):
		"""
		判断element 是否存在
		:param element:
		:return:
		"""
		
		for index, item in enumerate(self.elements):
			if element == item:
				return index
		return -1
	
	def log(func):
		def wrapper(*args, **kw):
			print('call %s():' % func.__name__)
			return func(*args, **kw)
		
		return wrapper
	
	def _range_check(self, index):
		if index < 0 | | index > self._size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self._size))
