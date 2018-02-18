import random

def insertionsort(A):
	for i in range(1, len(A)):
		while i > 0 and A[i] < A[i-1]:
			A[i], A[i-1] = A[i-1], A[i]
			i -= 1

def main():
	a = [random.randint(1,100) for _ in range(100)]
	insertionsort(a)
	print(a)

if __name__ == '__main__':
	main()