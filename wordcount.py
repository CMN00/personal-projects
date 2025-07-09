lang1 = input('enter a sentence? ')
lang = lang1.split()
count = {}
for word in lang:
    if word in count:
        count [word] += 1
    else:
        count [word] = 1
       
print('word count',count)