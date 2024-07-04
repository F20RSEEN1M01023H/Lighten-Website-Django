from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"About.html")
def product(request):
    return render(request,"Product.html")
def blog(request):
    return render(request,"Blog.html")
def signup(request):
    return render(request,"sign up.html")


