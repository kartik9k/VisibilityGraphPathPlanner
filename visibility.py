import numpy as np

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	return (C.y - A.y)*(B.x - A.x) > (B.y - A.y)*(C.x - A.x)

def intersect(A,B,C,D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

class VisibilityGraph():
	def __init__(self, obstacleList, edges, vertices):
		self.obstacleList = obstacleList
		self.edges = edges
		self.vertices = vertices
		self.visibleVertex = []

	def CreateGraph(self):
		for i in range(len(self.vertices)):
			for j in range(len(self.vertices)):
				if i != j:
					if self.isVisible(i, j):
						self.visibleVertex.append([self.vertices[i], self.vertices[j]])

		return self.visibleVertex

	def isVisible(self, i, j):
		a = Point(self.vertices[i][0], self.vertices[i][1])
		b = Point(self.vertices[j][0], self.vertices[j][1])

		for (x1, y1, x2, y2) in self.obstacleList:
			c = Point(x1, y1)
			d = Point(x2, y2)

			if intersect(a, b, c, d):
				return False
			else:
				continue
		return True