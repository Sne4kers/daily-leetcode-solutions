from functools import cmp_to_key
from queue import PriorityQueue

class Solution:
    def compare(x, y):
        return x[0] - y[0]
    
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        sorted_times = sorted(times, key=cmp_to_key(Solution.compare))
        pq_exit = PriorityQueue()
        pq_seat = PriorityQueue()
        print(sorted_times)
        for i in range(len(sorted_times)):
            current = sorted_times[i]
            while not pq_exit.empty():
                if pq_exit.queue[0][0] <= current[0]:
                    pq_seat.put(pq_exit.get()[1])
                else:
                    break

            if targetFriend == current[2]:
                break
                
            if pq_seat.empty():
                pq_exit.put((current[1], pq_exit.qsize()))
            else:
                pq_exit.put((current[1], pq_seat.get()))

        if pq_seat.empty():
            return pq_exit.qsize()
        else:
            return pq_seat.get()
