# -*- coding: utf-8 -*-
"""
@author: F.Talbot
"""

class User:
   
    def __init__(self,pseudo,password="",userType="simple"):
            self.pseudo,self.password,self.userType=pseudo,password,userType
    def __repr__(self):
        
        return "{},{},{}".format(self.pseudo,self.password,self.userType)
    def __eq__(self,other):
        return self.pseudo==other.pseudo
import os 
class Users:
    def __init__(self,path="data/users.txt",delimiter=","):
        self.users=[]
        self.path=path
        if not os.path.exists(path):
             with open(path,"w") as f:
                 f.write("ad,ad,admin\n")
                 f.close()
        with open(path,"r") as f :
            lines=f.readlines()
            for line in lines:
                line=line.replace("\n","").split(delimiter)
                user=User(line[0].strip(),line[1].strip(),line[2].strip())
                self.users.append(user)
    @staticmethod
    def getUserByPseudo(pseudo):
        users=Users().users
        if User(pseudo) in users:
            ind= users.index(User(pseudo))
            
            return users[ind] 
      
        
        raise Exception("no such user ")
    def printAllUser(self):
        if self.users:
            print("pseudo\tpasswrod \tType ")
            print("------\t---------\t-----")
            for user in self.users:
                print(user.pseudo+"\t"+"*"*len(user.password)+"\t\t"+user.userType)
        else:
            print("no user ")
    def saveData(self):
        with open(self.path,"w") as f:
            for user in self.users:
                f.write(str(user)+"\n")
    def addUser(self,user):
        if user in self.users:
            print("user already exist")
            return 
        else:
            self.users.append(user)
    def editUserPassword(self,user,password):
        if user not in self.users:
            print("user does not  exist")
            return 
        else:
            indexUs=self.users.index(user)
            self.users[indexUs].password=password


    def loginUser(self,user):
        indexUs=self.users.index(user)
        user2= self.users[indexUs]
        if  user.password==user2.password and user.pseudo==user2.pseudo:
            return user2
        return False
