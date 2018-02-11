list1 = ['and', 'and', 'but', 'for', 'too']

sub = raw_input('Test: ')

count = 0

for letter in list1:
    if letter == sub:
        count = count + 1

print sub, count