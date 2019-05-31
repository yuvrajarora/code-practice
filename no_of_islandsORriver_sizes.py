# Given a 2D matrix where 0 represents land and 1 represents water
# Count the number of islands OR return the river sizes

def riverSizes(matrix):

	size = []
	# Auxilary Matrix to store if a node is visited
	visited = [[False for value in row] for row in matrix]

	# Treat the matrix as a graph.
	# When encountered 1, check its neighbors and visit those if not previously visited.

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			if visited[i][j]:
				continue

			traverseNodes(i, j, matrix, visited, size)

	return size #return len for the number of islands

def traverseNodes(i,j,matrix,visited,size):

	currentSize = 0

	nodesToExplore = [[i,j]]

	while len(nodesToExplore) > 0:
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if not matrix[i][j]:
			continue
		currentSize += 1
		unvisitedNeighbor = getUnvisitedNeighbor(i,j,matrix,visited)
		for neighbors in unvisitedNeighbor:
			nodesToExplore.append(neighbors)
	if currentSize >0:
		size.append(currentSize)


def getUnvisitedNeighbor(i,j,matrix,visited):
	unvisitedNeighbor = []
	if i > 0 and not visited[i-1][j]:
		unvisitedNeighbor.append([i-1,j])
	if i < len(matrix) and not visited[i+1][j]:
		unvisitedNeighbor.append([i+1,j])
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbor.append([i,j-1])
	if j < len(matrix[0]) and not visited[i][j+1]:
		unvisitedNeighbor.append([i,j+1])
	return unvisitedNeighbor









