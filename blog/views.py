from django.shortcuts import render, get_object_or_404
from .models import contact, Blog
# Create your views here.

#from django.http import HttpResponse

def index(request):
    return render(request, 'blog/home.html')

def blogs(request):
    var_1 = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'var_1': var_1})  

def detail(request, blog_id):
    detail_page = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail_blog': detail_page})      

def contacts(request):
    if request.method == 'POST':
        Your_name = request.POST.get('name')
        Your_email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Your_message = request.POST.get('message')

        var_contact = contact(name=Your_name, email=Your_email, subject=Subject, messages=Your_message)
        var_contact.save()
        return render(request, 'blog/thanks.html') 
    else:
        return render(request, 'blog/contacts.html') 

def project_detail1(request):
    return render(request, 'blog/project_detail1.html') 

def project_detail2(request):
    return render(request, 'blog/project_detail2.html') 

def project_detail3(request):
    return render(request, 'blog/project_detail3.html')                

