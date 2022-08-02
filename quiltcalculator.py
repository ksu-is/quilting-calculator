from doctest import master
from tkinter import *
from math import sqrt as sqr

class calculator(Frame):

    def __init__(self, master):
       
        Frame.__init__(self, master)
        self.entry = Entry(master, width=30, font=("Arial",25))
        self.entry.grid(row=0, column=0, columnspan=1, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()

    def add_chr(self, char, btn=None):
        
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
        """Button to clear calculator"""
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):
        """Button to clear all of calculator"""
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        """Allows for quilt name to display without visible numbers"""
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("Throw","50X60")
        e = e.replace("Full","54X75")
        e = e.replace("Queen","60X80")
        e = e.replace("King","76X80")

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0, END)
            self.entry.insert(0, "Invalid")
        else:
            self.entry.delete(0,END)

    def flash(self, btn):

        if btn != None:
            btn.config(bg="pink")
            if btn ==self.c_bttn:
                self.clear()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="lightgrey"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()                
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            else:
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
        else:
            pass

    def bind_buttons(self, master):
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("Throw", lambda event, char="5", btn=self.throw_bttn: self.add_chr(char, btn))
        master.bind("Full", lambda event, char="8", btn=self.full_bttn: self.add_chr(char, btn))
        master.bind("Queen", lambda event, char="12", btn=self.queen_bttn: self.add_chr(char, btn))
        master.bind("King", lambda event, char="14", btn=self.king_bttn: self.add_chr(char, btn))
        master.bind("1/4 Seam", lambda event, char=".25", btn=self.quarter_bttn: self.add_chr(char, btn))
        master.bind("1/2 Seam", lambda event, char=".5", btn=self.half_bttn: self.add_chr(char, btn))
        master.bind("X", lambda event, char="*", btn=self.multiply_bttn: self.add_chr(char, btn))

    def create_widgets(self):
        self.eq_bttn = Button(self, text="Calculate", width=70, height=3, bg="white", fg="black", command=lambda: self.calculate())
        self.eq_bttn.grid(row=4, column=0, columnspan=4)

        self.ac_bttn = Button(self, text='Clear', width=22, height=3, bg='Lightgreen', fg='black',command=lambda: self.clear_all())
        self.ac_bttn.grid(row=1, column=2)

        self.c_bttn = Button(self, text='←', width=22, height=3, bg='Lightgreen', fg='black',command=lambda: self.clear())
        self.c_bttn.grid(row=2, column=2 )

        self.multiply_bttn = Button(self, text="X", width=22, height=3,bg='Lightgreen', fg='black', command=lambda: self.add_chr('*'))
        self.multiply_bttn.grid(row=3, column=2)

        self.throw_bttn = Button(self, text="Throw", width=22, height=3,bg='Lightgreen', fg='black', command=lambda: self.add_chr('5'))
        self.throw_bttn.grid(row=2, column=0)

        self.full_bttn = Button(self, text="Full", width=22, height=3, bg='Lightgreen', fg='black',command=lambda: self.add_chr('8'))
        self.full_bttn.grid(row=2, column=1)

        self.queen_bttn = Button(self, text="Queen", width=22, height=3,bg='Lightgreen', fg='black', command=lambda: self.add_chr('12'))
        self.queen_bttn.grid(row=3, column=0)

        self.king_bttn = Button(self, text="King", width=22, height=3,bg='Lightgreen', fg='black', command=lambda: self.add_chr('14'))
        self.king_bttn.grid(row=3, column=1)

        self.quarter_bttn = Button(self, text="1/4 Seam", width=22, height=3, bg='Lightgreen', fg='black',command=lambda: self.add_chr(".25"))
        self.quarter_bttn.grid(row=1, column=0)

        self.half_bttn = Button(self, text="1/2 Seam", width=22, height=3, bg='Lightgreen', fg='black',command=lambda: self.add_chr(".5"))
        self.half_bttn.grid(row=1, column=1)

root = Tk()
root.geometry()
root.title("Calculator")
app = calculator(root)
root.mainloop()



