## SICP ex 1.12
def pascal(result, level=5):
	if level == 0:
		return []

	if level == 1:
		result.append([1])
		return result

	new_row = [1]
	result = pascal(result, level=level-1)
	last_row = result[-1]
	for i in range(len(last_row)-1):
		new_row.append(last_row[i] + last_row[i+1])

	new_row += [1]
	result.append(new_row)
	return result

def main():
	result = []
	pascal(result, level=5)
	print(result)

if __name__ == '__main__':
	main()