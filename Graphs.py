import math
from DataStructs import heap

class Vertex:
	def __init__(self, id):
		self.id = id
		self.adjacent = {}
		self.distance = math.inf
		self.pred = None
		self.color = 'white'
		self.discoverdTime = math.inf
		self.finishTime = math.inf

	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

	def __lt__(self, other):
		return other and self.distance < other.distance

	def addNeighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight

	def getConnections(self):
		return self.adjacent.keys()  

	def setPred(self, p):
		self.pred = p

	def getId(self):
		return self.id

	def getWeight(self, neighbor):
		return self.adjacent[neighbor]

	def getDistance(self):
		return self.distance


class Graph:
	def __init__(self):
		self.vertDict = {}
		self.numVertices = 0
		self.time = 0

	def __iter__(self):
		return iter(self.vertDict.values())

	def addVertex(self, newVertId):
		if newVertId not in self.vertDict:
			self.numVertices += 1
			newVertex = Vertex(newVertId)
			self.vertDict[newVertId] = newVertex
			return newVertex

	def getVertex(self, vertId):
		if vertId in self.vertDict:
			return self.vertDict[vertId]
		else:
			return None

	def addEdge(self, vertId1, vertId2, weight = 0, directed = True):
		if vertId1 not in self.vertDict:
			self.addVertex(vertId1)
		if vertId2 not in self.vertDict:
			self.addVertex(vertId2)

		self.vertDict[vertId1].addNeighbor(self.vertDict[vertId2], weight)
		if not directed:
			self.vertDict[vertId2].addNeighbor(self.vertDict[vertId1], weight)

	def getVertices(self):
		return self.vertDict.keys()

	def BreadthFirstSearch(self, source = None):
		if type(source) == str:
			source = self.getVertex(source)
		if(source == None or type(source) != Vertex):
			return
		for u in self.vertDict.values():
			u.color = 'white'
			u.distance = math.inf
			u.pred = None

		source.color = 'grey'
		source.distance = 0

		Q = queue.Queue()
		Q.put(source)
		while not Q.empty():
			u = Q.get()
			# print(u.id)
			for v in u.getConnections():
				if v.color == 'white':
					v.color = 'grey'
					v.distance = u.distance + 1
					v.pred = u
					Q.put(v)
			u.color = 'black'

	def PrintPath(self, s, v):
		if v.id == s.id:
			print(s.id)
		elif v.pred == None:
			print("No path from " + str(s.id) + " to " + str(v.id) + " exists through predecessor subgraph")
		else: 
			self.PrintPath(s, v.pred)
			print(v.id)

	def _dfsVisit(self, u):
		self.time += 1
		u.discoverdTime = self.time
		u.color = 'grey'
		# print(u.id)
		for v in sorted(u.getConnections(), key = lambda x: x.finishTime, reverse = True):
			if v.color == 'white':
				v.pred = u
				self._dfsVisit(v)
		u.color = 'black'
		self.time += 1
		u.finishTime = self.time

	def DepthFirstSearch(self):
		for u in self.vertDict.values():
			u.color = 'white'
			u.pred = None
		self.time = 0
		for u in sorted(self.vertDict.values(), key = lambda x: x.finishTime, reverse = True):
			if u.color == 'white':
				# print(u.id)
				self._dfsVisit(u)

	def TopologicalSort(self):
		sortkey = lambda x: x.finishTime
		return [x.id for x in sorted(self.vertDict.values(), key = sortkey, reverse = True)]	

	def MST_Prim(self, source = None, dijkstra = False):
		"""
		if dijktra = True then MST_Prim will perform dijktra's shortest path algorithm instead
		"""
		if type(source) == str:
			source = self.getVertex(source)
		if(source == None or type(source) != Vertex):
			return

		for u in self.vertDict.values():
			u.distance = math.inf
			u.pred = None
		source.distance = 0

		Q = heap(self.vertDict.values(), 'distance')
		while not Q.empty():
			u = Q.extractMin()
			for v in u.getConnections():
				if v in Q and u.getWeight(v) + dijkstra * u.distance < v.distance:
					v.pred = u
					Q.decreaseKey(v, u.getWeight(v) + dijkstra * u.distance)
					# v.distance = u.getWeight(v) + dijkstra * u.distance
		if dijkstra:
			treeWeight = sorted([(i.id, i.distance) for i in self.vertDict.values()])
		else:
			treeWeight = sum([i.distance for i in self.vertDict.values()])
		treeEdges = sorted([(v.pred.id, v.id) for v in self.vertDict.values() if v.pred != None])
		return treeWeight, treeEdges





g = Graph()
g.addEdge('0', '1', weight = 4, directed = False)
g.addEdge('0', '7', weight = 8, directed = False)
g.addEdge('1', '7', weight = 11, directed = False)
g.addEdge('1', '2', weight = 8, directed = False)
g.addEdge('2', '3', weight = 7, directed = False)
g.addEdge('2', '5', weight = 4, directed = False)
g.addEdge('2', '8', weight = 2, directed = False)
g.addEdge('3', '4', weight = 9, directed = False)
g.addEdge('3', '5', weight = 14, directed = False)
g.addEdge('4', '5', weight = 10, directed = False)
g.addEdge('5', '6', weight = 2, directed = False)
g.addEdge('6', '7', weight = 1, directed = False)
g.addEdge('6', '8', weight = 6, directed = False)
g.addEdge('7', '8', weight = 7, directed = False)

# print(g.MST_Prim('0'))
treeWeight, treeEdges = g.MST_Prim('0')
print('Weight of MST:', treeWeight)
print('Edges in MST:', treeEdges)
print()

h = Graph()
h.addEdge('v1', 'v2', weight = 2, directed = True)
h.addEdge('v1', 'v4', weight = 1, directed = True)
h.addEdge('v2', 'v4', weight = 3, directed = True)
h.addEdge('v2', 'v5', weight = 10, directed = True)
h.addEdge('v3', 'v1', weight = 4, directed = True)
h.addEdge('v3', 'v6', weight = 5, directed = True)
h.addEdge('v4', 'v3', weight = 2, directed = True)
h.addEdge('v4', 'v5', weight = 2, directed = True)
h.addEdge('v4', 'v6', weight = 8, directed = True)
h.addEdge('v4', 'v7', weight = 4, directed = True)
h.addEdge('v5', 'v7', weight = 6, directed = True)
h.addEdge('v7', 'v6', weight = 1, directed = True)


treeWeight, treeEdges = h.MST_Prim('v1', dijkstra = True)
print('Shortest distances of vertices from source:', treeWeight)
print('Edges in dijkstra tree:', treeEdges)