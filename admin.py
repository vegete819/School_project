# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

from tkinter import ttk



from users import Users,User
from films import Films,Film

Allusers=Users()
user=User("u1","u1","simple")
AllFilms =Films()


def screen_geometry():
    width, height = 660, 800
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


#---------------------frames-------------


Acceuil = tk.Frame(root,name="acceuil")
Acceuil.configure(bg='white')



EditPassWord = tk.Frame(root)
EditPassWord.configure(bg='white')



Films = tk.Frame(root)
Films.config(bg='white')

users = tk.Frame(root)
users.config(bg='white')

# ___________________ Acceuil _______________

tabControl = ttk.Notebook(Acceuil,name="tabControl")
s = ttk.Style()
s.configure('new.TFrame', background='#fff')

tab1 = ttk.Frame(tabControl , style='new.TFrame')
tab2 = ttk.Frame(tabControl , style='new.TFrame' ,name="tab2")
tab3 = ttk.Frame(tabControl , style='new.TFrame')



tabControl.add(tab1, text ='  Users')


entry1=tk.Label(tab1, text="pseudo " , font=lbl_font, bg='white')
            
entry1.grid(row=0,column=1)
            
entry1=tk.Label(tab1, text="Password ",font=lbl_font, bg='white' )
                        
entry1.grid(row=0,column=2)

entry1=tk.Label(tab1, text=" Type ",font=lbl_font, bg='white' )
                        
entry1.grid(row=0,column=3)
for w,userData in enumerate(Allusers.users):
            
            #button.pack()
            w=w+1
            entry1=tk.Label(tab1, text=userData.pseudo,font=lbl_font, bg='white')
            
            entry1.grid(row=w,column=1)
            
            entry1=tk.Label(tab1, text="*"*len(userData.password),font=lbl_font, bg='white' )
            
            entry1.grid(row=w,column=2)
            
            entry1=tk.Label(tab1, text=userData.userType,font=lbl_font, bg='white' )            
            entry1.grid(row=w,column=3)


def newUser():
    import NewUser
    NewUser.editPassword.mainloop()
button = tk.Button(tab1,text="Ajouter",fg='white', bg='#0096FF',font=lbl_font,command=newUser)
button.grid(row=w+2,column=2)            
            #entry1.pack()

tabControl.add(tab2, text ='Films',)


entry1=tk.Label(tab2, text="nomFilm",font=lbl_font, bg='white' )
                    
                
entry1.grid(row=0,column=2)
                   
entry1=tk.Label(tab2, text=" Reserver Par " , font=lbl_font, bg='white')
                    
entry1.grid(row=0,column=3)
        
entry1=tk.Label(tab2, text="operation ",font=lbl_font, bg='white' )
                    
entry1.grid(row=0,column=4)
        
def rendrFilm(x):
       f=Film(x.nomFilm)
       AllFilms.returnFilm(f)
       AllFilms.saveData()
       for widgets in tab2.winfo_children():
               widgets.destroy()
       remplirFilms()
def reserveFilm(filmname,user1):
    pass
    f=Film(filmname)
    print(f)
    user1=User(user1.get())
    print(user1)
    AllFilms.borowFilm(f,user1)
    AllFilms.saveData()
    for widgets in tab2.winfo_children():
               widgets.destroy()
    remplirFilms()
    
def addfilm():
            
            filmname=root.nametowidget("acceuil.tabControl.tab2.filmname").get()
            newFilm=Film(filmname)
            try:
                AllFilms.addFilm(newFilm)
                AllFilms.saveData()
                for widgets in tab2.winfo_children():
                        widgets.destroy()
                remplirFilms()
               
            except Exception as e :
                messagebox.showerror("Error",str(e))
                #print(,str(e))
            
            

import functools


def remplirFilms():
    for w,film in enumerate(AllFilms.films):
                    
                    #button.pack()
                    
                    w=w+1
                   
                    entry1=tk.Label(tab2, text=film.nomFilm,font=lbl_font, bg='white' )
                    
                
                    entry1.grid(row=w,column=2)
                    if film.user:
                                    entry1=tk.Label(tab2, text=film.user.pseudo, font=lbl_font, bg='white')
                    else:
                            entry1=tk.Label(tab2, text="-",font=lbl_font, bg='white' )
                    entry1.grid(row=w,column=3)
                    if film.user:
                            button = tk.Button(tab2,text="Rendre",fg='white', bg='#0096FF',command=functools.partial(rendrFilm, x=film))
                            button.grid(row=w,column=4)                   
                    else:
                            
                        
                        user_cb = ttk.Combobox(tab2 )
                        
                        # get first 3 letters of every month name
                        user_cb['values'] = [user1.pseudo for user1 in Allusers.users if user1.userType!="admin"]
                        
                     
                        user_cb.grid(row=w,column=4)
                        button = tk.Button(tab2,text="reserver",fg='white', bg='#0096FF',command=functools.partial(reserveFilm,user1=user_cb,filmname=film.nomFilm))
                        button.grid(row=w,column=5)
    
    entry1=tk.Label(tab2, text="nomFilm",font=lbl_font, bg='white' )
                    
                
    entry1.grid(row=w+2,column=2)
    
    user_input = tk.StringVar(root)
    
    filmname=tk.Entry(tab2, font=lbl_font,name="filmname",textvariable=user_input, bg='white' )
                    
                
    filmname.grid(row=w+2,column=3)
    
    button = tk.Button(tab2,text="Ajouter",fg='white',
                           bg='#0096FF',command=addfilm)
    button.grid(row=w+2,column=4)   
 
        
   

w=remplirFilms()


        
        
        
        

#filmsPage()
tabControl.add(tab3, text ='Others ',)

tabControl.pack(expand = 1, fill ="both")

def deconnecter():
   
    #Acceuil.forget()
    root.withdraw()
    root.destroy()
    
    import loginForm
    loginForm.main()
    #login.pack(fill='both', expand=1) 
loguout = tk.Button(tab3, text='logout ', fg='white', bg='#0096FF')
loguout.config(width=8, height=1,
                font=txt_font,
                command=deconnecter)
loguout.pack(pady=20)
def modifier():
    import modifierMDP
    
    modifierMDP.editPassword.mainloop()
editPassword2 = tk.Button(tab3, text='edit Password ', fg='white', bg='#0096FF')
editPassword2.config(width=18, height=1,
                font=txt_font,
                command=modifier)
editPassword2.pack(pady=20)


cl = tk.Button(tab3, text='Close ', fg='white', bg='#0096FF')
cl.config(width=18, height=1,
                font=txt_font,
                command=root.destroy )
cl.pack(pady=20)






#________________________Main___________________
Acceuil.pack(fill='both', expand=1)


def main():
    
    root.mainloop()
    
if __name__=='__main__':
    main()
    