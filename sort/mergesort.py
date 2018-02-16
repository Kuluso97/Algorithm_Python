import random

def mergesort(a):
	if len(a) <= 1: return a

	mid = len(a) / 2
	left = a[:mid]
	right = a[mid:]
	
	left = mergesort(left)
	right = mergesort(right)

	return merge(left,right)

def merge(left, right):
	res = []
	while left and right:
		if left[0] < right[0]:
			res.append(left[0])
			left = left[1:]
		else:
			res.append(right[0])
			right = right[1:]

	if not left:
		res += right
	elif not right:
		res += left

	return res

def main():
	a = [random.randint(1,100) for _ in range(100)]
	print(mergesort(a))

if __name__ == '__main__':
	main()