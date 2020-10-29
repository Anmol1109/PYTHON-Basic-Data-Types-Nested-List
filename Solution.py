a = [[raw_input(),float(raw_input())]for i in xrange(int(raw_input()))]
b = sorted(set([x[1] for x in a]))
for i in sorted(x[0] for x in a if x[1] == b[1]):
    print i