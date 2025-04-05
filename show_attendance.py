import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def deptchoose(text_to_speech):
    def calculate_attendance():
        dept = tx.get()
        if dept=="":
            t='Please enter the dept name.'
            text_to_speech(t)
    
        filenames = glob(
            f"Attendance\\{dept}\\{dept}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv(f"Attendance\\{dept}\\attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of "+dept)
        root.configure(background="black")
        cs = f"Attendance\\{dept}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    dept = Tk()
    # windo.iconbitmap("AMS.ico")
    dept.title("dept...")
    dept.geometry("580x320")
    dept.resizable(0, 0)
    dept.configure(background="black")
    # dept_logo = Image.open("UI_Image/0004.png")
    # dept_logo = dept_logo.resize((50, 47), Image.ANTIALIAS)
    # dept_logo1 = ImageTk.PhotoImage(dept_logo)
    titl = tk.Label(dept, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(dept, image=dept_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        dept,
        text="Which dept of Attendance?",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the dept name!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"Attendance\\{sub}"
            )


    attf = tk.Button(
        dept,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        dept,
        text="Enter dept",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        dept,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        dept,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    dept.mainloop()
