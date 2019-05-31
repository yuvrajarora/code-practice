# Depth First Search
class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))

	# will run in O(v+e) time and O(v) space
	def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array

def main():
	node = Node(5)
	node1 = Node(2)
	node.addChild(7)
	node1.addChild(8)
	print(node.depthFirstSearch([]))

if __name__ == '__main__':
	main()