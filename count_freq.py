list1 = ['and', 'and', 'but', 'for', 'too']

sub = raw_input('Test: ')

def freq_count(user_input,list):
    for user_input in list:
        print list, ":",list.count(sub);

freq_count(sub,list1)