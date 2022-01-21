# -*- coding: utf-8 -*-
"""
@author: F.Talbot
"""
from users import Users
class Film:
    def __init__(self,nomFilm,user=None):
            self.nomFilm,self.user=nomFilm,user
    def __repr__(self):
        if self.user is None:
            return  "{},".format(self.nomFilm) 
        else:   
            return "{},{}".format(self.nomFilm,self.user.pseudo) 
    def __eq__(self,other):
        return self.nomFilm==other.nomFilm
class Films:
    def __init__(self,path="data/films.txt",delimiter=","):
        self.films=[]
        self.path=path
        import os
        if not os.path.exists(path):
             with open(path,"w") as f:
                 f.close()
        with open(path,"r") as f :
            lines=f.readlines()
            for line in lines:
                line=line.replace("\n","").split(delimiter)
             
                if line[1]!="":
                    user=(Users.getUserByPseudo(line[1]))
                    film=Film(line[0],user)
                   
                else:
                    film=Film(line[0])
                #print(film)
                self.films.append(film)
    def saveData(self):
        with open(self.path,"w") as f:
            for film in self.films:
                f.write(str(film)+"\n")
    def filmDisp(self):
        filmDisp=[film for film in self.films if film.user is None]
        if filmDisp:
            for film in filmDisp:
                print(film.nomFilm)
        else:
            print("no film disp")
    def userFilms(self,user):
        l=[]
        
        for film in self.films:
            if not film.user is None:
                
                      
                if film.user.pseudo==user.pseudo:
                    l.append(film.nomFilm)
        if len(l)==0:
            print("no film")
        else:
            for film in l:
                print(film)
    def AllFilms(self):
     
        
        if self.films:
            for film in self.films:
                
                print(film.nomFilm,end="\t")
                user=str(film).split(",")[1]
                if user:
                    print(user.upper())
                else:
                    print("Dispo ")
        else:
            print("no films" )
                
    def addFilm(self,film):
        if film in self.films:
            print("film already exist")
            return 
        else:
            self.films.append(film)
    def returnFilm(self,film):
        if film not in self.films:
            print("film does not  exist")
            return 
        else:
            indexUs=self.films.index(film)
            if self.films[indexUs].user:
                self.films[indexUs]=film
            else:
                print("film deja chez nous")
    def borowFilm(self,film,user):
        if film not in self.films:
            print("we don't have such film {} ".format(film.nomFilm))
            return 
        index=self.films.index(film)
        if self.films[index].user:
            print("film is not avaible ")
        else:
             self.films[index].user=user

 