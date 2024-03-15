
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import pymysql as mq


mysql=mq.connect(host="localhost",user="root",password="12345678",database="pythonproject")
mycursor=mysql.cursor()

def insertData(full_name, age, gender, teacher_id, branch, dob,master) :
    
    try:
        mycursor.execute("INSERT INTO teacher (name, age, gender, teacher_id, branch, dateOfBirth) VALUES (%s, %s, %s, %s, %s, %s)",(full_name, age, gender, teacher_id, branch, dob))
        mysql.commit()
        messagebox.showinfo("Successfull","Data entered successfully")
        master.switch_frame(StartPage)
    except mq.Error as e :
        print("Error",e)
        messagebox.showerror("Error","Invalid Input")
        master.switch_frame(StartPage)


def deleteData(id,master):
    

    mycursor.execute("SELECT * from teacher")
    result = mycursor.fetchall()

    print(result)

    flag = False
    for i in result :
        if id in i:
            flag = True
            break

    if flag:

        try:
            query = "Delete from teacher where teacher_id = %s"
            mycursor.execute(query,id)
            mysql.commit()

            messagebox.showinfo("Successfull","Data Deleted Successfully")
            master.switch_frame(StartPage)

        except mq.Error as e :
            print("Error",e)
    else :
        messagebox.showerror("Error","ID not available")
        master.switch_frame(StartPage)


def getData(branch,gender):

    if branch == "All Branches" and gender == "All Teachers":
        mycursor.execute("SELECT * from teacher")

    elif branch == "All Branches":
        mycursor.execute("SELECT * from teacher Where gender=%s",(gender))
    elif branch == "All Teachers":
        mycursor.execute("SELECT * from teacher Where branch=%s",(branch))

    else:
        mycursor.execute("SELECT * from teacher Where branch=%s and gender = %s",(branch,gender))
    result = mycursor.fetchall()
    return result

def displayData(branch,gender,master,self):
    mysql=mq.connect(host="localhost",user="root",password="12345678",database="pythonproject")
    mycursor=mysql.cursor()

    
    teacherList=getData(branch,gender)

    parameter = ("ID","Name","Age","Gender","Branch","Birth Date")

    for i in range(len(parameter)):
        tk.e=Entry(self,width=15,fg='black',font=('Arial',16,'bold'),justify='center')
        tk.e.grid(row=2,column=i)
        tk.e.insert(tk.END,parameter[i])
        
    for i in range(len(teacherList)):
        for j in range(len(teacherList[i])):
            tk.e=Entry(self,width=15,fg='blue',font=('Arial',16,'bold'),justify='center')
            tk.e.grid(row=i+3,column=j)
            tk.e.insert(tk.END,teacherList[i][j])


    

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
        button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        
        button2 = tk.Button(self,text="View Teacher Data" ,height=5,width=37,font=("Ariel",15),command=lambda: master.switch_frame(PageTwo))
        button2.place (relx=0.5, rely=0.5, anchor=tk.CENTER)

        button3 = tk.Button(self,text="Delete Teacher Data" ,height=5,width=37,font=("Ariel",15),command=lambda: master.switch_frame(PageThree))
        button3.place (relx=0.5, rely=0.8, anchor=tk.CENTER)
        
        

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
        entry_gender_m = tk.Radiobutton(self, text="Male", font=("Arial", 12), variable=x, value="MALE")
        entry_gender_m.grid(row=3, column=1)
        entry_gender_f = tk.Radiobutton(self, text="Female", font=("Arial", 12), variable=x, value="FEMALE")
        entry_gender_f.grid(row=3, column=2)

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

        button_back = tk.Button(self, text="Back", font=("Arial", 15), width=10,command=lambda: master.switch_frame(StartPage))
        button_back.grid(row=7, column=0, padx=(10, 5), pady=10)

        button_submit = tk.Button(self, width=10,text="Submit", font=("Arial", 15),command=lambda: insertData(entry_full_name.get(), entry_age.get(),
                                                             x.get(), entry_ID.get(), value_inside.get(),
                                                             entry_dob.get_date(),master))
        button_submit.grid(row=7, column=1, padx=(5, 10), pady=60)

    
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        filter = tk.Label(self, text="Select Filters : ", font=("Arial", 12))
        filter.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        branch_list = ["Computer Engineering", "Mechanical Engineering", "Electrical Engineering","All Branches"]
        value_inside1 = tk.StringVar(self)
        value_inside1.set("All Branches")


        gender_list = ["Male","Female","All Teachers"]
        value_inside2 = tk.StringVar(self)
        value_inside2.set("All Teachers")

        bm = tk.OptionMenu(self, value_inside1, *branch_list)
        bm.grid(row=0, column=1, padx=10, pady=5)

        gm = tk.OptionMenu(self, value_inside2, *gender_list)
        gm.grid(row=0, column=2, padx=10, pady=5)

        button_back = tk.Button(self, text="Back", width=9,font=("Arial", 12), command=lambda: master.switch_frame(StartPage))
        button_back.grid(row=1, column=0, padx=(10, 5), pady=10)

        submit_button = tk.Button(self, text="Display Data",width=10,font=("Arial", 12),command=lambda:displayData(value_inside1.get(),value_inside2.get(),master,self))
        submit_button.grid(row=1, column=1,  padx=(20, 5), pady=10)


        # teacherList=getData()
        
        # parameter = ("ID","Name","Age","Gender","Branch","Birth Date")

        # for i in range(len(parameter)):
        #         tk.e=Entry(self,width=15,fg='black',font=('Arial',16,'bold'),justify='center')
        #         tk.e.grid(row=0,column=i)
        #         tk.e.insert(tk.END,parameter[i])
        
        # for i in range(len(teacherList)):
        #     for j in range(len(teacherList[i])):
        #         tk.e=Entry(self,width=15,fg='blue',font=('Arial',16,'bold'),justify='center')
        #         tk.e.grid(row=i+1,column=j)
        #         tk.e.insert(tk.END,teacherList[i][j])

            
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        title = tk.Label(self, text="Delete Teacher Data", font=("Arial", 18))
        title.grid(row=0, column=1, columnspan=3, pady=10)

        label1 = tk.Label(self, text="Enter Teacher ID  : ", font=("Arial", 12))
        label1.grid(row=1, column=0, columnspan=2, pady=10,padx=10)

        deleteId = tk.Entry(self, font=("Arial", 12))
        deleteId.grid(row=1, column=2, padx=10, pady=5)

        button_back = tk.Button(self, text="Back", width=10,font=("Arial", 15), command=lambda: master.switch_frame(StartPage))
        button_back.grid(row=2, column=1, padx=(10, 5), pady=10)

        submit_button = tk.Button(self, text="Submit",width=10,font=("Arial", 15),command=lambda: deleteData(deleteId.get(),master))
        submit_button.grid(row=2, column=2,  padx=(20, 5), pady=10)
    




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
