# -*- coding: utf-8 -*-
"""
@author: F.Talbot
"""
from users import User,Users
from films import Film,Films


def menuToutuser():
    return (""" choisir une option :
    1: Login
    2: consulter la liste des films disponible 
    3: Quitter 
    """)

def menuUserSimple():
    return (""" choisir une option :
    1: consulter la liste des films
    2: modifier password
    3: Deconnecter 
    """)

def menuUserAdmin():
    return (""" choisir une option :
    1: consulter la liste des films
    2: consulter la liste des utilisateurs
    3: modifier  password
    4: ajouter un film
    5: ajouter un utilisateur
    6: reserver Film 
    7: rendre Film
    8: Deconnecter 
    """)

users=Users()
films=Films()
def main():
    while True:
            menuToutuser()
            choix=input(menuToutuser())
            if choix=="1":
                pseudo=input("Login :")
                password=input("Password :")
                user=User(pseudo,password)
                try:
                    user =users.loginUser(user)
                  
                    if not user:
                        print("Login ou password incorrect")
                    else:
                        
                        print("****************")
                        print("welcome {} ".format(user.pseudo ))
                        
                        print("****************")
                        userType=user.userType
                        
                        if userType=="simple":
                            while True:
                                option=input(menuUserSimple())
                                
                                if option=="1":
                                     
                                     films.userFilms(user)
                               
                                if option=="2":
                                    mdp=input("nouveau password ")
                                    users.editUserPassword(user,mdp)
                                    users.saveData()
                                elif option=="3":
                                     break
                                
                        elif userType=="admin" :
                            while True:
                                option=input(menuUserAdmin())
                                if option=="1":
                                     films.AllFilms()
                                if option=="2":
                                    users.printAllUser()
                                if option=="3":
                                    mdp=input("Nouveau password : ")
                                    users.editUserPassword(user,mdp)
                                    users.saveData()
                                elif option=="4":
                                     nomdeFilm=input("Nom du film  : " )
                                     film=Film(nomdeFilm)
                                     films.addFilm(film)
                                 
                                     films.saveData()
                                elif option=="5":
                                    pseudo=input("Nom d'utilisateur : ")
                                    password=input("password  : ")
                                    user=User(pseudo, password)
                                    users.addUser(user)
                                    users.saveData()
                                elif option=='6':
                                    filmName=input("le nom du film  : ")
                                    film=Film(filmName)
                                    pseudo=input("Nom d'utilisateur  : ")
                                    user=User(pseudo)
                                    
                                    if user  in users.users: 
                                        print(user)
                                        films.borowFilm(film,user)
                                        films.saveData()
                                    else:
                                        print('wrong user ')
                                    
                                elif option=="7":
                                    filmName=input("Nom du film : ")
                                    film=Film(filmName)
                                    films.returnFilm(film)
                                    films.saveData()
                                elif option=="8":
                                    break
                                
                except Exception as e:
                    print(" compte n'existe pas  "+str(e))
            elif choix=="2":
                films.filmDisp()
            elif choix=="3":
                break
            else:
                print("option Non valide ")
main()
print("Have a good day :D ")
            
    