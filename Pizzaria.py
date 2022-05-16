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
        self.scr.iconbitmap('ICONM.png')
        
        # Imagem de Banner
        self.mainf1 = Frame(self.scr, height=150, width=1366)
        self.banner = PhotoImage(file='mosaico.png')
        self.b =Label(self.mainf1, image=self.banner)
        self.b.place(x=0, y=0)
        self.mainf1.pack(fill=BOTH, expand=1)
        
        # Imagem de Background
        self.mainf2 = Frame(self.scr, height=616, width=1366)
        self.c = Canvas(self.mainf2, height=616, width=1366)
        self.c.pack()
        self.back = PhotoImage(file='banner.png')
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
        self.scr.iconbitmap('ICONM.png')
        
        self.loginf1 = Frame(self.scr, height=150, width=1366)
        self.bannerlogin = PhotoImage(file='mosaico.png')
        self.bl =Label(self.loginf1, image=self.bannerlogin, height=150).place(x=0, y=0)
        
        
        # Botão de ir para inicio
        self.btnHome = Button(self.loginf1, text='Home', command=lambda:self.main(),cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnHome.place(x=800, y=100)
        
        
        # Botão de ir para Admin
        self.btnAdmine = Button(self.loginf1, text='Administrado login' ,cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnAdmine.place(x=925, y=100)
        
        
        # Botão de ir para Sobre
        self.btnSobre = Button(self.loginf1, text='Sobre Nós' ,cursor='hand2', bd=2, border=2, font=('cooper black', 10, 'bold'),fg='white', bg='green')
        self.btnSobre.place(x=1200, y=100)
        self.loginf1.pack(fill=BOTH, expand=1)
        
        # Imagem de Background
        self.back1 = PhotoImage(file='banner.png')
        self.c.create_image(683, 309, image=self.back1)
        
            
x=Pizzaria()
x.main()