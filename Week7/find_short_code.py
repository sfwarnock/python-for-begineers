import re


ufn = raw_input('Enter the text file name: ')

ufp = 'C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/'

fhand = open(ufp+ufn)

for line in fhand:
    line = line.strip()
    if re.findall(('<short_name>([A-Z]+<))'|('[A-Z]+')), line):
        print line
        #for code in line:
            #if re.findall('[A-Z]+', code):print code,
    
fhand.close()