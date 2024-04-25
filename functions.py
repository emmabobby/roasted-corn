def len_of_string(lexus):
	return len(lexus)

def characters(divine):
	count = 1
	word = ""
	while count < len(divine):
		word += divine[count]
		count += 2
	return word

def minimum(numbers):
	min = numbers[0]
	for num in numbers:
		if num < min:
			min = num
	return min
def maximum(numbers):
	max = numbers[0]
	for num in numbers:
		if num > max:
			max = num
	return max
def sum_square_elements(smart):
	total = 0
	for num in smart:
		sqr = num**2
		total +=sqr
	return total
def square_elements(harry):
	result = []
	for num in harry:
		sqr = num**2
		result.append(sqr)
	return result		
print(square_elements([2,3,4,5,7]))
		
	
