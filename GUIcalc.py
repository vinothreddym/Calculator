from tkinter import *
def sbutton(number):
    global operator
    operator=operator+str(number)
    txtdisplay.set(operator)
    
def clearb():
    global operator
    txtdisplay.set("")
    operator=""

def equalb():
    txtdisplay.set(str(eval(txtdisplay.get())))
    operator=""
    
calc=Tk()
calc.title("Calculator")
operator=''
txtdisplay=StringVar()
displaybutton=Entry(calc,width=28,textvariable=txtdisplay, font="bold",justify='right',bg="powder blue")
displaybutton.grid(row=1,columnspan=6)
sevenbutton=Button(calc,text='7',fg="black",highlightcolor="blue",command=lambda:sbutton(7),width=10)
sevenbutton.grid(row=2,column=1)
eightbutton=Button(calc,text='8',fg="black",highlightcolor="blue",command=lambda:sbutton(8),width=10)
eightbutton.grid(row=2,column=2)
ninebutton=Button(calc,text='9',fg="black",highlightcolor="blue",command=lambda:sbutton(9),width=10)
ninebutton.grid(row=2,column=3)
clearbutton=Button(calc,text='C',fg="Blue",highlightcolor="blue",command=clearb,width=10,bd=3)
clearbutton.grid(row=2,column=4)
fourbutton=Button(calc,text='4',fg="black",highlightcolor="blue",command=lambda:sbutton(4),width=10)
fourbutton.grid(row=3,column=1)
fivebutton=Button(calc,text='5',fg="black",highlightcolor="blue",command=lambda:sbutton(5),width=10)
fivebutton.grid(row=3,column=2)
sixbutton=Button(calc,text='6',fg="black",highlightcolor="blue",command=lambda:sbutton(6),width=10)
sixbutton.grid(row=3,column=3)
divbutton=Button(calc,text='/',fg="green",highlightcolor="blue",command=lambda:sbutton("/"),width=10)
divbutton.grid(row=3,column=4)
onebutton=Button(calc,text='1',fg="black",highlightcolor="blue",command=lambda:sbutton(1),width=10)
onebutton.grid(row=4,column=1)
twobutton=Button(calc,text='2',fg="black",highlightcolor="blue",command=lambda:sbutton(2),width=10)
twobutton.grid(row=4,column=2)
threebutton=Button(calc,text='3',fg="black",highlightcolor="blue",command=lambda:sbutton(3),width=10)
threebutton.grid(row=4,column=3)
multbutton=Button(calc,text='*',fg="orange",highlightcolor="blue",command=lambda:sbutton("*"),width=10)
multbutton.grid(row=4,column=4)

zerobutton=Button(calc,text='0',fg="black",highlightcolor="blue",command=lambda:sbutton(0),width=10)
zerobutton.grid(row=5,column=1)
sumbutton=Button(calc,text='+',fg="red",height=1,command=lambda:sbutton("+"),width=10)
sumbutton.grid(row=5,column=2)
equalbutton=Button(calc,text='=',fg="green",highlightcolor="blue",command=equalb,width=10)
equalbutton.grid(row=5,column=3)  
diffbutton=Button(calc,text='-',fg="Blue",highlightcolor="blue",command=lambda:sbutton("-"),width=10,bd=3)
diffbutton.grid(row=5,column=4)             
calc.mainloop()