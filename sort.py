number = int(input('enter a number? '))
number1 = (input('enter numbers separated by space '))
numbers = (number1.split())
numbers.reverse()
numbers = numbers[:number]
print('list of numbers', numbers)
