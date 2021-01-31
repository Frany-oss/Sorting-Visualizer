
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort  import quick_sort
from mergesort import  merge_sort
from insertionsort import insertion_sort
from heapsort import heap_sort

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1100, 800)
root.config(bg = 'black')

#variables
selected_alg = StringVar()  # se algorithm
data = []

def draw_Data(data, colorArray): # draw the rectangles to sort
    canvas.delete("all")
    c_height = 580
    c_width  = 800
    x_width  = c_width / (len(data) + 1)
    offset   = 10 # space between the margin and the rectangle 
    spacing  = 5 # space between the rectangles
    normalize_data = [i / max(data) for i in data] # normalize the data of the array, making it the bigger element, the max height
    
    for i, height in enumerate(normalize_data):
        #top left of rectangle
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        
        #bottom right of rectangle
        x1 = (i + 1) * x_width + offset 
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        canvas.create_text(x0 + 3, y0, anchor = SW, text = str(data[i]))
        
    root.update_idletasks() #update afer evry single event
        
    

def Generate():
    global data
    minVal = int(minEntry.get() )
    maxVal = int(maxEntry.get() )
    size   = int(sizeEntry.get())
    
    data = []
    # generate random values to the empty data list
    for i in range(size):
        data.append(random.randrange(minVal, maxVal + 1 ))
        
    draw_Data(data, ['red' for x in range(len(data))])


def start_algo():
    global data
    if not data: return 
    
    if algoMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_Data, speedScale.get())
        
    elif algoMenu.get() == 'Bubble sort':
        bubble_sort(data, draw_Data, speedScale.get())
    
    elif algoMenu.get() == 'Merge Sort':
        merge_sort(data, draw_Data, speedScale.get())
    
    elif algoMenu.get() == 'Insertion Sort':
        insertion_sort(data, draw_Data, speedScale.get())
    
    elif algoMenu.get() == 'Heap Sort':
        heap_sort(data, draw_Data, speedScale.get())
        
    draw_Data(data, ['green' for x in range(len(data))])
    

# Frame / base layout
UI_frame = Frame(root, width = 800, height = 400, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

# Canvas (where the sorting is going to happend)
canvas = Canvas(root, width = 800, height = 580, bg = 'white')
canvas.grid(row = 1, column = 0,  padx = 10, pady = 5)


# -------- User Interface Area ---------
#Row[0]
Label(UI_frame, text = "Algorithm: ", bg = 'grey').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algoMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values = ['Bubble sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort', 'Heap Sort'])
algoMenu.grid(row = 0, column = 0, padx = 5, pady = 5)
algoMenu.current(0)

#speed scale
speedScale = Scale(UI_frame, from_ = 0.0, to = 4.0, length = 200, digits = 3, resolution = 0.1, orient = HORIZONTAL, label = "Select Speed")
speedScale.grid(row = 0, column = 1, padx = 5, pady = 5)

# start button
Button(UI_frame, text = "Start", command = start_algo, bg = 'red').grid(row = 0, column = 4, padx = 10, pady = 10)

#Row[1]
# size scale
sizeEntry = Scale(UI_frame, from_ = 3, to = 50, resolution = 1, orient = HORIZONTAL, label = "Data Size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)

# min value scale
minEntry = Scale(UI_frame, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, label = "Min Value") 
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

# max value scale
maxEntry = Scale(UI_frame, from_ = 10, to = 100, resolution = 1, orient = HORIZONTAL, label = "Max Value")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

# Generate array
Button(UI_frame, text="Generate", command = Generate, bg = 'white').grid(row = 1, column = 4, padx = 5, pady = 5)


root.mainloop()

