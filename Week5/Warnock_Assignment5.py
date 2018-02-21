# Assignement 5
## Scott Warnock
## Mesage frequency count

ufn = raw_input('Enter the text file name: ')

ufp = 'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/'

fhand = open(ufp+ufn)

e = dict()

for line in fhand:
    if not line.startswith('From:'): continue
    word = line.split() 
    email = word[1]
    for word in email:
        if email not in e:
            e[email] = 1
        else:
            e[email] += 1
    
first = list()  

for key, val in e.items():
    first.append((val,key))

first.sort(reverse=True)

print first[0]
    
fhand.close()