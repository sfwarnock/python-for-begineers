# Assignement 4
## Scott Warnock
## Files, Lists, and Splits

# %cd C:/Users/Scott Warnock/Desktop/UCSD/Python/Python Code/romeo.txt

ufn = raw_input('Enter the text file name: ')

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

uis = raw_input('Enter the string you would like to serch for: ')

def freq_count(user,list1):
    for word in list1:
        if user in word:
            print word, word.count(user)
        elif user not in word:
            print word, word.count(user)

freq_count(uis,script_list)