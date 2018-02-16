def binarysearch(A, n, lo, hi):
	if lo > hi: return -1

	mid = (lo + hi) // 2
	if A[mid] == n:
		return mid
	elif A[mid] > n:
		return binarysearch(A, n, lo, mid-1)
	else:
		return binarysearch(A, n, mid+1, hi)


def main():
	a = [i for i in range(100)]
	index = binarysearch(a, 60, 0, 99)
	print(a[index] == 60)

if __name__ == '__main__':
	main()