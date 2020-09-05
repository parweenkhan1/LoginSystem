from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Login System')
        self.root.iconbitmap('logo.ico')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False,False)
    #  Images
        self.bg = ImageTk.PhotoImage(file='bg.jpg')
        bg_image = Label(self.root,image=self.bg).place(x=0,y=0)
        self.user = PhotoImage(file='../loginSystem/user.png')
        self.user_logo = PhotoImage(file='../loginSystem/userlogo.png')
        self.password = PhotoImage(file='../loginSystem/password1.png')



        Title = Label(self.root,text='LOGIN SYSTEM',font=("Goudy new style",40),bg='#d09784',fg='brown',bd=10,relief=GROOVE)
        Title.place(x=0,y=0,relwidth=1)

        login_frame = Label(self.root,bg='#d09784')
        login_frame.place(x=400,y=200,height=370,width=500)

        user_image = Label(login_frame,image=self.user,bd=10,relief=GROOVE).place(x=180,y=10)
        user_lbl = Label(login_frame,text='User Name :',font=('times new roman',15,'bold'),fg='black',bg='#d09784').place(x=20,y=150)
        userlogo_image = Label(login_frame,image=self.user_logo)
        userlogo_image.place(x=40,y=180)
        self.user_entry = Entry(login_frame,font=('times new roman',20))
        self.user_entry.place(x=150,y=180,height=40)
        pass_lbl = Label(login_frame,text='Password :',font=('times new roman',15,'bold'),fg='black',bg='#d09784')
        pass_lbl.place(x=20,y=230)
        password_image = Label(login_frame,image=self.password).place(x=40,y=260)
        self.password_entry = Entry(login_frame,font=('times new roman',20))
        self.password_entry.place(x=150,y=260,height=40)

        forget = Button(login_frame,text='forgot password?',font=('times new roman',15),bd=0,bg='#d09784').place(x=20,y=330)
        login = Button(self.root,command=self.LogIn,text='login',font=('times new roman',15))
        login.place(x=600,y=550,width=100)

    def LogIn(self):
        if self.user_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror("Error","All fields are required")
        elif self.user_entry.get() != "Parween khan" or self.password_entry.get() !="123456":
            messagebox.showerror("Error","Wrong username/password")
        else:
            messagebox.showinfo("Welcome",f"welcome {self.user_entry.get()} and your password is {self.password_entry.get()}")


root = Tk()
obj = Login_System(root)
root.mainloop()