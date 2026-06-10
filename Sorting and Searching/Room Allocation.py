import sys
from heapq import heappop, heappush

data = sys.stdin.buffer.read().split()
it = iter(data)
q = int(next(it))
intervals = [None] * q
for idx in range(q):
    a = int(next(it))
    b = int(next(it))
    intervals[idx] = (a, b, idx)
intervals.sort()

ans = [0] * q
heap = []
next_room = 1
for a, b, idx in intervals:
    if heap and heap[0][0] < a:
        _, room = heappop(heap)
    else:
        room = next_room
        next_room += 1
    ans[idx] = room
    heappush(heap, (b, room))

sys.stdout.write(str(next_room - 1) + "\n")
sys.stdout.write(" ".join(map(str, ans)))
