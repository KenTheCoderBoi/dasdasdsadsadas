from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("sus test")
title= Label(root,text="covid test")
title.pack()

Q1= Label(root,text="are you cough?")
Q1.pack()
Q1_value= StringVar(value="0")

yes1 = Radiobutton(root,text="yes",variable= Q1_value,value="yes")
yes1.place(relx=0.45,rely=0.1,anchor=CENTER)

no1=Radiobutton(root,text="no",variable= Q1_value,value="no")
no1.place(relx=0.55,rely=0.1,anchor=CENTER)

Q2=Label(root,text="are you fever?")
Q2.place(relx=0.5,rely=0.13,anchor=CENTER)
Q2_value= StringVar(value="0")

yes2= Radiobutton(root,text="yes",variable= Q2_value,value="yes")
yes2.place(relx=0.45, rely=0.17,anchor=CENTER)

no2=Radiobutton(root,text="no",variable= Q2_value,value="no")
no2.place(relx=0.55, rely=0.17,anchor=CENTER)

Q3=Label(root,text="are you dry throat?")
Q3.place(relx=0.5,rely=0.2,anchor=CENTER)
Q3_value=StringVar(value="0")

yes3= Radiobutton(root,text="yes",variable= Q3_value,value="yes")
yes3.place(relx=0.45, rely=0.24,anchor=CENTER)

no3=Radiobutton(root,text="no",variable= Q3_value,value="no")
no3.place(relx=0.55, rely=0.24,anchor=CENTER)
def test():
    sus_score=0
    if Q1_value.get()=="yes":
        sus_score+=10
    if Q2_value.get()=="yes":
        sus_score+=10
    if Q3_value.get()=="yes":
        sus_score+=10
    if sus_score<=10:
        messagebox.showinfo("Report","The person isnt sick")
    elif sus_score<=20:
        messagebox.showinfo("Report","The person is kinda covid")
    else:
        messagebox.showinfo("Report","The person is very very covid")
button= Button(root, text="test",command=test)
button.place(relx=0.5, rely=0.3, anchor=CENTER)
root.mainloop()