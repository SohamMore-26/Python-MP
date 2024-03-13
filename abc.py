
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import pymysql as mq


def insertData(full_name, age, gender, teacher_id, branch, dob,master) :
    mysql=mq.connect(host="localhost",user="root",password="12345678",database="pythonproject")
    mycursor=mysql.cursor()
    try:
        print("",gender)
        mycursor.execute("INSERT INTO teacher (name, age, gender, teacher_id, branch, dateOfBirth) VALUES (%s, %s, %s, %s, %s, %s)",(full_name, age, gender, teacher_id, branch, dob))
        mysql.commit()
        messagebox.showinfo("Successfull","Data entered successfully")
        master.switch_frame(StartPage)
    except mq.Error as e :
        print("Error",e)


    

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        self.geometry("500x600")
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.config(width=500,height=500)
        

        button = tk.Button(self,text="Enter Teacher Data",height=5,width=37,font=("Ariel",15),command=lambda: master.switch_frame(PageOne))
        button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        button2 = tk.Button(self,text="View Teacher Data" ,height=5,width=37,font=("Ariel",15),command=lambda: master.switch_frame(PageTwo))
        button2.place (relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        branch_list = ["Computer Engineering", "Mechanical Engineering", "Electrical Engineering"]
        value_inside = tk.StringVar(self)
        value_inside.set("Select an option")

        label_name = tk.Label(self, text="Teacher Registration", font=("Arial", 18))
        label_name.grid(row=0, column=0, columnspan=2, pady=10)

        label_full_name = tk.Label(self, text="Full Name:", font=("Arial", 12))
        label_full_name.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        entry_full_name = tk.Entry(self, font=("Arial", 12))
        entry_full_name.grid(row=1, column=1, padx=10, pady=5)

        label_age = tk.Label(self, text="Age:", font=("Arial", 12))
        label_age.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        entry_age = tk.Entry(self, font=("Arial", 12))
        entry_age.grid(row=2, column=1, padx=10, pady=5)

        label_gender = tk.Label(self, text="Gender:", font=("Arial", 12))
        label_gender.grid(row=3, column=0, sticky="e", padx=10, pady=5)

        x = tk.StringVar(self,"MALE")
        entry_gender_m = tk.Radiobutton(self, text="MALE", font=("Arial", 12), variable=x, value="MALE")
        entry_gender_m.grid(row=3, column=1, padx=10, pady=5)
        entry_gender_f = tk.Radiobutton(self, text="FEMALE", font=("Arial", 12), variable=x, value="FEMALE")
        entry_gender_f.grid(row=3, column=2, padx=10, pady=5)

        label_ID = tk.Label(self, text="Teacher ID:", font=("Arial", 12))
        label_ID.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        entry_ID = tk.Entry(self, font=("Arial", 12))
        entry_ID.grid(row=4, column=1, padx=10, pady=5)

        label_branch = tk.Label(self, text="Branch:", font=("Arial", 12))
        label_branch.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        bm = tk.OptionMenu(self, value_inside, *branch_list)
        bm.grid(row=5, column=1, padx=10, pady=5)

        label_dob = tk.Label(self, text="D.O.B:", font=("Arial", 12))
        label_dob.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        entry_dob = Calendar(self, selectmode='day', year=2020, month=5, day=22)
        entry_dob.grid(row=6, column=1, padx=10, pady=5)

        button_back = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: master.switch_frame(StartPage))
        button_back.grid(row=7, column=0, padx=(10, 5), pady=10)

        button_submit = tk.Button(self, text="Submit", font=("Arial", 15),command=lambda: insertData(entry_full_name.get(), entry_age.get(),
                                                             x.get(), entry_ID.get(), value_inside.get(),
                                                             entry_dob.get_date(),master))
        button_submit.grid(row=7, column=1, padx=(5, 10), pady=60)

    
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
