#Time: O(n) , Space: O(1)

def isValidSubsequence(array, sequence):
	index = 0
	sub_length = len(sequence)
	for i in array:
		if i == sequence[index]:
			index = index+1
		if sub_length == index:
			return True
	return False	

a = [1, 4, -1, 8, 3, 7, 0]
b = [4, 3, 0]
print(isValidSubsequence(a, b))