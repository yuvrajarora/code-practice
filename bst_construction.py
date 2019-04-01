class BST:
	# constructor for BST class
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

	#insert function for BST
	def insert(self,value):
		current_node = self
		while True:
			if value < current_node.value:
				if current_node is None:
					current_node.left = BST(value)
					break
				else:
					current_node = current_node.left
			else:
				if current_node is None:
					current_node.right = BST(value)
					break
				else:
					current_node = current_node.right
	# checks if a key is present in the BST or not
	def contains(self,key):
		current_node = self
		while current_node is not None:
			if key < current_node.value:
				current_node = current_node.left
			elif key > current_node.value:
				current_node = current_node.right
			else:
				return True
		return False

if __name__ == "__main__":
	first = BST(20)
	second = BST(30)
	third = BST(10)
	first.right = second
	first.left = third
	print(first.contains(2))
	first.insert(2)
