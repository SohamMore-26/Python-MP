from tkinter import *

window = Tk()

window.geometry("500x600")
window.title("Teacher Registration")

label_name = Label(window,text="Teacher Registration",font=("Ariel",18))
label_name.place (x=140, y =0)

label_name = Label(window,text="Full Name: ",font=("Ariel",12))
label_name.place (x=50, y =50)
entryname = Entry(window,font=("Ariel",12))
entryname.place(x=200, y =50)

label_age = Label(window,text="Age: ",font=("Ariel",12))
label_age.place (x=50, y =100)
entry_age = Entry(window,font=("Ariel",12))
entry_age.place(x=200, y =100)

label_gender = Label(window,text="Gender: ",font=("Ariel",12))
label_gender.place (x=50, y =150)
x = IntVar()
entry_gender_m = Radiobutton(window,text="MALE",font=("Ariel",12), variable=x , value=0)
entry_gender_m.place(x=200, y =150)
entry_gender_f = Radiobutton(window,text="FEMALE",font=("Ariel",12), variable=x , value=1)
entry_gender_f.place(x=300, y =150)

label_ID = Label(window,text="Teacher ID: ",font=("Ariel",12))
label_ID.place (x=50, y =200)
entry_ID = Entry(window,font=("Ariel",12))
entry_ID.place(x=200, y =200)

label_dob = Label(window,text="D.O.B: ",font=("Ariel",12))
label_dob.place (x=50, y =250)
entry_dob = Entry(window,font=("Ariel",12))
entry_dob.place (x=200, y =250)

button = Button(window,text="Submit" ,font=("Ariel",15))
button.place (x=200, y =350)

window.mainloop()