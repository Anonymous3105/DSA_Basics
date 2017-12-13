import sys


# Insertion Sort
def insertion_sort(a):
	for j in range(1, len(a)):
		k = a[j]
		i = j - 1
		while i>=0 and a[i] > k:
			a[i+1] = a[i]
			i -= 1
		a[i+1] = k
	return a

# Bubble Sort
def bubble_sort(a):
	for i in range(0, len(a)-1):
		for j in range(len(a)-1, i, -1):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
	return a


# Merge Sort
def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 

	return result

def merge_sort(a):
	if len(a) < 2:
		return a
	q = int(len(a)/2)
	L = merge_sort(a[:q])
	R = merge_sort(a[q:])
	return merge(L, R)

	

# Quick Sort
def partition(a, p, r):
	x = a[r]
	i = p - 1
	for j in range(p, r):
		if a[j] < x:
			i += 1
			a[i], a[j] = a[j], a[i]
	a[i+1], a[r] = a[r], a[i+1]
	return i+1

def quick_sort(a, p, r):
	if p<r:
		q = partition(a, p, r)
		quick_sort(a, p, q-1)
		quick_sort(a, q+1, r)
		return a

# Shell sort
def shell_sort(a):
	gap = int(len(a)/2)
	while gap > 0:
		for i in range(gap, len(a)):
			k = a[i]
			j = i
			while j >= gap and a[j-gap] > k:	
				a[j] = a[j-gap]
				j -= gap
			a[j] = k
		gap = int(gap/2)
	return a

# Bucket Sort
def bucket_sort(a):
	for i, x in enumerate(A):
		b[int(x*len(b))].append(x)
	result = []
	for buck in b:
		result += insertion_sort(buck)
	return result

# Comb Sort
def getnextgap(gap):
	return 1 if gap < 1 else int(gap*10/13)

def comb_sort(a):
	gap = len(a)
	swap = True
	while gap!=1 or swap==True:
		gap = getnextgap(gap)
		swap = False
		for i in range(len(a)-gap):
			if a[i] > a[i+gap]:
				a[i], a[i+gap] = a[i+gap], a[i]
				swap = True
	return a


# Selection Sort
def selection_sort(a):
	for i in range(len(a)):
		mini = i
		for j in range(i+1, len(a)):
			mini = j if a[mini] > a[j] else mini
		a[i], a[mini] = a[mini], a[i]
	return a


arr = [2,5,9,4,6,3,1]
print("Sorted list after insertion sort: ", insertion_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after bubble sort: ", bubble_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after merge sort: ", merge_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after quick sort: ", quick_sort(arr, 0, len(arr)-1))

arr = [2,5,9,4,6,3,1]
print("Sorted list after shell sort: ", shell_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after Bucket sort: ", bubble_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after Comb sort: ", comb_sort(arr))

arr = [2,5,9,4,6,3,1]
print("Sorted list after Selection sort: ", selection_sort(arr))


