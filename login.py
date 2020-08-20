from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title('Login System')
        self.root.geometry('1350x700+0+0')
        self.root.resizable(False,False)
        ########## ALL IMAGES ###########
        self.bg_icon = ImageTk.PhotoImage(file='bg.jpg')
        bg_lbl = Label(self.root, image=self.bg_icon).place(x=0,y=0)


        ##### LOGIN FRAME######
        Frame_login = Frame(self.root,bg='white')
        Frame_login.place(x=150,y=150,height=340,width=500)

        Title = Label(Frame_login,text='Login Here',font=('impact',40,'bold'),fg='#d77337',bg='white').place(x=130,y=20)

        desc = Label(Frame_login,text='Accountant Employee Login Here',font=('Goudy old style',15,'bold'),fg='#d25d17',bg='white').place(x=100,y=100)

        user = Label(Frame_login,text='User Name',font=('Goudy old style',15),fg='#d25d17',bg='white').place(x=100,y=130)
        self.user_ent = Entry(Frame_login,font=('Roman new times',15),bg='gray',fg='black')
        self.user_ent.place(x=100,y=160,height=30,width=240)

        password = Label(Frame_login, text='Password', font=('Goudy old style', 15), fg='#d25d17', bg='white').place(x=100,y=200)
        self.pass_ent = Entry(Frame_login, font=('Roman new times', 15), bg='gray', fg='black')
        self.pass_ent.place(x=100, y=230, height=30, width=240)

        forget = Button(Frame_login, text='Forget Password?',font=('Goudy old style', 15),bd=0,fg='#d77337',bg='white')
        forget.place(x=100,y=260)

        login = Button(self.root,command=self.login_system,text="login",font=('Goudy old style', 15),bg='#d77337',fg='white')
        login.place(x=320,y=470,width=150,height=40)


    def login_system(self):
        if self.user_ent.get() == '' or self.pass_ent.get() == '':
            messagebox.showerror('Error','must be filled')
        elif self.user_ent.get() != 'Parween' or self.pass_ent.get() !='123456':
            messagebox.showerror('Warning','wrong User Name/ Password')
        else:
            messagebox.showinfo('Welcome',f"Welcome{self.user_ent.get()} and Your Password is {self.pass_ent.get()}")


    # def forget_password(self):
    #     messagebox.showinfo('Password',self.pass_ent.get())






root = Tk()
obj = Login_System(root)
root.mainloop()