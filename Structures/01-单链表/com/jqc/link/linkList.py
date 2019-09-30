# from typing import Callable
# from typing import TypeVar, Generic, NewType
# UserId = NewType('next', Node)
# T = TypeVar('T')


class Node(object):
	def __init__(self, element=None, next_node=None):
		"""
		初始化节点
		:param element: node节点元素
		:param next_node: 当前节点的下一个节点
		"""
		self.element = element
		self.next = next_node
	
	def __str__(self):
		"""
		自定义node节点输出
		:return:
		"""
		return str(self.element)


class LinkList(object):
	
	def __init__(self):
		"""
		单链表初始化
		"""
		# 指向首结点
		self.__fist = None
		# 单链表长度
		self.__size = 0
	
	def __str__(self):
		"""
		自定义输出
		:return:
		"""
		string = 'size=' + str(self.__size) + ", ["
		node = self.__fist
		for i in range(self.__size):
			if i != 0:
				string += ','
			string += str(node.element)
			node = node.next
		string += ']'
		return string
	
	def clear(self):
		"""
		清空链表
		:return:
		"""
		self.__size = 0
		self.__fist = None
	
	def size(self) -> int:
		"""
		返回链表长度
		:return:
		"""
		return self.__size
	
	def is_empty(self):
		"""
		链表是否为空
		:return:
		"""
		return self.__size == 0
	
	def contains(self, element):
		"""
		链表是否包含某个元素
		:param element:
		:return:
		"""
		return self.index_of(element) != -1
	
	def index_of(self, element):
		"""
		返回element在链表中所对应的索引
		:param element:
		:return: 找到返回节点对应的索引; 未找到返回-1;
		"""
		node = self.__fist
		# 遍历节点
		for i in range(self.__size):
			if node.element == element:
				return i
			node = node.next
		return -1
	
	def get(self, index):
		"""
		根据索引获取指定位置的元素
		:param index:
		:return:
		"""
		node = self.__node(index)
		return node.element
	
	def set(self, index, element):
		"""
		修改指定位置的元素
		:param index: 索引
		:param element: 新元素
		:return:
		"""
		# 找到当前节点
		node = self.__node(index)
		old_val = node.element
		# 新值覆盖老值
		node.element = element
		return old_val
	
	def add(self, element):
		"""
		链表增加节点
		:param element: 元素
		"""
		self.insert(self.__size, element)
	
	def insert(self, index, element):
		"""
		在指定位置插入元素
		:param index: 索引
		:param element: 元素
		"""
		self.__range_check_add(index)
		if index == 0:
			# 首次添加 self.__fist 指向首结节点
			self.__fist = Node(element, self.__fist)
		else:
			# 上一个节点
			pre = self.__node(index - 1)
			# 上一个节点的next指向新创建的节点
			pre.next = Node(element, pre.next)
		
		self.__size += 1
	
	def remove(self, index):
		"""
		删除指定位置的节点
		:param index: 索引
		:return: 返回删除节点的元素
		"""
		self.__range_check(index)
		node = self.__fist
		if index == 0:
			# 如果删除的首结点 需要特殊处理
			self.__fist = node.next
		else:
			pre = self.__node(index - 1)
			node = pre.next
			pre.next = node.next
		self.__size -= 1
		return node.element
	
	def __node(self, index):
		"""
		根据索引获取node节点
		:param index:
		:return:
		"""
		self.__range_check(index)
		node = self.__fist
		for i in range(index):
			node = node.next
		return node
	
	def __range_check(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index >= self.__size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))
	
	def __range_check_add(self, index):
		"""
		索引是否越界判断
		:param index:
		:return:
		"""
		if index < 0 or index > self.__size:
			raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))
