"""
双链表
"""
from .abstractList import AbstractList


class Node(object):
	def __init__(self, element=None, pre_node=None, next_node=None):
		self.element = element
		self.pre = pre_node
		self.next = next_node
	
	def __str__(self):
		return str(self.pre) + "_" + str(self.element) + "_" + str(self.next)


class LinkList(AbstractList):
	
	def __init__(self):
		super().__init__()
		self.__fist = None
		self.__last = None
	
	def clear(self):
		self._size = 0
		self.__fist = None
		self.__last = None
	
	def insert(self, index, element):
		self._range_check_add(index)
		if index == self._size:
			# 能进到这里，可能是第0个 也可能是添加到最后
			old_last = self.__last
			self.__last = Node(old_last, element, None)
			if old_last is None:
				# 第0个元素
				self.__fist = self.__last
			else:
				old_last.next = self.__last
		else:
			next = self.__node(index)
			pre = node.pre
			current = Node(pre, element, next)
			next.pre = current
			
			if pre is None:
				# 如果pre为None 说明是第一个元素
				self.__fist = current
			else:
				pre.next = current
		
		self_size += 1
	
	def __node(self, index):
		"""
		当前index索引和self._size的一半比较 如果小于它的一半 从前往后开始遍历 否则从后往前倒着遍历
		:param index:
		:return:
		"""
		# self._size >> 1 self._size大小右移一位，就是除以2
		half = (self._size >> 1)
		node = self.__fist
		if index < half:
			for i in range(index):
				node = node.next
		else:
			for i in range(self._size-1, index, -1):
				node = node.pre
		return node
