from tkinter import*

first_number= second_number=operator=None

# Defining all Functions

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')
    
def get_operator(op):
    global first_number,operator

    first_number=int(result_label['text'])
    operator=op
    result_label.config(text='')

def get_result():
    global first_number, second_number,operator

    second_number =int(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_number + second_number))
    elif  operator=='-':
        result_label.config(text=str(first_number - second_number))
    elif  operator=='*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number ==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number)))

# Creating the window for the GUI calculator
              
w=Tk()
w.title('calculator')
w.geometry('280x380')
w.resizable(0,0)

# Setting up the label formatting

result_label=Label(w,text=' ',bg='white',fg='black')
result_label.grid(row=0,column=0,columnspan=9 ,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

#Adding the buttons to the GUI calculator . griding the button on the window

b1=Button(w,text='9',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(9))
b1.grid(row=1,column=0)
b1.config(font=('verdana',14))

b2=Button(w,text='8',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(8))
b2.grid(row=1,column=1)
b2.config(font=('verdana',14))

b3=Button(w,text='7',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(7))
b3.grid(row=1,column=2)
b3.config(font=('verdana',14))

b4=Button(w,text='+',bg='white',fg='black',width=5,height=2,command= lambda:get_operator('+'))
b4.grid(row=1,column=3)
b4.config(font=('verdana',14))

b5=Button(w,text='6',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(6))
b5.grid(row=2,column=0)
b5.config(font=('verdana',14))

b6=Button(w,text='5',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(5))
b6.grid(row=2,column=1)
b6.config(font=('verdana',14))

b7=Button(w,text='4',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(4))
b7.grid(row=2,column=2)
b7.config(font=('verdana',14))

b8=Button(w,text='-',bg='white',fg='black',width=5,height=2,command= lambda:get_operator('-'))
b8.grid(row=2,column=3)
b8.config(font=('verdana',14))

b9=Button(w,text='3',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(3))
b9.grid(row=3,column=0)
b9.config(font=('verdana',14))

b10=Button(w,text='2',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(2))
b10.grid(row=3,column=1)
b10.config(font=('verdana',14))

b11=Button(w,text='1',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(1))
b11.grid(row=3,column=2)
b11.config(font=('verdana',14))

b12=Button(w,text='*',bg='white',fg='black',width=5,height=2,command= lambda:get_operator('*'))
b12.grid(row=3,column=3)
b12.config(font=('verdana',14))

b13=Button(w,text='c',bg='orange',fg='black',width=5,height=2,command=lambda:clear())
b13.grid(row=4,column=0)
b13.config(font=('verdana',14))

b14=Button(w,text='0',bg='white',fg='black',width=5,height=2,command= lambda:get_digit(0))
b14.grid(row=4,column=1)
b14.config(font=('verdana',14))

b15=Button(w,text='=',bg='green',fg='black',width=5,height=2,command=get_result)
b15.grid(row=4,column=2)
b15.config(font=('verdana',14))

b16=Button(w,text='/',bg='white',fg='black',width=5,height=2,command= lambda:get_operator('/'))
b16.grid(row=4,column=3)
b16.config(font=('verdana',14))

w.mainloop()
