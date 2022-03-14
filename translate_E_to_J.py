from asyncio import subprocess
from itertools import count
from logging import root
from re import sub
import tkinter as tk
from unicodedata import name



def window_contents():

    sub_window = tk.Toplevel()
    sub_window.geometry("300x300")
    sub_window.title(u"sub window")
    sub_button_A =tk.Button(sub_window, text="午前在宅+午後出社",command=process_A)
    sub_button_A.pack()
    sub_button_B =tk.Button(sub_window,text="午前出社+午後在宅",command=process_B)
    sub_button_B.pack()
    sub_button_C =tk.Button(sub_window,text="終日在宅",command=process_C)
    sub_button_C.pack()
    sub_button_D =tk.Button(sub_window,text="終日出社",command=process_D)
    sub_button_D.pack() 


if __name__ == '__main__':
    root1 = tk.Tk()
    root1.geometry("300x300")
    frame = tk.Frame(root1)
    frame.pack(fill = tk.BOTH, padx=5, pady=10)
    name_button = tk.Button(text='takiguchi',command=window_contents)
    name_button.pack()

    root1.mainloop()

