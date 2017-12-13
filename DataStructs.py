import math
import queue

class heap:
	def __init__(self, A = None, key = None):
		if A == None:
			A = list()
		self.A = list(A)
		self.key = key
		self.buildHeap()

	def empty(self):
		return not bool(self.heapsize())

	def heapsize(self):
		return len(self.A)

	def __contains__(self, item):
		return item in self.A

	def _getKeyVal(self, i):
		if self.key == None:
			return self.A[i]
		return getattr(self.A[i], self.key)

	def _setKeyVal(self, i, val):
		if self.key == None:
			self.A[i] = val
		else:
			setattr(self.A[i], self.key, val)		

	def _left(self, i):
		return 2*i + 1
	def _right(self, i):
		return 2*i + 2
	def _parent(self, i):
		return (i-1)//2

	def _minHeapify(self, i):
		left = self._left(i)
		right = self._right(i)
		smallest = i
		if left < self.heapsize() and self._getKeyVal(left) < self._getKeyVal(smallest):
			smallest = left
		if right < self.heapsize() and self._getKeyVal(right) < self._getKeyVal(smallest):
			smallest = right
		if smallest != i:
			self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
			self._minHeapify(smallest)

	def buildHeap(self):
		for i in range(self.heapsize()//2, -1, -1):
			self._minHeapify(i)

	def extractMin(self):
		if self.heapsize() < 1:
			return None
		minimum = self.A[0]
		self.A[0] = self.A[-1]
		self.A.pop()
		self._minHeapify(0)
		return minimum

	def decreaseKey(self, node, newKeyVal):
		i = self.A.index(node)
		if newKeyVal > self._getKeyVal(i):
			return
		self._setKeyVal(i, newKeyVal)
		while i > 0 and self._getKeyVal(self._parent(i)) > self._getKeyVal(i):
			self.A[i], self.A[self._parent(i)] = self.A[self._parent(i)], self.A[i]
			i = self._parent(i)