from generator import Generator
from visibility import VisibilityGraph
import matplotlib.patches as patches
import matplotlib.pyplot as plt

if __name__ == "__main__":
	print "Preferable goal position ([95-100, 95-100])"
	gX = int(input("Enter X coordinate of the goal: "))
	gY = int(input("Enter Y coordinate of the goal: "))

	print "Preferable goal position ([0-5, 0-5])"
	X = int(input("Enter X coordinate of the initial position: "))
	Y = int(input("Enter Y coordinate of the initial position: "))
	n = int(input("Enter the number of obstacles: "))

	start = [X, Y]
	end = [gX, gY]

	generator = Generator(n)
	obstacleList = generator.generateRect()
	edges = generator.getEdges()
	vertices = generator.getVertices()
	vertices.append([X, Y])
	vertices.append([gX, gY])

	vis = VisibilityGraph(obstacleList, edges, vertices)
	graph = vis.CreateGraph()

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	for (ox, oy, sx, sy) in obstacleList:
		ax1.add_patch(patches.Rectangle((ox - sx/2.0, oy - sy/2.0), sx, sy, color='black'))


	for edge in graph:
		x = [edge[0][0], edge[1][0]]
		y = [edge[0][1], edge[1][1]]
		plt.plot(x, y)

	plt.show()