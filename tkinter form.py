from tkinter import *
root = Tk()
root.geometry('500x500')
root.title("Input Speed")

Fullname=StringVar()
spd1 = IntVar()
spd2= IntVar()

name1=Fullname.get()
graph1=spd1.get()
graph2=spd2.get()

label_0 = Label(root, text="rocket simulator",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Stage 1 speed",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
label_2a = Label (root, text ="(ideal = 2683m/s)", width=20, font = ("bold",10))
label_2a.place (x=68,y=200)

entry_2 = Entry(root,textvar=spd1)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Stage 2 speed",width=20,font=("bold", 10))
label_3.place(x=68,y=230)
label_3a = Label (root, text ="(ideal = 994m/s)", width=20, font = ("bold",10))
label_3a.place (x=68,y=250)

entry_3 = Entry(root,textvar=spd2)
entry_3.place(x=240,y=230)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

Button(root, text="start simulation", command=root.destroy).pack()



