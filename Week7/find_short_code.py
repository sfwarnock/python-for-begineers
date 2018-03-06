import re


ufn = raw_input('Enter the text file name: ')

ufp = 'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/'

fhand = open(ufp+ufn)

for line in fhand:
    line = line.strip()
    x = re.findall('<short_name>([A-Z]+)<', line)
    for code in x:
        if re.findall('[A-Z]', code):print code
    
fhand.close()