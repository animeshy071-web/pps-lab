def sum_of_digits_recursive(n):
	
	# Write your code here
	if n == 0:
		return 0
	return (n % 10) + sum_of_digits_recursive(n // 10)



# Write your code here
number = int(input())
result = sum_of_digits_recursive(number)	
print(result)

	