# remove duplicates from an unsorted linked list
# how to solve if a temp. buffer not allowed?

# Approach:
# 1. Use a hash set. Add each element of the list to hash table.
#	 if the element is seen again, then skip that element.
#	 Will run in O(n) time and need O(n) extra space to store elements
# 2. If extra space not allowed:
#	 Use two pointers technique. 
#	 point to a node with first pointer and using second pointer compare each 
#	 element with the first one. If same then skip that element. Continue iterating till Null.

class Node:

	def __init__(self, value):
		self.data = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def remove_duplicates_hash(self,head):
		hashSet = set()
		current = head
		previous = None
		while current is not None:
			if current.data in hashSet:
				previous.next = current.next
			else:
				hashSet.add(current.data)
				previous = current
			current = current.next

	def remove_duplicates_dbl_ptr(self,head):
		current = head
		while current is not None:
			runner = current
			while runner.next is not None:
				if runner.next.data == current.data:
					runner.next = runner.next.next
				else:
					runner = runner.next
			current = current.next


	def print_list(self):
	    curr = self.head
	    while(curr != None):
	        print(curr.data)
	        curr = curr.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(8)
    first = Node(3)
    second = Node(5)
    third = Node(8)
    fourth = Node(10)
    llist.head.next = first
    first.next = second
    second.next = third
    third.next = fourth
    llist.remove_duplicates_hash(llist.head)
    llist.remove_duplicates_dbl_ptr(llist.head)
    llist.print_list()


