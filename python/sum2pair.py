#!/usr/bin/env python
# sum2pair
# Popular interview programming question. Write a function which given a list, say
# [2, 8, 5, 6, 3, 4], will print out all pairs that add up to a particular sum, say 8.

def sum2pair(lst, sum):
    print "List =", lst, " ", "sum =", sum
    seen = set()
    print "%03s  %-30s  %06s " % ("E", "SEEN", "TARGET")
    for e in lst:
        target = sum - e
        print "%03s  %-30s  %06s " % (e, list(seen), target),
        if target in seen:
            print "(%s, %s)" % (e, target)
        else:
            seen.add(e)
            print

sum2pair([2, 8, 5, 6, 3, 4], 8)
