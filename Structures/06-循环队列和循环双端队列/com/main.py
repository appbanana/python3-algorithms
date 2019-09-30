from com.jqc.stack.stack import Stack
from com.jqc.queue.queue import Queue
from com.jqc.circleQueue.circleQueue import CircleQueue
from com.jqc.circleQueue.circleDeque import CircleDeque


def test1():
	"""
	测试栈
	:return:
	"""
	stack = Stack()
	stack.push(3)
	stack.push(6)
	stack.push(9)
	stack.push(12)
	# 12,9,6,3,
	print(stack)
	# 12
	print(stack.pop())
	# 9,6,3,
	print(stack)
	# 9
	print(stack.top())


def test2():
	"""
	测试队列
	:return:
	"""
	queue = Queue()
	queue.en_queue(3)
	queue.en_queue(6)
	queue.en_queue(9)
	queue.en_queue(12)
	# 3,6,9,12,
	print(queue)
	# 3
	print(queue.de_queue())
	# 6,9,12,
	print(queue)
	# 6
	print(queue.front())


def test3():
	"""
	测试循环队列
	:return:
	"""
	circle_queue = CircleQueue()
	# 循环队列添加10个元素
	for i in range(10):
		circle_queue.en_queue(i)
	# capcacity=10, size=10, 起始索引 front = 0, [0,1,2,3,4,5,6,7,8,9]
	print(circle_queue)
	# 在把前5个出队列
	for i in range(5):
		circle_queue.de_queue()
	# capcacity=10, size=5, 起始索引 front = 5, [None,None,None,None,None,5,6,7,8,9]
	print(circle_queue)
	
	# 扩容后可能会导致元素不对，注意的是扩容后要把索引转化为真实的索引后，在把元素放到新的数组中
	for i in range(10, 20):
		circle_queue.en_queue(i)
	# capcacity=15, size=15, 起始索引 front = 0, [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
	print(circle_queue)


if __name__ == '__main__':
	# test1()
	# test2()
	# test3()
	
	circle_deque = CircleDeque()
	# circle_deque.en_queue_front(0)
	# # capcacity=10, size=1, 起始索引 front = 9, [None,None,None,None,None,None,None,None,None,0]
	# print(circle_deque)
	# circle_deque.en_queue_front(1)
	# # capcacity=10, size=2, 起始索引 front = 8, [None,None,None,None,None,None,None,None,1,0]
	# print(circle_deque)
	
	# for i in range(10):
	# 	circle_deque.en_queue_front(i)
	# # capcacity=10, size=10, 起始索引 front = 0, [9,8,7,6,5,4,3,2,1,0]
	# print(circle_deque)
	
	for i in range(10):
		circle_deque.en_queue_rear(i)
	# capcacity=10, size=10, 起始索引 front = 0, [9,8,7,6,5,4,3,2,1,0]
	print(circle_deque)
	
	for i in range(5):
		circle_deque.de_queue_front()
	# capcacity=10, size=5, 起始索引 front = 5, [None,None,None,None,None,5,6,7,8,9]
	print(circle_deque)
	
	for i in range(9, 6, -1):
		print(circle_deque.de_queue_rear())
		
	print(circle_deque)