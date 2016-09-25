
def stepFloor(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4
	return stepFloor(n - 1) + stepFloor(n - 2) + stepFloor(n - 3)

if __name__ == '__main__':
	n = stepFloor(20)
	print(n)
