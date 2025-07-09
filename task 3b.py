numbers = [2,5,3,6,7,1]
count = len(numbers)
for i in range(count):
    for j in range(count -1):
        if numbers[j] > numbers[j+1]:
                   numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print('sorted numbers', numbers)
    
