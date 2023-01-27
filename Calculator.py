import math
from tkinter import *
root = Tk()
root.title('CALCULATOR')

#string variable for the entry field
shown=StringVar()
operation=''

#changes the values in operation
def click_number(number):
    global operation
    operation=operation+str(number)
    shown.set(operation)

#evaluates the operation
def click_equal():
    global operation
    expression=str(eval(operation))
    shown.set(expression)
    operation=expression

#clears the operation and also entry 
def click_clear():
    global operation
    shown.set('')
    operation=''

#clears the last character in operation
def click_del():
    global operation
    operation=operation[:-1]
    shown.set(operation)

#calculates trignometric values of operation
def click_trig(x):
    global operation
    expression=eval(operation)
    expression=expression*(math.pi/180)
    if(x=='sin'):
        expression=str(math.sin(expression))
    elif(x=='cos'):
        expression=str(math.cos(expression))
    elif(x=='tan'):
        expression=str(math.tan(expression))
    shown.set(expression)
    operation=expression

#calculates log of operation
def click_log(x):
    global operation
    expression=eval(operation)
    if x=='log':
        expression=str(math.log(expression,10))
    elif x=='ln':
        expression=str(math.log(expression))
    shown.set(expression)
    operation=expression

#entry
e = Entry(root,width=40,borderwidth=5,textvar=shown)
e.grid(row=0,column=0,columnspan=5)


#sin,cos,tan,clear
bt1 = Button(root,text = 'sin',width=5,height=2,command=lambda:click_trig('sin')).grid(row = 1,column = 0,pady=3)
bt2 = Button(root,text = 'cos',width=5,height=2,command=lambda:click_trig('cos')).grid(row = 1,column = 1,pady=3)
bt3 = Button(root,text = 'tan',width=5,height=2,command=lambda:click_trig('tan')).grid(row = 1,column = 2,pady=3)
bt4 = Button(root,text = 'clear',width=12,height=2,command=lambda:click_clear()).grid(row = 1,column = 3,columnspan= 2,pady=3)

#ln,log,(,),+
bt5 = Button(root,text = 'ln',width=5,height=2,command=lambda:click_log('ln')).grid(row = 2,column = 0,pady=3)
bt6 = Button(root,text = 'log',width=5,height=2,command=lambda:click_log('log')).grid(row = 2,column = 1,pady=3)
bt7 = Button(root,text = '(',width=5,height=2,command=lambda:click_number('(')).grid(row = 2,column = 2,pady=3)
bt8 = Button(root,text = ')',width=5,height=2,command=lambda:click_number(')')).grid(row = 2,column = 3,pady=3)
bt9 = Button(root,text = '+',width=5,height=2,command=lambda:click_number('+')).grid(row = 2,column = 4,pady=3)

#square,1,2,3,-
bt10 = Button(root,text = 'sqr',width=5,height=2,command=lambda:click_number('**2')).grid(row = 3 ,column = 0,pady=3)
bt11 = Button(root,text = '1',width=5,height=2,command=lambda:click_number(1)).grid(row = 3,column = 1,pady=3)
bt12 = Button(root,text = '2',width=5,height=2,command=lambda:click_number(2)).grid(row = 3,column = 2,pady=3)
bt13 = Button(root,text = '3',width=5,height=2,command=lambda:click_number(3)).grid(row = 3,column = 3,pady=3)
bt14 = Button(root,text = '-',width=5,height=2,command=lambda:click_number('-')).grid(row = 3,column = 4,pady=3)

#power,4,5,6,*
bt15 = Button(root,text = 'pow',width=5,height=2,command=lambda:click_number('**')).grid(row = 4,column = 0,pady=3)
bt16 = Button(root,text = '4',width=5,height=2,command=lambda:click_number(4)).grid(row = 4,column = 1,pady=3)
bt17 = Button(root,text = '5',width=5,height=2,command=lambda:click_number(5)).grid(row = 4,column = 2,pady=3)
bt18 = Button(root,text = '6',width=5,height=2,command=lambda:click_number(6)).grid(row = 4,column = 3,pady=3)
bt19 = Button(root,text = 'x',width=5,height=2,command=lambda:click_number('*')).grid(row = 4,column = 4,pady=3)

#root,7,8,9,/
bt20 = Button(root,text = 'rt',width=5,height=2,command=lambda:click_number('**0.5')).grid(row = 5,column = 0,pady=3)
bt21 = Button(root,text = '7',width=5,height=2,command=lambda:click_number(7)).grid(row = 5,column = 1,pady=3)
bt22 = Button(root,text = '8',width=5,height=2,command=lambda:click_number(8)).grid(row = 5,column = 2,pady=3)
bt23 = Button(root,text = '9',width=5,height=2,command=lambda:click_number(9)).grid(row = 5,column = 3,pady=3)
bt24 = Button(root,text = '/',width=5,height=2,command=lambda:click_number('/')).grid(row = 5,column = 4,pady=3)

#pi,.,0,del,=
bt25 = Button(root,text = '\u03C0',width=5,height=2,command=lambda:click_number(math.pi)).grid(row = 6,column = 0,pady=3)
bt26 = Button(root,text = '.',width=5,height=2,command=lambda:click_number('.')).grid(row = 6,column = 1,pady=3)
bt27 = Button(root,text = '0',width=5,height=2,command=lambda:click_number(0)).grid(row = 6,column = 2,pady=3)
bt28 = Button(root,text = 'del',width=5,height=2,command=lambda:click_del()).grid(row = 6,column = 3,pady=3)
bt29 = Button(root,text = '=',width=5,height=2,command=lambda:click_equal()).grid(row = 6,column = 4,pady=3)

root.mainloop()
