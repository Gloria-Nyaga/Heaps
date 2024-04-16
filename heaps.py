
import heapq

numbers = [10, 3, 56, 8, 9, 32, 40, 1, 7, 13,25]

heapq.heapify(numbers)
print(numbers)



ages = [2,7,13,45,67,83,90,5]
print (heapq.heappop(ages))
print(ages)


sums = [10, 20, 30, 40, 5, 4, 60, 70]
print (heapq.heappush(sums,55));
print(sums)
