# Assignement 4
## Scott Warnock
## Files, Lists, and Splits

# %cd C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/romeo.txt

fhand = open(r'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/romeo.txt')

line_list = []

script_list = []

for line in fhand:
    line_list = line.split()
    line_list.sort()
    print line_list
    
    combine = line_list + script_list
    
    print combine
    
fhand.close()