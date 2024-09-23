import tkinter as tk 
from tkinter import messagebox
class MyCalc : 
    def __init__(self) : 
        root=tk.Tk()
        root.geometry("800x500")

        self.label1=tk.Label(root,text='please enter the first number',font=('Arial',16))
        self.label1.pack()

        self.ip1=tk.Text(root,height=2)
        self.ip1.pack(padx=200,pady=20)

        self.label2=tk.Label(root,text='please enter the operation',font=('Arial',16))
        self.label2.pack()

        self.ip2=tk.Text(root,height=2)
        self.ip2.pack(padx=200,pady=20)

        self.label3=tk.Label(root,text='please enter the second number',font=('Arial',16))
        self.label3.pack()

        self.ip3=tk.Text(root,height=2)
        self.ip3.pack(padx=200,pady=20)

        self.button=tk.Button(root,text="Result ! :)",font=('Arial',18),fg='black',background='white',command=self.calculate)
        self.button.pack()


        root.mainloop()
    def calculate (self) : 
        x=int(self.ip1.get('1.0',tk.END).strip())
        y=int(self.ip3.get('1.0',tk.END).strip())
        operator=str(self.ip2.get('1.0',tk.END).strip())
        # print(operator)
        # print(type(operator))
        # print(type(x))

        if operator=='+' : 
            messagebox.showinfo(title="Result",message=f"The result of {x} + {y} is {x+y} !")
        elif operator=='-'  :
            messagebox.showinfo(title="Result",message=f"The result of {x} - {y} is {x-y} !")
        elif operator=='*' : 
             messagebox.showinfo(title="Result",message=f"The result of {x} * {y} is {x*y} !")
        elif operator=='/' : 
                if y != 0:
                    messagebox.showinfo(title="Result",message=x/y)
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return

    

MyCalc()