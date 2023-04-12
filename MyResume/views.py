from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutme_view(request):
    
    return render(request, 'aboutme.html')

def skills_view(request):


    skills={
        'python':60,
        'javascript':60,
        'jquery':100,
        'sql':70,
        'django':20
    }

    context={'skills':skills}

    return render(request,'skills.html',context)

def qualification(request):
    study = {
        'SSC':{'Sr':1 ,'study':'SSC' , 'board': 'Maharasthra' , 'marks' :63},
        'HSC':{'Sr':2 ,'study':'HSC' , 'board': 'Maharasthra' , 'marks' :53},
        'BSC':{'Sr':3 ,'study':'BSC' , 'board': 'MumbaiUnivercity' ,'marks' :7.3},
    }

    context = {'study':study}

    return render(request,'qualification.html',context)

def projects_view(request):
    projects = {
        'project1' : {'SR': 1 ,'Topic' :  'Hotel managment system' , 'Technology' : 'Html,Css,js,Python,sql','year' : 2022},
        'project2' : {'SR': 2 ,'Topic' :  'Bank managment system' , 'Technology' : 'Python & sql','year' : 2023},
        'project3' : {'SR': 3 ,'Topic' :  ' Hotel Room Booking system' , 'Technology' : 'Python & sql','year' : 2023},
        
        
        
    }


    context = {'projects' : projects}

    return render(request,'projects.html',context)

def Experience_view(request):

    return render(request,'Experience.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        p = request.POST.get('purpose')

        # print(name)
        # print(email)
        # print(p)
        

        context = {'name' : name}
        return render(request , 'Thanks.html',context)

    return render(request,'contactUS.html')