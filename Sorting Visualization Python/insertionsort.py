
import time

def insertion_sort(data, drawData, timeTick):
    for i in range(0, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1  
        data[j + 1] = key
        drawData(data, ['green' if x == j else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
    


# def get_color_array(dataLen, key, _i):
#     colorArray = []
#     for i in range(dataLen):
#         if i == _i:
#             colorArray.append('blue')
#         if i == key:
#             colorArray.append('deep pink')
#     return colorArray
        
