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
            script_list.append(word.lower())
    script_list.sort()

print script_list
             
fhand.close()

uis = raw_input('Input word: ')

def freq_count(user,list1):
    count = 0
    for word in list1:
        if (user) == word:
            count = count + 1
            print (user) + ' is found ' + str(count) + ' in ' + (word)
        elif (user) != word:
            print (user) + ' is found 0 times in ' + (word)

freq_count(uis,script_list)