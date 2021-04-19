from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    all_projects = projects.objects.all()

    # proje = projects.objects.filter(projects=all_projects[0])
    # proje1 = projects.objects.filter(projects=all_projects[1])

    # context = {"all_pro":all_projects,"projects":proje,"projects1":proje1}
    anniproducts = []
    catprods= projects.objects.values('domainname', 'id')
    cats= {item["domainname"] for item in catprods}
    reviews = False
    blogs = False
    print(cats)
    for cat in cats:
        prod=projects.objects.filter(domainname=cat)
        nSlides = len(prod)
        anniproducts.append([prod, nSlides,cat])
    print(anniproducts)
    context ={"allprojects":anniproducts,"reviews":reviews}
    return render(request,"index.html",context)
def HomePage(request):
    s = blog.objects.all()
    
    
    all_post = blog.objects.all().order_by('-pub_date')
    contesxt = {"all_posts":all_post}

    return render(request,'blog.html',contesxt)

def post(request,slug):
    bloga = blog.objects.filter(slug=slug).first()
    
    context = {'blog': bloga}
    return render(request, 'post.html',context)