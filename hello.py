from tkinter import *
top=Tk()
top.geometry("1400x800")
top.title("dharshana")
top.config(bg="black")
def login():
  toy=Frame(top,bg="skyblue4",height=700,width=400)
  toy.pack(fill=X)
  label1=Label(toy,text="LOGIN PAGE",font=("times new roman",20,'italic'),bg="skyblue4",fg="white")
  label1.place(x=500,y=100)
  label1=Label(toy,text="Username",font=("times new roman",20,'italic'),bg="skyblue4",fg="white")
  label1.place(x=700,y=200)
  box=Entry(top,text="",font=("times new roman",20,'italic'),bg="white",fg="black")
  box.place(x=900,y=200,width=400,height=50)
  label1=Label(toy,text="Password",font=("times new roman",20,'italic'),bg="skyblue4",fg="white")
  label1.place(x=700,y=275)
  box=Entry(top,text="",font=("times new roman",20,'italic'),bg="white",fg="black")
  box.place(x=900,y=275,width=400,height=50)
  button=Button(top,text="LOGIN",font=("times new roman",20,'bold'),bg="white",fg="black",activebackground="yellow",activeforeground="black",command=login)
  button.place(x=800,y=400,width=200,height=70)
  label1=Label(toy,text="Don't have an account?",font=("times new roman",20,'italic'),bg="skyblue4",fg="white")
  label1.place(x=700,y=500)
  button=Button(top,text="SIGN IN",font=("times new roman",20,'bold'),bg="red",fg="black",activebackground="yellow",activeforeground="black",command=login)
  button.place(x=1000,y=500,width=200,height=70)
details=Label(top,text="WELCOME OUR PAGE",font=("times new roman",20,"bold"),bg="black",fg="white")
details.place(x=500,y=60)
button=Button(top,text="GET STARTED",font=("times new roman",20,'bold'),bg="white",fg="black",activebackground="yellow",activeforeground="black",command=login)
button.place(x=400,y=500,width=600,height=70)
top.mainloop()
 
                                                                                                 
