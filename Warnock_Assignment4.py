# Assignement 4
## Scott Warnock
## Files, Lists, and Splits

# %cd C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/romeo.txt

fhand = open(r'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/romeo.txt')

line_list = []

script_list = []

for line in fhand:
    line_list = line.split()
    for word in line_list:
        if word not in script_list:
            script_list.append(word)

script_list.sort()

print script_list
             
fhand.close()