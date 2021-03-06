# Make a local change
# Make another local change
# Make a change from home

# iteration pattern
# iteration is doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exclude a calculaton from list members

def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"



#accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

def lowest_2(numbers):
	current_min = numbers[0]
	for i in range(2):
		for n in numbers:
			if n < current_min:
				current_min = n
				del numbers[n]
	return numbers

def avg_score(numbers):
	sum1 = sum(numbers)
	return (sum1 / (len(numbers)))

def avg_score_drop_last_2(numbers):
	low_nums_sum = numbers[0] + numbers[1]
	sum1 = sum(numbers)
	return int((sum1 - low_nums_sum) / (len(numbers) - 2))

def alernating_sum(numbers):
	total = numbers[0] * 2
	for n in range(0, len(numbers)):
		if (n % 2) == 0:
			total -= numbers[n]
		else:
			total += numbers[n]

	return total

def sum_outside(numbers, minimum, maximum):
	total = 0
	for n in numbers:
		if n < minimum or n >= maximum:
			total += n

	return total

def count_close_remainders(numbers, divisor):
	total = 0
	for n in numbers:
		if numbers[n] % 5 <= 1 or numbers[n] % 5 >= 4:
			total += 1

	return total

def double_down(numbers, target):
	result = [numbers[0]]
	for i in range(1, len(numbers)):
		distance = abs(numbers[i] - target)
		if numbers[i] < numbers[i - 1] or distance <= 3:
			result.append(2 * numbers[i])
		else:
			result.append(numbers[i])
	return result