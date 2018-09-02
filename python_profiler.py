from collections import defaultdict
import time

start_time = time.time()

dummy_list = []

print('start')
limit = 10000000

while limit:
    dummy_list.append('Dummy Value')
    limit -= 1
    stop = time.time()

print(time.time() - start_time)

start = time.time()

size_list = [None] * 10000000

index = 1
while index:
    size_list[index] = dummy_list
    index += 1
    if index == 10000000:
        break

print(time.time() - start)
