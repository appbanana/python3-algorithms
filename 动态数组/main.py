# import list.dynamicArray
from list.dynamicArray import DynamicArray

if __name__ == '__main__':
	# array = list.dynamicArray.DynamicArray()
	array = DynamicArray()
	for i in range(20):
		array.add(i)
	
	print(array)
