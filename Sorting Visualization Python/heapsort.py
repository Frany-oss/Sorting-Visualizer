
import time

def heapify(data, n, i):
    largest = i #initialize largest as the root
    l = (2 * i) + 1
    r = (2 * i) + 2
    
    if l < n and data[i] < data[l]:
        largest = l
    
    if r < n and data[largest] < data[r]: 
        largest = r 
    
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data, draw_Data, timeTick):
    n = len(data)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
        draw_Data(data, ['deep pink' for x in range(len(data))])
        time.sleep(timeTick)
    
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        draw_Data(data, ['deep pink' for x in range(len(data))])
        time.sleep(timeTick)
        
    draw_Data(data, ['green' for x in range(len(data))])

    