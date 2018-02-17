ufn = raw_input('Enter the text file name: ')

ufp = 'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/'

fhand = open(ufp+ufn)

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print counts