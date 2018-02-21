list1 = ['and', 'and', 'but', 'for', 'too']

sub = raw_input('Test: ')

def freq_count(uis,nlist):
    for word in nlist:
        if sub in word:
            print word, word.count(sub)
        elif sub not in word:
            print word, word.count(sub)

freq_count(sub,list1)