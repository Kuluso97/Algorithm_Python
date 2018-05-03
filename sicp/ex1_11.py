def f_rec(n):
	if n < 3: return n 

	return f_rec(n-1) + 2 * f_rec(n-2) + 3 * f_rec(n-3)

def f_iter(n):
	if n < 3: return n
	queue = [0,1,2]
	for i in range(3,n+1):
		new_item = queue[2] + 2 * queue[1] + 3 * queue[0]
		queue.pop(0)
		queue.append(new_item)

	return queue[-1]

def main():
	for i in range(10):
		print(f_rec(i))
		print(f_iter(i))

if __name__ == '__main__':
	main()