import random
import math

class Generator():
	def __init__(self, n):
		self.n = n
		self.vertices = []
		self.obstacles = []
		self.edges = []

	def generateRect(self):
		maxSize = ((100 * 100) / (self.n))/2
		for i in range(self.n):
			x, y = random.randint(7, 93), random.randint(7, 93)
			sizeX, sizeY = random.randint(2, int(math.sqrt(maxSize))), random.randint(2, int(math.sqrt(maxSize)))
			self.obstacles.append([x, y, sizeX, sizeY])
		# print self.obstacles
		return self.obstacles

	def getVertices(self):
		for (ox, oy, a, b) in self.obstacles:
			self.vertices.append([ox - a/2.0, oy - b/2.0])
			self.vertices.append([ox - a/2.0, oy + b/2.0])
			self.vertices.append([ox + a/2.0, oy - b/2.0])
			self.vertices.append([ox + a/2.0, oy + b/2.0])
		return self.vertices

	def getEdges(self):
		for (ox, oy, a, b) in self.obstacles:
			self.edges.append([ox - a/2.0, oy - b/2.0, ox - a/2.0, oy + b/2.0])
			self.edges.append([ox - a/2.0, oy - b/2.0, ox + a/2.0, oy - b/2.0])
			self.edges.append([ox + a/2.0, oy + b/2.0, ox + a/2.0, oy - b/2.0])
			self.edges.append([ox + a/2.0, oy + b/2.0, ox - a/2.0, oy + b/2.0])
		return self.edges