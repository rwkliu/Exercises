# Python3 Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 5

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pair shortest path
# via Floyd Warshall Algorithm

def floydWarshall(graph):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	for k in range(V):

		# pick all vertices as source one by one
		for i in range(V):

			# Pick all vertices as destination for the
			# above picked source
			for j in range(V):

				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

		print("k: ",k)
		printSolution(dist)

# A utility function to print the solution
def printSolution(dist):
	print("Following matrix shows the shortest distances\
 between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print("%7s" % ("INF"), end=" ")
			else:
				print("%7d\t" % (dist[i][j]), end=' ')
			if j == V-1:
				print()

if __name__ == "__main__":
	graph = [[0, 4, INF, 5, INF],
			     [INF, 0, 1, INF, 6],
			     [2, INF, 0, 3, INF],
			     [INF, INF, 1, 0, 2],
					 [1, INF, INF, 4, 0]
					]

	floydWarshall(graph)