from tkinter import *
import tkinter as tk
import tkinter.font as font
root = tk.Tk()
root.title("Simple Calculator")

e = Entry(root, width=45, borderwidth=4, bg="pink",fg="black",)
e.grid(row=0 , column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current =e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    fisrt_number = e.get()
    global f_num
    global math
    math ="addition"
    
    f_num = int(fisrt_number)
    e.delete(0,END)



def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math =="addition":
             e.insert(0,f_num + int(second_number))
    if math =="subtraction":
             e.insert(0,f_num - int(second_number))
    if math =="multiplication":
             e.insert(0,f_num * int(second_number))
    if math =="division":
             e.insert(0,f_num / int(second_number))
    if math =="square":
             e.insert(0,square)
            
   

def button_subtract():
    fisrt_number = e.get()
    global f_num
    global math
    math ="subtraction"
    
    f_num = int(fisrt_number)
    e.delete(0,END)

def button_multiply():
    fisrt_number = e.get()
    global f_num
    global math
    math ="multiplication"
    
    f_num = int(fisrt_number)
    e.delete(0,END)

def button_division():
    fisrt_number = e.get()
    global f_num
    global math
    math ="division"
    
    f_num = int(fisrt_number)
    e.delete(0,END)

def button_square():
    first_number = e.get()
    global f_num
    global math
    math ="square"
    
    f_num = int(fisrt_number)
    global sqaure
    square = f_num*f_num
    e.delete(0,END)
    

def button_sqroot():
    return


def button_fact():
    fisrt_number = e.get()
    global f_num
    global math
    math ="addition"
    
    f_num = int(fisrt_number)
    e.delete(0,END)

my = font.Font(family="imapact")
    
button_1 = Button(root,text="1  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(1))
button_2 = Button(root,text="2  ",padx=40,pady=20,bg="red",fg="yellow",command=lambda: button_click(2))
button_3 = Button(root,text="3  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(3))
button_4 = Button(root,text="4  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(4))
button_5 = Button(root,text="5  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(5))
button_6 = Button(root,text="6  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(6))
button_7 = Button(root,text="7  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(7))
button_8 = Button(root,text="8  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(8))
button_9 = Button(root,text="9  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(9))
button_0 = Button(root,text="0  ",padx=40,pady=20,bg="red",fg="yellow", command=lambda: button_click(0))
button_add =Button(root,text="+  ",padx=40,pady=20,bg="black",fg="yellow", command=button_add)
button_subtract =Button(root,text="-  ",padx=40,pady=20,bg="black",fg="yellow", command=button_subtract)
button_mult =Button(root,text="*  ",padx=40,pady=20,bg="black",fg="yellow", command=button_multiply)
button_div =Button(root,text="/  ",padx=40,pady=20,bg="black",fg="yellow", command=button_division)
button_equal =Button(root,text="=  ",padx=40,pady=20,bg="black",fg="yellow", command=button_equal)
button_clear =Button(root,text="clr",padx=40,pady=20,bg="yellow",fg="black", command=button_clear)

button_1.grid(row=5,column=0,sticky=tk.W+ tk.E)
button_2.grid(row=5,column=1,sticky=tk.W+ tk.E)
button_3.grid(row=5,column=2,sticky=tk.W+ tk.E)
button_4.grid(row=4,column=0,sticky=tk.W+ tk.E)
button_5.grid(row=4,column=1,sticky=tk.W+ tk.E)
button_6.grid(row=4,column=2,sticky=tk.W+ tk.E)
button_7.grid(row=3,column=0,sticky=tk.W+ tk.E)
button_8.grid(row=3,column=1,sticky=tk.W+ tk.E)
button_9.grid(row=3,column=2,sticky=tk.W+ tk.E)
button_0.grid(row=6,column=0,sticky=tk.W+ tk.E)


button_mult.grid(row=5,column=3,sticky=tk.W+ tk.E)
button_subtract.grid(row=4,column=3,sticky=tk.W+ tk.E)
button_clear.grid(row=3,column=3,sticky=tk.W+ tk.E)
button_div.grid(row=6,column=2,sticky=tk.W+ tk.E)
button_equal.grid(row=6,column=3,sticky=tk.W+ tk.E)
button_add.grid(row=6,column=1,sticky=tk.W+ tk.E)

button_1['font'] = my
button_2['font'] = my
button_3['font'] = my
button_4['font'] = my
button_5['font'] = my
button_6['font'] = my
button_7['font'] = my
button_8['font'] = my
button_9['font'] = my
button_0['font'] = my
button_add['font'] = my
button_subtract['font'] = my
button_mult['font'] = my
button_div['font'] = my

button_equal['font'] = my
button_clear['font'] = my







root.mainloop()
