from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    aboutme = AboutMe.objects.first()
    education = EducationExperience.objects.all()
    project = Project.objects.all()
    skill = Skill.objects.all()
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()

    context = {
        'aboutme': aboutme,
        'education': education,
        'projects': project,
        'skills': skill,
        'services': services,
        'portfolio': portfolio,
    }
    return render(request,'index.html',context)