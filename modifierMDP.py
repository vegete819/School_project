# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

from tkinter import * 


from tkinter.messagebox import *
  

from users import Users

users=Users()


def screen_geometry():
    width, height = 660, 500
    # root.geometry('%dx%d+0+0' % (width, height))

    screen_width = editPassword.winfo_screenwidth()
    screen_height = editPassword.winfo_screenheight()
    # root.geometry('%dx%d+0+0' % (screen_width, screen_height))

    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    editPassword.geometry('{}x{}+{}+{}'.format(width, height, x_cord, y_cord))
    
    editPassword.configure(bg='white')


 
editPassword = tk.Tk()

# config the editPassword window
editPassword.geometry('500x300')
editPassword.resizable(False, False)
editPassword.title('Combobox Widget')
screen_geometry()
# label
label = ttk.Label(editPassword,text="Please select a User")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
user_cb = ttk.Combobox(editPassword, )

# get first 3 letters of every month name
user_cb['values'] = [user.pseudo for user in users.users]

# place the widget
user_cb.pack(fill=tk.X, padx=5, pady=5)



input_text = StringVar()

label = ttk.Label(editPassword,text="Please write old password")
label.pack(fill=tk.X, padx=5, pady=5)
entry1 = ttk.Entry(editPassword,show='*', textvariable = input_text, )   

entry1.pack(fill=tk.X, padx=5, pady=5)

input_text2 = StringVar()

label2 = ttk.Label(editPassword,text="Please write new password")
label2.pack(fill=tk.X, padx=5, pady=5)
entry2 = ttk.Entry(editPassword,show='*', textvariable = input_text2, )   

entry2.pack(fill=tk.X, padx=5, pady=5)



input_text3 = StringVar()

label3 = ttk.Label(editPassword,text="Please rewrite new password")
label3.pack(fill=tk.X, padx=5, pady=5)
entry3 = ttk.Entry(editPassword, show='*',textvariable = input_text3, )   

entry3.pack(fill=tk.X, padx=5, pady=5)

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure ?')
    if answer:
        userpseudo=user_cb.get()
        if userpseudo:
                user=users.getUserByPseudo(userpseudo)
                if user.password==entry1.get() and  entry2.get()==entry3.get():
                    users.editUserPassword(user,entry2.get())
                    users.saveData()
                    answer = showinfo(title='confirmation',
                            message='Mot de passe modifié :D ')
                    editPassword.withdraw()
                    editPassword.destroy()
                   
                else:
                     answer = showerror(title='Error',
                            message=' mot de passe faux ou les 2 nouveaux mdp ne sont pas identique ')
        else:
               answer = showerror(title='Attention',
                            message='il faut  choisir un user ')
     
save = ttk.Button(editPassword, text = 'Save', command = confirm)
save.pack(side = TOP, pady = 10)


if __name__=="__main__":
    editPassword.mainloop()