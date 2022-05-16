from tkinter import*
import time
import random
from tkinter import messagebox
from webbrowser import BackgroundBrowser 


class Pizzaria:
    def main(self):
        try:
            self.scr.destroy()
            self.scr=Tk()
        except:
            try:
                self.scr=Tk()
            except:
                pass 
        
        
        # Titulo, logo e tamanho do display
        self.scr.geometry('1366x768')
        self.scr.title('Pizzaria Anderson')
        self.scr.iconbitmap('icon.ico')
        
        # Imagem de Banner
        self.mainf1 = Frame(self.scr, height=150, width=1366)
        self.banner = PhotoImage(file='logo1.png')
        self.b =Label(self.mainf1, image=self.banner)
        self.b.place(x=0, y=0)
        self.mainf1.pack(fill=BOTH, expand=False)
        
        # Imagem de Background
        self.mainf2 = Frame(self.scr, height=616, width=1360)
        self.c = Canvas(self.mainf2, height=616, width=1360)
        self.c.pack()
        self.back = PhotoImage(file='pizzamain.png')
        self.c.create_image(683, 284, image=self.back)
        
        # Botão de ir para Menu
        self.button = Button(self.mainf2, text='MENU', command=lambda:self.Login(),cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.button.place(x=250, y=15)
        
        self.mainf2.pack(fill=BOTH, expand=1)
                
        self.scr.mainloop()
        
    def Login(self):
        self.scr.destroy()
        self.scr=Tk()
        
        self.scr.geometry('1366x768')
        self.scr.title('Pizzaria Anderson')
        self.scr.iconbitmap('icon.ico')
        
        self.loginf1 = Frame(self.scr, height=150, width=1366)
        self.bannerlogin = PhotoImage(file='logo1.png')
        self.bl =Label(self.loginf1, image=self.bannerlogin, height=150).place(x=0, y=0)
        
        
        # Botão de ir para inicio
        self.btnHome = Button(self.loginf1, text='Home', command=lambda:self.main(),cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnHome.place(x=800, y=100)
        
        
        # Botão de ir para Admin
        self.btnAdmine = Button(self.loginf1, text='Administrado login' ,cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnAdmine.place(x=925, y=100)
        
        
        # Botão de ir para Sobre
        self.btnSobre = Button(self.loginf1, text='Sobre Nós' ,command=lambda:self.about(), cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnSobre.place(x=1200, y=100)
        self.loginf1.pack(fill=BOTH, expand=1)
        
        
         # Label de data e hora
        self.localtime=(time.strftime('%d/%m/%Y %H:%M'))
        self.tim=Label(self.loginf1,text=self.localtime,fg="white",font=("default",18, 'bold'),bg="#0b1335")
        self.tim.place(x=1150,y=40)
        
        
        # Imagem de Background
        self.loginf2 = Frame(self.scr, height=616, width=1360)
        self.c = Canvas(self.loginf2, height=616, width=1360)
        self.c.pack()
        self.back = PhotoImage(file='pizzamain.png')
        self.c.create_image(683, 284, image=self.back)


        self.c.create_rectangle(375,100,980,450, fill='#d3ede6',outline='white', width=6)
        self.logo= Label(self.loginf2, text='LOGIN ADMINISTRADOR',fg="white", font=("cooper black",26, 'bold'),bg="#0b1335",width=28)
        self.logo.place(x=380, y=101)
                

        self.lab1 = Label(self.loginf2, text='Usuario:', font=("cooper black",22, 'bold'),bg="#d3ede6")
        self.lab1.place(x=420, y=180)
        
        self.user = Entry(self.loginf2, font=("cooper black",18, 'bold'),bg="white", bd=1, justify='left')
        self.user.place(x=580, y=185)
        
        
        
        self.lab1 = Label(self.loginf2, text='Senha: ', font=("cooper black",22, 'bold'),bg="#d3ede6")
        self.lab1.place(x=420, y=250)
        
        self.pasd = Entry(self.loginf2, font=("cooper black",18, 'bold'),bg="white", bd=1, justify='left')
        self.pasd.place(x=580, y=255)
        
        self.btnLogin = Button(self.loginf2, text='Login:',cursor='hand2', font=('cooper black', 16, 'bold'),fg='white', bg='blue', bd=1)
        self.btnLogin.place(x=630, y=340)
        
        
        self.loginf2.pack(fill=BOTH, expand=1)
        self.scr.mainloop()
        
        
        
    def about(self):
        self.src1=Tk()
        self.src1.geometry('400x550')
        self.src1.config(bg='light pink')
        self.src1.title('Pizzaria Anderson / Sobre')
        self.src1.iconbitmap('icon.ico')
        
        
        self.label = Label(self.src1, text='lorem\n lorem', font=("cooper black",22, 'bold'),bg='light pink')
        self.label.pack()
        self.scr1.mainloop()
                
            
x=Pizzaria()
x.main()