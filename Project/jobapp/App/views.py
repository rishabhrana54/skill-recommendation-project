from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import pandas as pd

connection = pymysql.connect(host='localhost',port=3306,database='jobapp',user='root',autocommit = True)
cursor = connection.cursor()


skills = [["html","css","html5","css3","javascript","jquery","angular","react","angular 8","PWA"],
["php","wordpress","joomla","cms","magento","cake"],["java","jsp","servlets","jdbc","jfs","ejb","struts","spring","hibernate"],
["c",'c++','c#','.net','asp.net','.net framework'],
['python','django','flask','css','bootstrap','jquery','bootstrap','machine learning','data science','data analysis']]



def index(req):
    return render(req, 'index.html')

def register(req):
    return render(req, 'register.html')

def registerUser(req):
    username = req.POST['username']
    useremail = req.POST['usermail']
    userpwd = req.POST['userpwd']
    usermobile = req.POST['usernum']

    query = "insert into users values (%s,%s,%s,%s)"
    cursor.execute(query, (username,useremail,userpwd,usermobile))
    return render(req, 'editProfile.html', context={"email":useremail})

def editProfile(req,pk):
    return render(req, 'editProfile.html',{"email":pk})

def viewProfile(req,pk):
   
    query="select * from userProfile where email = %s"
    cursor.execute(query, (pk))
    data = cursor.fetchall()
    print(data)
    return render(req, 'viewProfile.html',{"data":data,"email":pk})


def submitProfile(req):
    email = req.POST['email']
    qualification = req.POST['qualification']
    college = req.POST['clg']
    obj = req.POST['obj']
    skills_submitted = req.POST['skills']
    cat = req.POST['cat']
    exp = req.POST['exp']
    
    query = "select * from userprofile where email = %s"
    cursor.execute(query,(email))

    data = cursor.fetchall()
    if(len(data)) >= 1:
        # update query
        query = "UPDATE userprofile SET skills=%s WHERE email=%s"
        cursor.execute(query,(skills_submitted,email))
        
    else:
        query = "insert into userprofile values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(email,qualification,college,obj,cat,skills_submitted,exp))
        data = cursor.fetchall()
        
    
    query = "select skills from userProfile where email = %s"
    cursor.execute(query,(email))
    userSkills = cursor.fetchall()
   
    if len(userSkills) < 1:
        return render(req, 'skillsuser.html', context={"data":data,"email":email})
    else:

        similarity = []
        for i in range(len(skills)):
            sim = len(set(skills[i]).intersection(userSkills[0])) / len(set(skills[i]).union(userSkills[0]))
            similarity.append([i,sim])
            sortedSim = sorted(similarity, key=lambda x : x[1],reverse=True)
        
       
        recommended = skills[sortedSim[0][0]]
        query = "select skills from userProfile where email = %s"
        cursor.execute(query,(email))
        userSkills = cursor.fetchall() 
        # print(recommended)

        return render(req, 'skillsuser.html', context={"data":data,"email":email,"recommended":recommended})


def loginUser(req): 
    # print(str(type(req)))
    print(req.POST)
    email = req.POST['email']
    pwd = req.POST['pwd']

    return render(req, 'login.html', context={"email":email})

def skillsuser(req):
     return render(req, 'skillsuser.html')

