class DynamicArray(object):
	
	def __init__(self, capacity=5):
		self._size = 0  # size
		self.elements = [None] * (5 if capacity < 5 else capacity)
	
	def __str__(self):
		return f"size: {self._size}, capacity: {len(self.elements)}\n{str(self.elements[:self._size])}"
	
	def clear(self):
		"""
		清空
		:return:
		"""
		self.elements = [None for _ in self.elements]
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
		self.insert(self._size, element)
	
	def insert(self, index, element):
		"""
		插入元素
		:param index:
		:param element:
		:return:
		"""
		print(index, self._size)
		self._range_check_add(index)
		self._ensure_capacity(self._size+1)
		for i in range(self._size - 1, index - 1, -1):
			self.elements[i + 1] = self.elements[i]
		self.elements[index] = element
		self._size += 1
	
	def get(self, index=0):
		"""
		根据索引获取元素
		:param index: 索引下标
		:return:
		"""
		self._range_check(index)
		
		return self.elements[index]
	
	def set(self, index, element):
		"""
		更新指定位置的值
		:param index:
		:param element:
		:return: 返回原来的值
		"""
		self._range_check(index)
		old_val = self.elements[index]
		self.elements[index] = element
		return old_val
	
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
	
	def _ensure_capacity(self, capacity):
		"""
		扩容
		:param capacity:
		:return:
		"""
		old_len = len(self.elements)
		if old_len >= capacity:
			return
		new_capacity = old_len + old_len >> 1
		new_data = [None] * new_capacity
		new_data[:self._size] = self.elements[:self._size]
		self.elements = new_data
	
	def _range_check(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index >= self._size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self._size))
	
	def _range_check_add(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index > self._size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self._size))
