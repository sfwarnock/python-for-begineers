# Assignment #3 Process Numbers
# Looping, Searching, and Slicing.

user_num = []

def user_input():
    num = raw_input('Type number: ')
    return num

while True:
    num = user_input()
    if num == 'done':
        break
    print num
    user_num.append(num)
print 'Done'

print (user_num)

int_list = [int(x) for x in user_num]

print 'You entered ' + str(len(int_list)) + ' numbers.'
print 'The smallest number you entered is: ' + str(min(int_list))
print 'The largest number you entered is: ' + str(max(int_list))
print 'The sum of the numbers you entered is: ' + str(sum(int_list))

y = sum(int_list)/len(int_list)

print 'The mean of the numbers you entered is: ' + str(y)
