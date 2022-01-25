from random import shuffle

adj=['nice','asshole','not nice','evil']
sub=['manelkar','joydeep','arghyadeep','keshob']

shuffle(adj)

for i in range(len(sub)):
    print(sub[i],'is',adj[i])
