# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 08:51:42 2022

@author: pc
"""
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

from tkinter import ttk,END



from users import Users,User
from films import Films,Film

Allusers=Users()
user=User("u1","u1","simple")
AllFilms =Films()

def screen_geometry():
    width, height = 660, 500
    # root.geometry('%dx%d+0+0' % (width, height))

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # root.geometry('%dx%d+0+0' % (screen_width, screen_height))

    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry('{}x{}+{}+{}'.format(width, height, x_cord, y_cord))
    
    
root = tk.Tk()
root.title(" Films ")
screen_geometry()

# __________________fonts __________________
lbl_font = font.Font(family='Calibri',
                     size='22')
txt_font = font.Font(family='Calibri',
                     size='14')


# ___________________Frames start ______________
login = tk.Frame(root)
login.config(bg='white')



Acceuil2 = tk.Frame(root)
Acceuil2.configure(bg='white')


# __________________ User login frame starts __________________
uog_label = tk.Label(login, bg='white')# image=uog_img,
uog_label.pack(pady=10)

sign_in_label = tk.Label(login,
                         text='Sign in',
                         font=lbl_font,
                         bg='white')

sign_in_label.pack(pady=15)
password_label = tk.Label(login, text='Enter username', font=lbl_font, bg='white')
password_label.pack(pady=5)

userid_entry = tk.Entry(login, font=txt_font, width=25)
userid_entry.configure(border=1)
userid_entry.pack(pady=20)
password_label = tk.Label(login, text='Enter Password', font=lbl_font, bg='white')
password_label.pack(pady=5)

userPass_entry = tk.Entry(login, font=txt_font,show="*", width=25)
userPass_entry.configure(border=1)
userPass_entry.pack(pady=20)


def login_method():
    global user
    username=userid_entry.get()
    password=userPass_entry.get()
    
    user=User(username,password)
    try: 
         
         user =Allusers.loginUser(user)
         if not user:
                messagebox.showerror("Error", "Could not login (Wrong data )")
         else: 
             
             
             if user.userType=="admin":
             
                 #Acceuil.pack(fill='both', expand=1)
                        root.withdraw()
                        root.destroy()
                        
                        import admin
                        admin.main()
                
             else:
                 login.forget()

                 #print(2)
                 Acceuil2.pack(fill='both', expand=1)  
                
             """"""
            
    except:
         messagebox.showerror("Error", "Could not login (Wrong data )")

    userPass_entry.delete(0,END)
    userPass_entry.insert(0,"")
next_btn = tk.Button(login, text='login', fg='white', bg='#0096FF',font=lbl_font)
next_btn.config(width=8, height=1,
                font=txt_font,
                command=login_method)
next_btn.pack(pady=20)


# ___________________ Acceuil2 _______________

tabControl = ttk.Notebook(Acceuil2)
s = ttk.Style()
s.configure('new.TFrame', background='#fff')

tab1 = ttk.Frame(tabControl, style='new.TFrame')
tab2 = ttk.Frame(tabControl, style='new.TFrame')


tabControl.add(tab1, text ='films')

tabControl.add(tab2, text ='Films',)

entry1=tk.Label(tab1, text="nomFilm",font=lbl_font, bg='white' )
            
        
entry1.grid(row=0,column=2)
           


entry1=tk.Label(tab1, text="Cas  ",font=lbl_font, bg='white' )
            
entry1.grid(row=0,column=3)


for w,film in enumerate(AllFilms.films):
            
            #button.pack()
            
            w=w+1
           
            if film.user:
                if film.user==user:
                            entry1=tk.Label(tab1, text=film.nomFilm,font=lbl_font, bg='white' )
            
        
                            entry1.grid(row=w,column=2)
            
                            entry1=tk.Label(tab1, text="Chez moi", font=lbl_font, bg='white')
                            entry1.grid(row=w,column=3)
            else:
                            entry1=tk.Label(tab1, text=film.nomFilm,font=lbl_font, bg='white' )
            
        
                            entry1.grid(row=w,column=2)
                            entry1=tk.Label(tab1, text="Disponible",font=lbl_font, bg='white' )
                            entry1.grid(row=w,column=3)

tabControl.add(tab2, text ='other')

def deconnecter():
   
    Acceuil2.forget()
    login.pack(fill='both', expand=1) 
loguout = tk.Button(tab2, text='logout ', fg='white', bg='#0096FF')
loguout.config(width=8, height=1,
                font=txt_font,
                command=deconnecter)

loguout.pack(pady=20)
cl = tk.Button(tab2, text='Close ', fg='white', bg='#0096FF')
cl.config(width=18, height=1,
                font=txt_font,
                command=root.destroy )
cl.pack(pady=20)
tabControl.pack(expand = 1, fill ="both")




#________________________Main___________________
login.pack(fill='both', expand=1)


def main():
    
    root.mainloop()
    
if __name__=='__main__':
    main()
    