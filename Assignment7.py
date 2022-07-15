#Question 1

from tkinter import *
def get_gst():
    a=int(netprice_t.get())
    b=int(originalcost_t.get())
    display.insert(0,f'GST rate ={((a-b)*100)/b}')

k=Tk()
k.title("GST rate calculator")
k.geometry('400x300')
k.config(bg='#0f4b6e')

netprice_t=Entry(k)
originalcost_t=Entry(k)

netprice_lbl=Label(k,text='Net Price',bg='#0f4b6e',fg='white')
originalcost_lbl=Label(k,text='Original Cost',bg='#0f4b6e',fg='white')

netprice_lbl.pack()
netprice_t.pack()
originalcost_lbl.pack()
originalcost_t.pack()

bt=Button(k,text="Get GST Rate",relief='solid',command=get_gst)
bt.pack(pady=10)

display=Entry(k,width=38,font=('Arial',14))
display.pack(pady=5)
k.mainloop()



#Question 2

from tkinter import *
import calendar
def disp_cal():
    n=Tk()
    n.title('Calender')
    n.geometry('700x600')
    
    year=int(enter_year.get())
    cal=calendar.calendar(year)
    cal_disp=Label(n,text=cal,font = "Consolas 10 bold")
    cal_disp.grid(row = 5, column = 1, padx = 80)
    n.mainloop() 
k=Tk()
k.title("Year specification")
k.geometry('400x300')
k.config(bg='#0f4b6e')

year_t=Label(k,text='Enter year',bg='#0f4b6e',fg='white')
enter_year=Entry(k)

year_t.pack()
enter_year.pack()

bt=Button(k,text='Display Calender',relief='solid',command=disp_cal)
bt.pack()
k.mainloop()



#Question 3


from tkinter import *

win = Tk() 
win.geometry("312x324")  
win.resizable(0, 0)  
win.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

 
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""
 

 
input_text = StringVar()
 

 
input_frame=Frame(win, width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) 

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()
clear=Button(btns_frame, text="C", fg="black", width=32,height=3,bd=0,bg="#eee",cursor="hand2",
             command=lambda:bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1) 
divide=Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",
              command=lambda:btn_click("/")).grid(row=0, column=3,padx=1, pady=1)
 

 
seven=Button(btns_frame,text="7", fg="black", width=10, height=3, bd=0, bg="#fff",cursor="hand2",
             command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg ="#fff",cursor="hand2",
             command=lambda:btn_click(8)).grid(row=1,column=1,padx =1,pady=1)
nine=Button(btns_frame,text = "9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",
            command=lambda:btn_click(9)).grid(row =1, column=2, padx=1, pady=1)
multiply=Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
                command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

 
four=Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",
            command=lambda:btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five=Button(btns_frame,text ="5",fg="black", width=10,height=3,bd=0, bg="#fff",cursor="hand2",
            command=lambda:btn_click(5)).grid(row=2, column=1, padx=1, pady=1) 
six=Button(btns_frame,text="6",fg="black",width=10,height=3, bd=0,bg="#fff",cursor="hand2",
           command=lambda:btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus=Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",
             command=lambda:btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
 
one=Button(btns_frame,text ="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",
           command=lambda:btn_click(1)).grid(row=3,column=0,padx=1, pady=1)
two=Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",
           command=lambda:btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three=Button(btns_frame,text ="3",fg ="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",
             command=lambda:btn_click(3)).grid(row=3,column=2, padx=1, pady=1)
plus=Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",
            command=lambda:btn_click("+")).grid(row=3,column=3,padx=1,pady=1)

zero=Button(btns_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff", cursor = "hand2",
            command = lambda:btn_click(0)).grid(row=4, column=0,columnspan=2,padx=1,pady=1)
point=Button(btns_frame,text=".",fg="black",width=10,height=3, bd = 0, bg = "#eee", cursor = "hand2",
             command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals=Button(btns_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",
              command=lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()



#Question 4

n=int(input("Enter number of marks to be inputed:"))
list=[]
for i in range(0,n):
    s=int(input("Enter marks:"))
    list.append(s)
    
def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  
        quicksort(pi+1, r, nums)  
    return nums

print(quicksort(0,len(list)-1,list))



#Question 5

n=int(input("Enter number of inputs:"))
l=[]
for i in range(0,n):
    s=int(input("Enter number:"))
    l.append(s)
l.sort()
print(l)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
 
x=int(input("Enter value to be searched:"))
result = binary_search(l, x)
print("Number of occurences:",l.count(x))
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



#Question 6


def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
          
    return array
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
n=int(input("Enter number of inputs:"))
l=[]
for i in range(0,n):
    s=int(input("Enter number:"))
    l.append(s)
l=set(l)
l=list(l)
l.sort()
print(l)

