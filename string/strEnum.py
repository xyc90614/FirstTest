
def strEnum(s , n):
	result = []
	length = len(s)
	result = [s[0]]
	for j in range(1,length):
		each_ch = s[j]
		result1 = []
		list_len = len(result)
		for p in range(list_len):
			each_item = result[p]
			len_sub = len(each_item)
			for i in range(len_sub + 1):
				##str_item = str(each_item)
				a = each_item[0:i] + each_ch + each_item[i : ]
				result1.append(a)
		result = result1
	return result

if __name__ == '__main__':
	ret = strEnum("abc",1)
	try:
		fl = open("data.txt" , "w")
		print(ret , file = fl)
		fl.close()
	except IOError:
		print('File Error')	
