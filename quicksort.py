import random


## In-place quicksort
def quicksort(a, lo, hi):
	if lo < hi:
		pi = partition(a, lo, hi)

		quicksort(a, lo, pi-1)
		quicksort(a, pi+1, hi)
	
def partition(a, lo, hi):
	pivot = a[hi]
	i = lo

	for j in range(lo, hi):
		if a[j] < pivot:
			a[i], a[j] = a[j], a[i]
			i += 1

	a[i], a[hi] = a[hi], a[i]
	return i

## Quicksort with O(n) space
def quicksortTwo(A):
	if len(A) <= 1:
		return A
	else:
		pivot = A[0]
		lesser = [i for i in A[1:] if i <= pivot]
		greater = [i for i in A[1:] if i > pivot]

	return quicksortTwo(lesser) + [pivot] + quicksortTwo(greater)


def main():
	a = [random.randint(1,100) for _ in range(100)]
	print(a)
	quicksort(a, 0, len(a)-1)
	print(a)
	a = [random.randint(1,100) for _ in range(100)]

	print(a)
	a = quicksortTwo(a)
	print(a)

if __name__ == '__main__':
	main()
