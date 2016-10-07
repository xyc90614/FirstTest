def BubbleSort(a):
	length = len(a)
	for i in range(length):
		for j in range(0 , length - i - 1):
			if a[j] > a[j + 1]:
				tmp = a[j]
				a[j] = a[j + 1]
				a[j + 1] = tmp
	return a

def insertSort(a):
	length = len(a)
	sorted_a = []
	sorted_a.append(a[0])
	for i in range(1,length):
		new_in = a[i]
		sub_len = len(sorted_a)
		for j in range(sub_len):
			if(new_in < sorted_a[j]):
				sorted_a.insert(j , new_in)
				break

	return sorted_a

def selectSort(a):
	length = len(a)
	sorted_a = []
	
	for i in range(length):
		min = a[i]
		min_index = i
		for j in range(i+1 , length):
			if a[j] < min:
				min_index = j
				min = a[j]	
		
		if i != min_index:
			a[min_index] = a[i]
			a[i] = min
		
	return a

def quickSortInner(a , left , right):
	if left < right:
		i = left
		j = right
		X = a[left]
		while i < j:
			while i < j and  a[j] > X:
				j = j - 1

			if i < j:
				a[i] = a[j]
				i = i + 1
			while i < j and a[i] < X:
				i = i +1
			if i < j:
				a[j] = a[i]
				j = j - 1

		a[i] = X
		quickSortInner(a , left , i-1)
		quickSortInner(a , i + 1, right)
			
def quickSort(a):
	length = len(a)
	i = quickSortInner(a , 0 , length - 1)
	return a
