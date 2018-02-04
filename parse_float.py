# Assignment #3 Parse Float
# Looping, Searching, and Slicing.
## Scott Warnock

avg_str = 'Average value read: 0.72903'

atcol = avg_str.find(':')

endpos = len(avg_str)

number = avg_str[atcol+1:endpos+1]

print float(number)