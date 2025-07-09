numbers = [2, 5, 3, 1, 4, 10]
min_value = numbers[0]
max_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
    if number > max_value:
            max_value = number
            
print('min value is ', min_value)
print('max value is ', max_value)

